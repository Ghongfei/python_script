import os
import shutil

path_txt = r"E:\hongfei\Smoke\datatset\dataset2\test_labels"
filelist = os.listdir(path_txt)
path1 = r"E:\hongfei\Smoke\datatset\dataset2\test_bad_img_2"
filelist2 = os.listdir(path1)
path2 = r"E:\hongfei\Smoke\datatset\dataset2\test_bad_img_2"

for files in filelist:
    filename0 = os.path.splitext(files)[0]
    for files2 in filelist2:
        filename2 = os.path.splitext(files2)[0]
        print(filename2)
        if filename0 == filename2:
            full_path = os.path.join(path_txt, files)
            shutil.move(full_path, path2)
        else:
            continue