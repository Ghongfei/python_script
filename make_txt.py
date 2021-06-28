import os

path = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\folder25\JPEGImages"
file_list = os.listdir(path)

for file in file_list:
    old_path = os.path.join(path, file)

    filename = os.path.splitext(file)[0]
    file_type = os.path.splitext(file)[1]
    new_path = r"E:\HONGFEI\arms\knife_fire_fall_face_smoke_person_pic\folder25\labels"
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    txt_name = filename + '.txt'
    new_path_txt = os.path.join(new_path, txt_name)
    print(new_path_txt)
    with open(new_path_txt, 'w') as f:
        f.write('')
        f.close()
