import mask as mk
import cv2 as cv
import os
import multiprocessing
import shutil
pathf = "/home/ai/jiayou/work/face_dataset/"
pathm = "/home/ai/jiayou/work/mask_dataset/"
fail_dir = "/home/ai/jiayou/work/fail_mask_dataset/"

if not os.path.exists(fail_dir):
    os.makedirs(fail_dir)


def proth(path):
    facepath = path[0]
    faceimg = path[1]
    pic_path = pathf+facepath+"/"+faceimg
    fail_save_path =  fail_dir+facepath+"/"+faceimg
    face = cv.imread(pic_path)
    try:
        face.shape
    except:
        shutil.move(pic_path, fail_save_path)
        print("fail ", pic_path)
        return "fail"
    maskface = mk.automask(face)
    try:
        maskface.shape
    except:
        shutil.move(pic_path, fail_save_path)
        print("fail ", pic_path)
        return "fail"

    cv.imwrite(pathm+facepath+"/"+faceimg, maskface)
    print("ok", pic_path)
    return "ok"


if __name__ == "__main__":
    po = multiprocessing.Pool(51)
    pic_list = []
    num = 0
    for facepath in os.listdir(pathf):
        for faceimg in os.listdir(pathf+facepath):

            if os.path.exists(pathm+facepath+"/"+faceimg):
                continue
            if not os.path.exists(pathm + facepath):
                os.makedirs(pathm + facepath)
            if not os.path.exists(fail_dir + facepath):
                os.makedirs(fail_dir + facepath)

            pic_list.append([facepath, faceimg])
            if num == 50:
                for i in range(len(pic_list)):
                    po.apply_async(proth, (pic_list[i],))
                pic_list.clear()
                num = 0
            num = num + 1
    po.close()
    po.join()




