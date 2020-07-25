import os

# List all files in a directory using os.listdir
basepath = 'hack_code/'
for fileName in os.listdir(basepath):
    if os.path.isfile(os.path.join(basepath, fileName)):
        print(fileName)
