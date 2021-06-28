import os
import cv2
from PIL import Image
# path = "E:\Train001"
# tif_list = [x for x in os.listdir(path) if x.endswith(".tif")] #找到当前路径下的所有.tif文件
# for num, i in enumerate(tif_list):
#     img = cv2.imread(i,-1)  #这里选择-1，不进行转化
#     cv2.imwrite(i.split('.')[0]+".jpg", img)
#     print('总共:',len(tif_list),'张，剩余:',len(tif_list)-num-1,'张')

path = "E:\Train001"
tif_list = [x for x in os.listdir(path) if x.endswith(".tif")] #找到当前路径下的所有.tif文件
for num in tif_list:
    img = Image.open(os.path.join(path, num))
    img.save(path + "\\" + num.split(".")[0] + '.jpg')