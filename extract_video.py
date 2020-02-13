#!/bin/bash

import os
import sys
import time, re
from shutil import copyfile
from datetime import datetime

def extract_video(start_time, end_time):
    for filename in os.listdir("/var/videos/hls/"):
        filename_prefix = filename.split("-", 1)[0]

        filename_timestamp_str = re.sub(r'.*-', '', filename);
        filename_timestamp_str = filename_timestamp_str.split(".", 1)[0]

        try:
            filename_timestamp_int = int(filename_timestamp_str)
            # if filename between timestamp, then cp file to folder on home
            if (filename_timestamp_int >= int(start_time)) and (filename_timestamp_int <= int(end_time)):

                # cam3
                if('camhd3' in filename_prefix):
                    # print(filename)
                    copyfile('/var/videos/hls/' + filename, '/var/videos/extract_cam_3/' + filename)

                # cam6
                elif('camhd6' in filename_prefix):
                    # print(filename)
                    copyfile('/var/videos/hls/' + filename, '/var/videos/extract_cam_6/' + filename)

                # cam9
                elif('camhd9' in filename_prefix):
                    # print(filename)
                    copyfile('/var/videos/hls/' + filename, '/var/videos/extract_cam_9/' + filename)

                # cam12
                elif('camhd12' in filename_prefix):
                    # print(filename)
                    copyfile('/var/videos/hls/' + filename, '/var/videos/extract_cam_12/' + filename)

        except ValueError:
            continue

def check_video_time_range():

    oldest_time = sys.maxint
    newest_time = -sys.maxint - 1

    for filename in os.listdir("/var/videos/hls/"):
        filename_prefix = filename.split("-", 1)[0]

        filename_timestamp_str = re.sub(r'.*-', '', filename);
        filename_timestamp_str = filename_timestamp_str.split(".", 1)[0]

        try:
            filename_timestamp_int = int(filename_timestamp_str)

            # check for older created file
            if(filename_timestamp_int < oldest_time):
                oldest_time = filename_timestamp_int

            # check for newer created file
            if(filename_timestamp_int > newest_time):
                newest_time = filename_timestamp_int

        except ValueError:
            continue

    # Print range of videos
    print("Oldest timed video file = ", oldest_time) #, " ", datetime.fromtimestamp(oldest_time))
    print("Newest timed video file = ", newest_time) #, " ", datetime.fromtimestamp(newest_time))

def main():
    # Destination folder for videos
    video_dest = '/var/videos/'

    # create folders
    #camera_names = ['extract_cam_3', 'extract_cam_6', 'extract_cam_9', 'extract_cam_12']
    #for camera_name in camera_names:
    #    create_command = "sudo mkdir /var/videos/" + camera_name
    #    os.system(create_command)

    # check_video_time_range()

    start_time = "1581425160000"
    end_time = "1581425400000"
    extract_video(start_time, end_time)

if __name__ == '__main__':
    main()
