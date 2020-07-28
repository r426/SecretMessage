# Crack the secret message hiding in hack_code directory

import re
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
    assert not os.path.isdir(crackedMessageDirectory), ""
except:
    shutil.rmtree(crackedMessageDirectory)

# Copy the directory for deciphering the secret message
shutil.copytree(secretMessageDirectory, crackedMessageDirectory)

# Rename files in the crackedMessageDirectory directory
basepath = crackedMessageDirectory + '//'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        newName = re.sub(r'\d+', '', fileName)
        os.rename(basepath + fileName, basepath + newName)
