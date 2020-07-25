# Crack the secret message hiding in hack_code directory

import os

# List all files in a directory using os.listdir
basepath = 'hack_code/'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        print(fileName)

# Create a new directory for the deciphered code
dir = os.path.join("hack_code_done")
if not os.path.exists(dir):
    os.mkdir(dir)