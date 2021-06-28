import os, sys

path = str(sys.argv[1])
files = os.listdir(path)
with open(path + '/train.txt', mode='w') as f:
    for i in files:
        f.write(path + '/' + i + '\n')
