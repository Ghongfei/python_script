import os
import shutil
name = 0
for i in os.listdir('E:/hatdata1/labels/train'):
    size = os.path.getsize('E:/hatdata1/labels/train/' + i)
    if size == 0:
        name += 1
for i in os.listdir('E:/hatdata1/labels/val'):
    size = os.path.getsize('E:/hatdata1/labels/val/' + i)
    if size == 0:
        name += 1

print(name)
