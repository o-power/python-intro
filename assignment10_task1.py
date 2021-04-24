import os
import random

file_name = "words.txt"

try:
    with open(file_name,"r") as file_stream:
        file_contents = file_stream.readlines()
except FileNotFoundError:
    print(f"The file {file_name} could not be found.")
    print(f"Please copy the file into the folder {os.getcwd()}")

random.shuffle(file_contents)

with open(file_name,"w") as file_stream:
    file_stream.writelines(file_contents)