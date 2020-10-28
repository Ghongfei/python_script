import os

rootdir = os.path.join('/home/ai/hongfei/yolov4/dataset0908/')

write_path = open(r'E:\hongfei\dataset0908\train.txt', 'w')

path = r'E:\hongfei\dataset0908\train'
path_list = os.listdir(path)

for path_list_name in path_list:
    path_1 = os.path.join(path, path_list_name)
    path_1_list = os.listdir(path_1)
    for path_1_list_name in path_1_list:
        if path_1_list_name == "JPEGImages":
            path_2 = os.path.join(path_1, path_1_list_name)
            path_2_list = os.listdir(path_2)
            for path_2_list_name in path_2_list:
                write_path.write(rootdir + 'train' + '/' + path_list_name + '/' + path_1_list_name + '/' + path_2_list_name + '\n')

write_path.close()

print('ok')

