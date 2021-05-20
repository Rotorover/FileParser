# This script should Parse files and concatinate content
import os

# folder_1 =  PureWindowsPath("C:\_Temp\benchmarkstt\GCP Transcribe")
file_orig = input("Enter file name: ")
file_post = (file_orig + "_post.txt")
# GCP uses 27 & -3; AWS uses 38 & -7
trimOffset_start = 27
trimOffset_end = -3

with open(file_orig, "r") as reader:
    for line in reader:
        if "transcript" in line:
            y = line[trimOffset_start:trimOffset_end]
            with open(file_post,'a') as a_writer:
                a_writer.writelines(y)

# the following is just to view the results in the console, but not strictly needed
with open(file_post, "r") as reader:
    print(reader.read())