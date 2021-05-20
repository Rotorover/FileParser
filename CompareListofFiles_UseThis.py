# This program will pass ref and hyp files to benchmarkstt to process the entire directory
# The file naming convention must match the endswith pattern.

from os import listdir
from os.path import isfile, join
import glob
import os

folder_1 = "C:\\_temp\\benchmarkstt\\AzureComparisons\\"
#folder_2 = "C:\\_temp\\benchmarkstt\\AWSComparisons\\"

onlyfiles = [f for f in listdir(folder_1) if isfile(join(folder_1, f))]
ref_file_list = []
hyp_file_list = []

for file in onlyfiles:
    if file.endswith('_ref.txt'):
        ref_file_list.append(file)
            
    elif file.endswith('_hyp.txt'):
        hyp_file_list.append(file)
    
print(ref_file_list)
print(hyp_file_list)

for ref_file in ref_file_list:
    ref_base = ref_file.split('_') 
    for hyp_file in hyp_file_list:
        hyp_base = hyp_file.split('_')
        if ref_base[0] == hyp_base[0]:
            print('files match. Running comparison.')
            results_file = ref_base[0] + '_result.txt'
            os.system('benchmarkstt -r '+ folder_1 + ref_file + ' -h ' + folder_1 + hyp_file + ' --wer --diffcounts > ' + folder_1 + results_file)
            print('Done. The output file is: ' + results_file)

        elif ref_base[0] != hyp_base[0]:
            print("Files don't match, so can't run comparison.")
else:
    print("the comparison is done")



