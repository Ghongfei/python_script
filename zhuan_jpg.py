from PIL import Image
import os


root = r'E:\division_video'
root_list = os.listdir(root)
for root_name in root_list:
    rootdir = os.path.join(root, root_name)
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            print('parentis :' + parent)
            print('filenameis :' + filename)
            currentPath = os.path.join(parent, filename)
            print('thefulll name of the file is :' + currentPath)
            im = Image.open(currentPath)
            out = im.transpose(Image.ROTATE_270)
            path = rootdir + "_1"
            if not os.path.exists(path):
                os.makedirs(path)
            newname = path + '\\' + filename
            out.save(newname)