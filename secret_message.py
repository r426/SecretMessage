# Crack the secret message hiding in hack_code directory

import os
import shutil

# Create a new directory for the deciphered code
# dir = os.path.join('hack_code_done')
# if not os.path.exists(dir):
#     os.mkdir(dir)

# Copy the directory for deciphering the code
shutil.copytree('hack_code', 'hack_code_done')

# List all files in a directory using os.listdir
basepath = 'hack_code/'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        print(fileName)

# Create a new directory for the deciphered code
dir = os.path.join("hack_code_done")
if not os.path.exists(dir):
    os.mkdir(dir)