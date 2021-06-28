from PIL import Image
import os, glob


def batch_image(in_dir, out_dir):
    if not os.path.exists(out_dir):
        print(out_dir, 'is not existed.')
        os.mkdir(out_dir)

    if not os.path.exists(in_dir):
        print(in_dir, 'is not existed.')
        return -1
    count = 0
    for files in glob.glob(in_dir + '/*'):
        filepath, filename = os.path.split(files)

        out_file = filename[0:8] + '.jpg'
        # print(filepath,',',filename, ',', out_file)
        im = Image.open(files)
        new_path = os.path.join(out_dir, out_file)
        print(count, ',', new_path)
        count = count + 1
        im.save(os.path.join(out_dir, out_file))


if __name__ == '__main__':
    batch_image(r'D:\数据集\USC行人数据集', r'D:\数据集')