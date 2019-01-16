import yaml
from psychopy import visual, event


class Experiment:
    def __init__(self):
        """Initialize the experiment.

        >>> experiment = Experiment()
        """
        self.texts = yaml.load(open("texts.yaml"))
        self.win = visual.Window(units="pix")

    def __call__(self):
        """Run the experiment.

        >>> experiment = Experiment()  # initialize the experiment
        >>> experiment()               # call the experiment to run it
        """
        self.show_instructions()

    def show_instructions(self):
        instructions = visual.TextStim(self.win, text=self.texts["instructions"], color="white")
        instructions.draw()
        self.win.flip()
        event.waitKeys()


if __name__ == "__main__":
    experiment = Experiment()  # initialize the experiment
    experiment()               # call the experiment to run it
