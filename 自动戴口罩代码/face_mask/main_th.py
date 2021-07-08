import mask as mk
import cv2 as cv
import os
from multiprocessing.pool import ThreadPool
# import multiprocessing

pathf = "/home/ai/jiayou/work/face_dataset/"
pathm = "/home/ai/jiayou/work/mask_dataset/"
max_th_pool = 10
pool = ThreadPool(processes=max_th_pool)

# pool = multiprocessing.Pool(processes=3)


def pro_th(path):
    facepath = path[0]
    faceimg = path[1]
    face = cv.imread(pathf+facepath+"/"+faceimg)
    try:
        face.shape
    except:
        print('fail to read face image')
        return "fail"
    maskface = mk.automask(face)
    try:
        maskface.shape
    except:
        return "fail"
    cv.imwrite(pathm+facepath+"/"+faceimg, maskface)
    return "ok"


pic_list = []
num = 0
for facepath in os.listdir(pathf):
    for faceimg in os.listdir(pathf+facepath):

        if not os.path.exists(pathm + facepath):
            os.makedirs(pathm + facepath)

        # os.path.join()
        if os.path.exists(pathm+facepath+"/"+faceimg):
            print(pathm+facepath+"/"+faceimg)
            continue

        pic_list.append([facepath, faceimg])
        if num == (max_th_pool - 1):
            result_list = pool.map(pro_th, (pic_list[i] for i in range(len(pic_list))))
            print(result_list)
            pic_list.clear()
            num = 0
        num = num + 1





