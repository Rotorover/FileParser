# Scan dir for files with specific substrings usiung glob 
import glob
import os

def get_file_names_with_strings(str_list):
    full_list = os.listdir("C:\\_temp\\benchmarkstt\\Azure Comparisons")
    final_list = [nm for ps in str_list for nm in full_list if ps in nm]

    return final_list
# print(get_file_names_with_strings(['_hyp.txt','_ref.txt']))

for file in get_file_names_with_strings(str_list):
    ref_file = (get_file_names_with_strings(['_ref.txt']))
    hyp_file = (get_file_names_with_strings(['_hyp.txt']))

print(ref_file)
print(hyp_file)
   
# following will run a python script from this script if you uncomment it. 
#os.system('python JelloWorld.py')