#!/bin/bash

import os.path, time, re
from shutil import copyfile
import subprocess
import shutil

def getCountStr(count):
    if count >= 1 and count <= 9:
        return "000" + str(count)
    elif count >= 10 and count <= 99:
        return "00" + str(count)
    elif count >= 100 and count <= 999:
        return "0" + str(count)
    else:
        return str(count)

def convert_to_numbered_mp4(list_dir, source_folder, dest_folder):

    # sequence of files
    file_number = 0

    for filename in list_dir:
        file_number += 1

        filename_prefix = filename.split("-", 1)[0]
        filename_timestamp_str = re.sub(r'.*-', '', filename);
        filename_timestamp_str = filename_timestamp_str.split(".", 1)[0]

        filename_format_ts = ".ts"
        filename_format_mp4 = ".mp4"

        # convert to mp4
        output_file = str(file_number) + filename_format_mp4
        print("Processing {} -> file number {}".format(filename, file_number))
        subprocess.call(['ffmpeg', '-i', (source_folder + filename), output_file])

        # move output_file to its own folder
        shutil.move(output_file, dest_folder + str(file_number) + filename_format_mp4)

def main():
    # Convert to mp4 for 1st folder
    source_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/extract_test_3/'
    dest_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/cam3/'

    # Get a list of files sorted by name
    list_dir = os.listdir(source_folder)
    list_dir = [f for f in list_dir]
    list_dir = sorted(list_dir)

    # Convert ts files to mp4 files with numbered name
    convert_to_numbered_mp4(list_dir, source_folder, dest_folder)
    ## ------------------------

    source_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/extract_test_6/'
    dest_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/cam6/'

    # Get a list of files sorted by name
    list_dir = os.listdir(source_folder)
    list_dir = [f for f in list_dir]
    list_dir = sorted(list_dir)

    # Convert ts files to mp4 files with numbered name
    convert_to_numbered_mp4(list_dir, source_folder, dest_folder)
    # ------------------------

    source_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/extract_test_9/'
    dest_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/cam9/'

    # Get a list of files sorted by name
    list_dir = os.listdir(source_folder)
    list_dir = [f for f in list_dir]
    list_dir = sorted(list_dir)

    # Convert ts files to mp4 files with numbered name
    convert_to_numbered_mp4(list_dir, source_folder, dest_folder)
    # ------------------------

    source_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/extract_test_12/'
    dest_folder = '/Users/shubham/Desktop/Knightscope /Forescout/MIN40/cam12/'

    # Get a list of files sorted by name
    list_dir = os.listdir(source_folder)
    list_dir = [f for f in list_dir]
    list_dir = sorted(list_dir)

    # Convert ts files to mp4 files with numbered name
    convert_to_numbered_mp4(list_dir, source_folder, dest_folder)
    # ------------------------

if __name__ == "__main__":
    main()

