# Crack the secret message hiding in hack_code directory

import os
import shutil

secretMessageDirectory = 'hack_code'
crackedMessageDirectory = 'hack_code_done'

try:
    assert os.path.isdir(secretMessageDirectory), "Secret message directory does not exist."
except AssertionError as object:
    print(object)
    exit()

try:
    assert not os.path.isdir(crackedMessageDirectory), "Outdated directory deleted."
except AssertionError as object:
    print(object)
    shutil.rmtree(crackedMessageDirectory)

# Copy the directory for deciphering the code
shutil.copytree(secretMessageDirectory, crackedMessageDirectory)

# List all files in a directory using os.listdir
basepath = 'hack_code/'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        print(fileName)
