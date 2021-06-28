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


from removebg import RemoveBg
from PIL import Image
import os


# changebg: 调用PIL添加背景颜色
def changebg(img, color):
    color_dict = {"A": (255, 0, 0), "B": (67, 142, 219), "C": (255, 255, 255)}  # A:red B:bule C:white D:justremovebg
    im = Image.open(img)
    x, y = im.size
    try:
        p = Image.new('RGBA', im.size, color=color_dict.get(color))
        p.paste(im, (0, 0, x, y), im)
        p.save('{}.png'.format('new' + color))
    except:
        print('changebg err')
        pass


rmbg = RemoveBg("UiwiP9dQj53v693md9UyEyZz", "error.log")

# 获取单个照片的抠图   XKMh1J7geGfnGY9CFu9zXV8f

rmbg.remove_background_from_img_file("./1.png")  # 图片地址
option = 'B'  # 蓝色
changebg('1.png_no_bg.png', option)

# 批量获取抠图信息
# path = '%s/picture' % os.getcwd()
# for pic in os.listdir(path):
#   rmbg.remove_background_from_img_file("%s/%s" % (path, pic))
