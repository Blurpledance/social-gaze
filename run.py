import yaml
from psychopy import visual, event, core, sound, gui

from generate_trials import generate_trials


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

        self.fix = visual.TextStim(self.win, text="+", color="white")
        self.noise = sound.Sound("noise.wav")

    def __call__(self):
        """Run the experiment.

        >>> experiment = Experiment("SUBJ100")  # initialize the experiment
        >>> experiment()                        # call the experiment to run it
        """
        self.show_instructions()

        for _, trial in self.trials.iterrows():
            self.run_trial(trial)

    def show_instructions(self):
        instructions = visual.TextStim(self.win, text=self.texts["instructions"], color="white")
        instructions.draw()
        self.win.flip()
        event.waitKeys()

    def run_trial(self, trial):
        mov = visual.MovieStim(self.win, filename=trial["filename"])

        self.fix.draw()
        self.win.flip()
        self.noise.play()
        core.wait(0.25)

        key, rt = "", -1
        timer = core.Clock()
        while timer.getTime() < 4:
            mov.draw()
            self.win.flip()
            response = event.getKeys(keyList=["right", "left", "q"], timeStamped=timer)
            if len(response) > 0:
                key, rt = response[0]
                if key == "q":
                    core.quit()
                break
        else:
            print("no response!")

        trial_data = {
            "key": key,
            "rt": rt,
        }

        print(trial_data)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--subj-id")
    parser.add_argument("--show-instructions", action="store_true")
    parser.add_argument("--run-trial", action="store_true")
    args = parser.parse_args()

    if args.subj_id is None:
        runtime_vars = {"subj_id": "SUBJ100"}
        dlg = gui.DlgFromDict(runtime_vars)
        if not dlg.OK:
            core.quit()
        args.subj_id = runtime_vars["subj_id"]

    # Initialize the experiment
    experiment = Experiment(subj_id=args.subj_id)

    if args.show_instructions:
        experiment.show_instructions()
    elif args.run_trial:
        experiment.run_trial({"filename": "vids/f_1_EC_L.mp4"})
    else:
        # Run the whole experiment
        experiment()
