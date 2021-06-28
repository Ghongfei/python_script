# import os
# import shutil
#
# path_txt = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\face_wider\Annotations_combine"
# filelist = os.listdir(path_txt)
# path1 = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\face_wider\badjpg"
# filelist2 = os.listdir(path1)
# path2 = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\face_wider\badcombine"
#
# for files in filelist:
#     filename0 = os.path.splitext(files)[0]
#     for files2 in filelist2:
#         filename2 = os.path.splitext(files2)[0]
#         print(filename2)
#         if filename0 == filename2:
#             full_path = os.path.join(path_txt, files)
#             shutil.move(full_path, path2)
#         else:
#             continue



import os
import shutil

path_txt = r"/media/vtouch/项目/Crawling/baidu/out_shot/1"
filelist = os.listdir(path_txt)
path2 = r"/media/vtouch/项目/Crawling/baidu/out_shot/2"

count = 1
for files in filelist:

    full_path = os.path.join(path_txt, files)
    full_path_list = os.listdir(full_path)
    for files2 in full_path_list:
        full_path_2 = os.path.join(full_path, files2)
        shutil.move(full_path_2, path2)
        print('已转移 %d 张！！！' % count)
        count += 1