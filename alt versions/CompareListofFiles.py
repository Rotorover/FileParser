# This program will pass ref and hyp files to benchmarkstt to process the entire directory
# The file naming convention must match the endswith pattern.

from os import listdir
from os.path import isfile, join
import glob
import os

folder_1 = "C:\\_temp\\benchmarkstt\\AzureComparisons\\new\\"
#folder_2 = "C:\\_temp\\benchmarkstt\\AWSComparisons\\"

onlyfiles = [f for f in listdir(folder_1) if isfile(join(folder_1, f))]

for file in onlyfiles:

    if file.endswith('_refx.txt'):
        ref_file=file
    
    elif file.endswith('_hyp.txt'):
        hyp_file=file
    
ref_base = ref_file.split('_') 
hyp_base = hyp_file.split('_')
print('The ref file is: ' + ref_base[0])
print('The hyp file is: ' + hyp_base[0])
results_file = ref_base[0] + '_result.txt'

if ref_base[0] == hyp_base[0]:
    print('files match. Running comparison.')
    os.system('benchmarkstt -r '+ folder_1 + ref_file + ' -h ' + folder_1 + hyp_file + ' --wer --diffcounts > ' + folder_1 + results_file)
    print('Done. The output file is: ' + results_file)
else:
    print("Files don't match, so can't run comparison.")




