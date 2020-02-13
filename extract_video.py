#!/bin/bash

import os
import time, re
from shutil import copyfile

def extract_video(start_time, end_time):
    count = 0
    for filename in os.listdir("/var/videos/hls/"):
        count += 1
        filename_prefix = filename.split("-", 1)[0]

        filename_timestamp_str = re.sub(r'.*-', '', filename);
        filename_timestamp_str = filename_timestamp_str.split(".", 1)[0]

        try:
            filename_timestamp_int = int(filename_timestamp_str)
            # if filename between timestamp, then cp file to folder on home
            if (filename_timestamp_int >= start_time) and (filename_timestamp_int <= end_time):
                # cam3
                if('camhd3' in filename_prefix):
                    # print(filename)
                    copyfile('hls/' + filename, '/var/videos/extract_cam_3/' + filename)

                # cam6
                elif('camhd6' in filename_prefix):
                    # print(filename)
                    copyfile('hls/' + filename, '/var/videos/extract_cam_6/' + filename)

                # cam9
                elif('camhd9' in filename_prefix):
                    # print(filename)
                    copyfile('hls/' + filename, '/var/videos/extract_cam_9/' + filename)

                # cam12
                elif('camhd12' in filename_prefix):
                    # print(filename)
                    copyfile('hls/' + filename, '/var/videos/extract_cam_12/' + filename)

        except ValueError:
            continue

def main():
    # Destination folder for videos
    video_dest = '/var/videos/'

    # create folders
    camera_names = ['extract_cam_3', 'extract_cam_6', 'extract_cam_9', 'extract_cam_12']
    for folder_name in camera_name:
        create_command = "sudo mkdir /var/videos/" + folder_name
        os.system(create_command)

    start_time = "1581425160000"
    end_time = "1581425400000"
    extract_video(start_time, end_time)

if __name__ == '__main__':
    main()
