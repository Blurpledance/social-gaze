import yaml
from psychopy import visual, event, core, sound, gui, parallel

from generate_trials import generate_trials


parallel.setPortAddress(0XD020)
parallel.setData(0)


def get_runtime_vars():
    runtime_vars = {"subj_id": "SUBJ100"}
    dlg = gui.DlgFromDict(runtime_vars)
    if not dlg.OK:
        core.quit()
    return runtime_vars


class Experiment:
    ITI = 2.0  # interstimulus interval
    FIXATION_DELAY = 0.8
    VIDEO_DURATION = 6.0
    RECORDING_DURATION = 10
    BREAK_SCREEN_DURATION = 10

    def __init__(self, **runtime_vars):
        """Initialize the experiment.

        Args:
            subj_id (str): identifier for subject

        >>> experiment = Experiment("SUBJ100")
        """
        self.runtime_vars = runtime_vars
        self.texts = yaml.load(open("texts.yaml"))
        self.win = visual.Window(units="pix")
        self.trials = generate_trials(subj_id=runtime_vars["subj_id"])
        self.datafile = open("{subj_id}.csv".format(subj_id=runtime_vars["subj_id"]), "w", 0)
        self.datacols = self.trials.columns.tolist() + ["key", "rt"]

        # write the header
        self.datafile.write(",".join(self.datacols) + "\n")

        self.fix = visual.TextStim(self.win, text="+", color="white", height=150)
        self.noise = sound.Sound("stimuli/sounds/noise.wav")

    def __call__(self):
        """Run the experiment.

        >>> experiment = Experiment("SUBJ100")  # initialize the experiment
        >>> experiment()                        # call the experiment to run it
        """
        self.show_baseline()
        self.show_recording()
        self.show_getready()
        self.show_instructions()

        cur_block = 1
        for _, trial in self.trials.iterrows():
            is_block_transition = (cur_block != trial["block_ix"])
            if is_block_transition:
                self.show_break_screen()
                cur_block = trial["block_ix"]

            trial_data = self.run_trial(trial)
            self.write_trial_data(trial_data)

    def draw_text(self, key):
        text = visual.TextStim(self.win, text=self.texts[key], color="white")
        text.draw()
        self.win.flip()

    def show_baseline(self):
        parallel.setData(int('1', 2))
        self.draw_text("baseline")
        event.waitKeys()

    def show_recording(self):
        self.draw_text("recording")
        core.wait(self.RECORDING_DURATION)

    def show_getready(self):
        self.draw_text("getready")
        event.waitKeys()

    def show_break_screen(self):
        self.draw_text("break_screen")
        core.wait(self.BREAK_SCREEN_DURATION)

    def show_instructions(self):
        self.draw_text("instructions")
        event.waitKeys()

    def run_trial(self, trial):
        parallel.setData(0)
        mov = visual.MovieStim3(self.win, filename=trial["filename"])

        # add interstimulus interval
        self.win.flip()
        core.wait(self.ITI)

        self.fix.draw()
        self.win.flip()
        self.noise.play()
        core.wait(self.FIXATION_DELAY)

        parallel.setData(int(trial["stim_code"], 2))

        key, rt = "", -1
        timer = core.Clock()
        while timer.getTime() < self.VIDEO_DURATION:
            mov.draw()
            self.win.flip()
            response = event.getKeys(keyList=["right", "left", "q"], timeStamped=timer)
            if len(response) > 0:
                is_first_key = (key == "")
                if is_first_key:
                    key, rt = response[0]
                if key == "q":
                    core.quit()

        trial_data = {
            "key": key,
            "rt": rt,
        }
        trial_data.update(self.runtime_vars)
        trial_data.update(trial)

        return trial_data

    def write_trial_data(self, trial_data):
        trial_data_strs = []
        for col_name in self.datacols:
            trial_data_strs.append(str(trial_data[col_name]))

        row = ",".join(trial_data_strs)
        self.datafile.write(row + "\n")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--subj-id")
    parser.add_argument("--show-instructions", action="store_true")
    parser.add_argument("--show-baseline", action="store_true")
    parser.add_argument("--show-recording", action="store_true")
    parser.add_argument("--show-getready", action="store_true")
    parser.add_argument("--run-trial", action="store_true")
    args = parser.parse_args()

    subj_id = args.subj_id
    if subj_id is None:
        runtime_vars = get_runtime_vars()
    else:
        runtime_vars = dict(subj_id=subj_id)

    # Initialize the experiment
    experiment = Experiment(**runtime_vars)

    if args.show_instructions:
        experiment.show_instructions()
    elif args.show_baseline:
        experiment.show_baseline()
    elif args.show_recording:
        experiment.show_recording()
    elif args.show_getready:
        experiment.show_getready()
    elif args.run_trial:
        trial_data = experiment.run_trial({"filename": "stimuli/videos/f_1_EC_L.mp4"})
        print(trial_data)
    else:
        # Run the whole experiment
        experiment()
