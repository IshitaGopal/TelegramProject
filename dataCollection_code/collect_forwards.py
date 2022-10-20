import os
from config import Config, extract_from_dict, collect_fwds_info
import pandas as pd
import glob as glob
import time
import argparse
import logging


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel_pickleFile", type=str, required=True)
    args = parser.parse_args()
    # logging.basicConfig(level=logging.DEBUG)

    start_time = time.time()

    channel_df_input = args.channel_pickleFile
    fwds_master_file_path = Config.fwds_master_file

    # check if forwards master file exists else create one
    if os.path.exists(fwds_master_file_path) == False:
        fwd_cols = [
            "fwd_from",
            "fwd_id",
            "fwd_username",
            "fwd_title",
            "fwd_user_created",
            "fwd_is_verified",
            "fwd_is_broadcast",
            "fwd_is_megagroup",
            "fwd_is_gigagroup",
        ]
        pd.DataFrame(columns=fwd_cols).to_pickle(fwds_file_path)

    # existing fwd ids collected from other channels
    old_fwds = pd.read_pickle(fwds_master_file_path)
    old_fwd_ids = old_fwds.fwd_id.dropna().astype(int).tolist()

    # get non duplicated fwd ids
    channel_fwd_ids = clean_df[clean_df.fwd_type == "PeerChannel"]["fwd_id"]
    channel_fwd_ids = channel_fwd_ids.drop_duplicates().astype(int).tolist()
    print(f"Total number of unique forwards from channels: {len(channel_fwd_ids)}")

    # collect new fwds which aren't in all_fwds
    new_fwds = [value for value in channel_fwd_ids if value not in old_fwd_ids]
    print(f"Number of new forwards: {len(new_fwds)}")

    if len(new_fwds) > 0:
        new_fwds_df = collect_fwds_info(new_fwds)
        old_fwds = pd.concat([old_fwds, new_fwds_df])
        old_fwds.to_pickle(fwds_file_path)

    # Merge in all_fwds into the main df
    clean_df = clean_df.merge(old_fwds, how="left", on="fwd_id")
    print("Merged in the forwards")
