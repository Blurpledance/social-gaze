import yaml
from psychopy import visual, event, core, sound


class Experiment:
    def __init__(self):
        """Initialize the experiment.

        >>> experiment = Experiment()
        """
        self.texts = yaml.load(open("texts.yaml"))
        self.win = visual.Window(units="pix")

        self.fix = visual.TextStim(self.win, text="+", color="white")
        self.noise = sound.Sound("noise.wav")

    def __call__(self):
        """Run the experiment.

        >>> experiment = Experiment()  # initialize the experiment
        >>> experiment()               # call the experiment to run it
        """
        self.show_instructions()
        self.run_trial()

    def show_instructions(self):
        instructions = visual.TextStim(self.win, text=self.texts["instructions"], color="white")
        instructions.draw()
        self.win.flip()
        event.waitKeys()

    def run_trial(self):
        mov = visual.MovieStim(self.win, filename="vids/f_1_EC_L.mp4")

        self.fix.draw()
        self.win.flip()
        self.noise.play()
        core.wait(0.25)

        key, rt = "", -1
        timer = core.Clock()
        while timer.getTime() < 4:
            mov.draw()
            self.win.flip()
            response = event.getKeys(keyList=["right", "left"], timeStamped=timer)
            if len(response) > 0:
                key, rt = response[0]
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
    parser.add_argument("--show-instructions", action="store_true")
    parser.add_argument("--run-trial", action="store_true")
    args = parser.parse_args()

    experiment = Experiment()  # initialize the experiment
    if args.show_instructions:
        experiment.show_instructions()
    elif args.run_trial:
        experiment.run_trial()
    else:
        experiment()
