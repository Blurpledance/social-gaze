#!/usr/bin/env python
import os
import pandas
import numpy


# read in the stim info
stim_info = pandas.read_csv("stim_info.csv")


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

    # generate two blocks of trials: one majority eye contact, one majority no eye contact
    majority_eye_contact_trials = generate_majority_eye_contact_block(random)
    majority_no_eye_contact_trials = generate_majority_no_eye_contact_block(random)

    # randomly assign block order
    blocks = [majority_eye_contact_trials, majority_no_eye_contact_trials]
    random.shuffle(blocks)

    # glue the two blocks of trials together into a single dataframe
    trials = pandas.concat(blocks, keys=[1, 2], names=["block_ix"]).reset_index(level=0)

    # set response type for all trials to active
    trials["response_type"] = "active"

    # insert additional columns
    trials.insert(0, "subj_id", subj_id)
    trials.insert(1, "trial_ix", list(range(len(trials))))

    return trials



def generate_majority_eye_contact_block(random):
    # TODO: sample the correct number of eye contact and no eye contact trials
    # HINT: why does this function require a numpy.random.RandomState object?
    eye_contact_trials = stim_info.loc[stim_info.gaze == "EC", :].sample(n=13, random_state=random)
    no_eye_contact_trials = stim_info.loc[stim_info.gaze == "NC", :].sample(n=7, random_state=random)
    trials = pandas.concat([eye_contact_trials, no_eye_contact_trials])
    # TODO: shuffle the trials in the block
    trials = trials.sample(len(trials), random_state=random)
    trials["block_type"] = "majority_eye_contact"
    return trials


def generate_majority_no_eye_contact_block(random):
    # TODO: sample the correct number of eye contact and no eye contact trials
    # HINT: why does this function require a numpy.random.RandomState object?
    eye_contact_trials = stim_info.loc[stim_info.gaze == "EC", :]
    no_eye_contact_trials = stim_info.loc[stim_info.gaze == "NC", :]
    trials = pandas.concat([eye_contact_trials, no_eye_contact_trials])
    # TODO: shuffle the trials in the block
    trials["block_type"] = "majority_no_eye_contact"
    return trials


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("subj_id")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()
    trials = generate_trials(args.subj_id, seed=args.seed)

    # write trials to a file
    subj_trials_path = os.path.join(trials_dir, "trials-{subj_id}.csv".format(subj_id=subj_id))
    trials.to_csv(subj_trials_path, index=False)
