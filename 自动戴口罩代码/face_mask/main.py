import mask as mk
import cv2 as cv
import os

pathf = "/home/ai/jiayou/work/face_dataset/"
pathm = "/home/ai/jiayou/work/mask_dataset/"
for facepath in os.listdir(pathf):

    for faceimg in os.listdir(pathf+facepath):

        face = cv.imread(pathf+facepath+"/"+faceimg)
        try:
            face.shape
        except:
            print('fail to read face image')
            continue
        maskface = mk.automask(face)
        try:
            maskface.shape
        except:
            continue
        if os.path.exists(pathm+facepath):
            cv.imwrite(pathm+facepath+"/"+faceimg, maskface)
            print(pathm+facepath+"/"+faceimg + " ok")
        else:
            os.makedirs(pathm+facepath)
            cv.imwrite(pathm+facepath+"/"+faceimg, maskface)
            print(pathm+facepath+"/"+faceimg + " ok")
