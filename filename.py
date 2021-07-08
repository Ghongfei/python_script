import os

path = r"/media/vtouch/项目/Crawling/baidu/out_shot/监控摄像头拍摄视频/2021-06-19"
file_list = os.listdir(path)
count = 0
for file in file_list:
    old_path = os.path.join(path, file)  # 原来的文件路径
    filename = os.path.splitext(file)[0]  # 文件名
    file_type = os.path.splitext(file)[1]  # 文件扩展名
    # 用字符串函数zfill 以0补全所需位数
    new_path = os.path.join(path, 'xzwaipai_motor_1_' + str(count).zfill(4) + file_type)
    # new_path = os.path.join(path, 'fall_c5_' + str(count).zfill(4) + file_type)
    # filename = filename.replace("knife","hammer")
    # new_path = os.path.join(path, filename + file_type)

    # new_path = os.path.join(path, 'old_' + filename + file_type)
    print(new_path)
    os.rename(old_path, new_path)  # 重命名
    count += 1
