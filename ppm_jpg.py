from PIL import Image
import os

# path = "D:\数据集\MIT行人数据集\pedestrians128x64"
# save_path = "D:\数据集\MIT行人数据集"
# path_list = os.listdir(path)
# for path_name in path_list:
#     path_new = os.path.join(path, path_name)
#     img = Image.open(path_new)
#     img.save(r"D:\数据集\MIT行人数据集")
input_test_path = r"E:\pedestrians128x64"
output_test_path = r"E:\pedestrians128x64"


def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.mkdir(out_dir)

    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        return -1

    directories = [d for d in os.listdir(in_dir) if os.path.isdir(os.path.join(in_dir))]
    print(directories)
    for d in directories:
        # 每一类的路径
        label_directory = os.path.join(in_dir)
        new_directory = os.path.join(out_dir)
        # out_folder = os.path.exists(out_dir + d)
        # if not out_folder:
        #     os.mkdir(new_directory)
        file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f.endswith(".ppm")]
        # file_names is every photo which is end with ".ppm"
        print(file_names)
        count = 0
        for files in file_names:
            file_path, extfilename = os.path.split(files)
            filename, extname = os.path.splitext(extfilename)
            out_file = filename + '.jpg'
            im = Image.open(files)
            new_path = os.path.join(new_directory, out_file)
            print(count, ',', new_path)
            count = count + 1
            im.save(new_path)


if __name__ == '__main__':
    batch_image(input_test_path, output_test_path)