#!/usr/bin/env python
"""Create a csv of stimuli with data extracted from filenames."""
import os
import pandas


def create_stim_info():
    filenames = [x for x in os.listdir("vids") if x.endswith(".mp4")]

    # filenames = []
    # for x in os.listdir("vids"):
    #     if x.endswith(".mp4"):
    #         filenames.append(x)

    stim_info = pandas.DataFrame({"filename": filenames})

    # extract stimulus info from filename
    re_filename = r"(?P<gender>[mf])_(?P<person_id>\d)_(?P<gaze>NC|EC)_(?P<direction>L|R)\.mp4"
    filename_data = stim_info.filename.str.extract(re_filename, expand=True)
    stim_info = stim_info.join(filename_data)

    # convert strings to numbers
    stim_info.loc[:, "person_id"] = pandas.to_numeric(stim_info.loc[:, "person_id"])


    return stim_info


if __name__ == "__main__":
    stim_info = create_stim_info()
    stim_info.to_csv("stim_info.csv", index=False)
