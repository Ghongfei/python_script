import os

path = r"E:\hongfei\hat\bundle_archive\images"
file_list = os.listdir(path)
for file in file_list:
    old_path = os.path.join(path, file)  # 原来的文件路径
    filename = os.path.splitext(file)[0]  # 文件名
    newfilename = filename.replace('jpg', '')  # 字符替换
    file_type = os.path.splitext(file)[1]  # 文件扩展名
    new_path = os.path.join(path, newfilename + file_type)  # 新命名加入新路径
    print(new_path)
    os.rename(old_path, new_path)  # 重命名
