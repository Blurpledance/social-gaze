#!/usr/bin/env python
import os
import pandas
import numpy


def generate_trials(subj_id, seed=None):

    # initialize a pseudo random number generator
    if seed is None:
        subj_id_hash = abs(hash(subj_id))
        seed = int(str(subj_id_hash)[-6:])
    random = numpy.random.RandomState(seed=seed)

    # create the trials dir if it doesn't exist
    trials_dir = "trials"
    if not os.path.isdir(trials_dir):
        os.mkdir(trials_dir)

    # read in the stim info
    stim_info = pandas.read_csv("stim_info.csv")

    # create trials from stim info
    trials = stim_info.copy()

    # shuffle the trials
    trials = trials.sample(len(trials), random_state=random)

    # insert columns
    trials.insert(0, "subj_id", subj_id)
    trials.insert(1, "trial_ix", list(range(len(stim_info))))

    # write trials to a file
    subj_trials_path = os.path.join(trials_dir, "trials-{subj_id}.csv".format(subj_id=subj_id))
    trials.to_csv(subj_trials_path, index=False)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("subj_id")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    generate_trials(args.subj_id, seed=args.seed)
