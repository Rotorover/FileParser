# Scan dir for files with specific substrings usiung glob 
import glob
import os

os.chdir("C:\\_temp\\benchmarkstt\\Azure Comparisons")
for file in list(glob.glob('*_ref.txt')):
   print(file)

for file in list(glob.glob('*_hyp.txt')):
   print(file)
   
# following will run a python script from this script if you uncomment it. 
#os.system('python JelloWorld.py')