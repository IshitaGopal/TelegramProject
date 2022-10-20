import os
from config import Config, get_cleaned_dataframe
import pandas as pd
import glob as glob
import time
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel_input", type=str, required=True)
    args = parser.parse_args()
    # logging.basicConfig(level=logging.DEBUG)

    start_time = time.time()

    channel_input = args.channel_input

    # get all the paths of all the json files associated with a channel
    json_pattern = os.path.join(Config.jsonChat_dir, channel_input, "*.json")
    all_jsons = glob.glob(json_pattern)

    # read all jsona and convert into a single dataframe
    # keep only relevant fields/columns

    cols = [
        "id",
        "date",
        "message",
        "from_id",
        "fwd_from",
        "reply_to",
        "media",
        "entities",
        "views",
        "forwards",
        "edit_date",
        "ttl_period",
    ]

    dfs = pd.concat([pd.read_json(f)[cols] for f in all_jsons], ignore_index=True)

    # clean dataframe using the get_cleaned_dataframe() function from config.py
    print("cleaning df")
    clean_df = get_cleaned_dataframe(dfs)

    # save the cleaned dataframe
    # format: channel_input.pkl
    pkl_name = channel_input + ".pkl"
    pkl_name_path = os.path.join(
        Config.processed_dir, Config.chatDf_dir, channel_input, pkl_name
    )
    clean_df.to_pickle(pkl_name_path)
