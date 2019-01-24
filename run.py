import yaml
from psychopy import visual, event, core, sound, gui

from generate_trials import generate_trials


def get_runtime_vars():
    runtime_vars = {"subj_id": "SUBJ100"}
    dlg = gui.DlgFromDict(runtime_vars)
    if not dlg.OK:
        core.quit()
    return runtime_vars


class Experiment:
    def __init__(self, subj_id):
        """Initialize the experiment.

        Args:
            subj_id (str): identifier for subject

        >>> experiment = Experiment("SUBJ100")
        """
        self.texts = yaml.load(open("texts.yaml"))
        self.win = visual.Window(units="pix")
        self.trials = generate_trials(subj_id=subj_id)
        self.datafile = open("{subj_id}.csv".format(subj_id=subj_id), "w", 0)
        self.breaktext = yaml.load(open("break.yaml"))
        self.baseline = yaml.load(open("baseline.yaml"))
        self.recording = yaml.load(open("recording.yaml"))
        self.getready = yaml.load(open("getready.yaml"))


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

    def show_baseline(self):
        baseline = visual.TextStim(self.win, text=self.baseline["baseline"], color="white")
        baseline.draw()
        self.win.flip()
        event.waitKeys()

    def show_recording(self):
        recording = visual.TextStim(self.win, text=self.recording["recording"], color="white")
        recording.draw()
        self.win.flip()
        core.wait(300)

    def show_getready(self):
        getready = visual.TextStim(self.win, text=self.getready["getready"], color="white")
        getready.draw()
        self.win.flip()
        event.waitKeys()

    def show_break_screen(self):
        break_screen = visual.TextStim(self.win, text=self.breaktext["break_screen"], color="white")
        break_screen.draw()
        self.win.flip()
        event.waitKeys()

    def show_instructions(self):
        instructions = visual.TextStim(self.win, text=self.texts["instructions"], color="white")
        instructions.draw()
        self.win.flip()
        event.waitKeys()

    def run_trial(self, trial):
        mov = visual.MovieStim3(self.win, filename=trial["filename"])

        self.fix.draw()
        self.win.flip()
        self.noise.play()
        core.wait(0.8)

        key, rt = "", -1
        timer = core.Clock()
        while timer.getTime() < 6:
            mov.draw()
            self.win.flip()
            response = event.getKeys(keyList=["right", "left", "q"], timeStamped=timer)
            if len(response) > 0:
                is_first_key = (key == "")
                if is_first_key:
                    key, rt = response[0]
                if key == "q":
                    core.quit()
        else:
            print("no response!")

        trial_data = {
            "key": key,
            "rt": rt,
        }

        return trial_data

    def write_trial_data(self, trial_data):
        row = ",".join(map(str, trial_data.values()))
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
        subj_id = runtime_vars["subj_id"]

    # Initialize the experiment
    experiment = Experiment(subj_id=subj_id)

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
