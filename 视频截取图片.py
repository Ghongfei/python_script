import cv2
import os

name = 1
url = r"E:\baidu\外拍视频"
path = r"E:\baidu\jpg"

if not os.path.exists(path):
    os.makedirs(path)

for filename in os.listdir(url):

    videopath = url + "\\" + filename
    cap = cv2.VideoCapture(videopath)
    if cap.isOpened():
        rel, frame = cap.read()
    else:
        rel = False
    time = 10
    c = 1

    while rel:

        rel, frame = cap.read()
        if (c % time == 0):
            try:
                cv2.imwrite(path + "\\" + "armed_" + str(name) + '.jpg', frame)
            except:
                print("error")
            # cv2.imwrite('E:/aa.jpg', frame)
            name += 1

        c = c + 1

    cap.release()
    print(videopath + ' ok')
