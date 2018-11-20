#!/usr/bin/env python
"""Create a csv of stimuli with data extracted from filenames."""
import os
import pandas


def create_stim_info():
    filenames = [x for x in os.listdir("vids") if x.endswith(".avi")]

    # filenames = []
    # for x in os.listdir("vids"):
    #     if x.endswith(".avi"):
    #         filenames.append(x)

    stim_info = pandas.DataFrame({"filename": filenames})

    # extract stimulus info from filename
    re_filename = r"(?P<gender>[mf])_(?P<person_id>\d)_(?P<gaze>NC|EC)_(?P<direction>left|right)_(?P<speed>\d)\.avi"
    filename_data = stim_info.filename.str.extract(re_filename, expand=True)
    stim_info = stim_info.join(filename_data)

    # convert strings to numbers
    stim_info.loc[:, "person_id"] = pandas.to_numeric(stim_info.loc[:, "person_id"])
    stim_info.loc[:, "speed"] = pandas.to_numeric(stim_info.loc[:, "speed"])

    # label race based on person ids
    stim_info["race"] = stim_info.person_id.apply(lambda person_id: "white" if person_id <= 4 else "black")

    return stim_info


if __name__ == "__main__":
    stim_info = create_stim_info()
    stim_info.to_csv("stim_info.csv", index=False)
