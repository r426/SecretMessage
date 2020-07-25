# Crack the secret message hiding in hack_code directory

import os
import shutil

# Copy the directory for deciphering the code
shutil.copytree('hack_code', 'hack_code_done')

# List all files in a directory using os.listdir
basepath = 'hack_code/'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        print(fileName)
