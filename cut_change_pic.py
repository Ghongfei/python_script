# import cv2
# import numpy as np
#
# img = cv2.imread(r'E:\Crawling\baidu\green_video_test\VID_20201110_152747_armed_000330.jpg')
# img_back = cv2.imread(r'E:\Crawling\baidu\green_video_test\1604996726_output_armed_000010.jpg')
#
# # 日常缩放
# # rows, cols, channels = img_back.shape
# # img_back = cv2.resize(img_back, None, fx=0.7, fy=0.7)
# # cv2.imshow('img_back', img_back)
#
# rows, cols, channels = img.shape
# img = cv2.resize(img, None, fx=0.4, fy=0.4)
# rows, cols, channels = img.shape  # rows，cols最后一定要是前景图片的，后面遍历图片需要用到
#
# # 转换hsv
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# # 获取mask
# lower_blue = np.array([36, 43, 46])
# upper_blue = np.array([80, 255, 255])
# mask = cv2.inRange(hsv, lower_blue, upper_blue)
# cv2.imshow('Mask', mask)
#
# # 腐蚀膨胀
# erode = cv2.erode(mask, None, iterations=1)
# # cv2.imshow('erode', erode)
# dilate = cv2.dilate(erode, None, iterations=1)
# # cv2.imshow('dilate', dilate)
#
# # 遍历替换
# center = [50, 50]  # 在新背景图片中的位置
# for i in range(rows):
#     for j in range(cols):
#         if dilate[i, j] == 0:  # 0代表黑色的点
#             img_back[center[0] + i, center[1] + j] = img[i, j]  # 此处替换颜色，为BGR通道
#
#
# cv2.imshow('res', img_back)
# cv2.waitKey(0)
# cv2.destroyAllWindows()








# import cv2
# from PIL import Image
# import numpy as np
#
# yuantu = r"E:\Crawling\baidu\green_video_test\VID_20201110_152747_armed_000700.jpg"
# masktu = r"E:\Crawling\baidu\green_video_test\1604996726_output_armed_000010.jpg"
#
# #使用opencv叠加图片
# img1 = cv2.imread(yuantu)
# img2 = cv2.imread(masktu)
#
# alpha = 0.1
# meta = 1 - alpha
# gamma = 0
# # cv2.imshow('img1', img1)
# # cv2.imshow('img2', img2)
# # image = cv2.addWeighted(img1,alpha,img2,meta,gamma)
# image = cv2.add(img1, img2)
#
# cv2.imshow('image', image)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cv2.imwrite(r"E:\Crawling\baidu\green_video_test\mask.png",image)





# import os, paddlehub as hub
# humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')# 加载模型
# path = 'E:/python_script/1/'# 文件目录
# files = [path + i for i in os.listdir(path)]# 获取文件列表
# results = humanseg.segmentation(data={'image':files})# 抠图


# 待预测图片
test_img_path = ["E:/python_script/1/4.jpg"]

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(test_img_path[0])

# 展示待预测图片
plt.figure(figsize=(10, 10))
plt.imshow(img)
plt.axis('off')
plt.show()

import paddlehub as hub

module = hub.Module(name="deeplabv3p_xception65_humanseg")
input_dict = {"image": test_img_path}

results = module.segmentation(data=input_dict)
for result in results:
    print(result)

# 预测结果展示
# test_img_path = "E:/python_script/humanseg_output/4.png"
# img = mpimg.imread(test_img_path)
# plt.figure(figsize=(10, 10))
# plt.imshow(img)
# plt.axis('off')
# plt.show()