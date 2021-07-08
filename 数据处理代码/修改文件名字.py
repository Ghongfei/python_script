import os
import re
import shutil

path = 'E:/安全帽/安全帽12/'
despath = 'E:/安全帽/'
name = 0
for file in os.listdir(path):
    print(file)
    fullpath = path + file
    output = despath + 'safety_cat12_' + str(name) + '.jpg'
    shutil.copy(fullpath, output)
    name += 1