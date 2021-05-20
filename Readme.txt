i wrote parsefiles.py for examining specific transcript files from speach to text engines, 
and as an excercise in doing file ops in python. JS 12/1/20

GCP puts chunks of the transcript into separate transcript fields so you need to search for those
and then concatinate it into one string. 

AWS returns a json file that must be first formatted in VS so that its not on one line, 
and then you can run it through parsefiles.  

The offsets for trimming must be set for each. 

to run this make sure Python 3.x is installed and then from prompt ($) python parsefiles.py

for now put the files in the path where the script is located. I'll add path handlers later. 

with open() as reader|writer automatically closes a file after you read or write to it.  
if you did just open() you'd have to explicitly close the file. 