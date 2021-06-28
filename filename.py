import os

path = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\folder26\label"
file_list = os.listdir(path)
count = 0
for file in file_list:
    old_path = os.path.join(path, file)  # 原来的文件路径
    filename = os.path.splitext(file)[0]  # 文件名
    file_type = os.path.splitext(file)[1]  # 文件扩展名
    # 用字符串函数zfill 以0补全所需位数
    new_path = os.path.join(path, 'waipai_motuoc_2_' + str(count).zfill(4) + file_type)
    # new_path = os.path.join(path, 'fall_c5_' + str(count).zfill(4) + file_type)
    # filename = filename.replace("knife","hammer")
    # new_path = os.path.join(path, filename + file_type)

    # new_path = os.path.join(path, 'old_' + filename + file_type)
    print(new_path)
    os.rename(old_path, new_path)  # 重命名
    count += 1
