#!/usr/bin/env python
"""Create a csv of video data extracted from filenames."""
import os
import pandas

stim_codes = {
    "gender": {"m": 0, "f": 1},
    "gaze": {"NC": 0, "EC": 1},
    "direction": {"L": 0, "R": 1},
}

def create_stim_code(row):
    stim_code_values = []
    for col_name, map in stim_codes.items():
        stim_code_values.append(str(map[row[col_name]]))
    return ''.join(stim_code_values)


def create_stim_info():
    filenames = [x for x in os.listdir("stimuli/videos") if x.endswith(".mp4")]

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

    stim_info["stim_code"] = stim_info.apply(create_stim_code, axis=1)

    return stim_info


if __name__ == "__main__":
    stim_info = create_stim_info()
    stim_info.to_csv("video_info.csv", index=False)
