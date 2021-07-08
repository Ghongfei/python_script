import cv2
import os

name = 11517
url = "E:/抽烟/video/"
path = "E:\\videoimg\\"
if not os.path.exists(path):
    os.makedirs(path)
for filename in os.listdir(url):

    videopath = url + filename

    cap = cv2.VideoCapture(videopath)

    if cap.isOpened():
        rel, frame = cap.read()
    else:
        rel = False
    time = 15
    c = 1
    while rel:

        rel, frame = cap.read()
        if c % time == 0:
            cv2.imwrite('E:/videoimg/p_smoke9' + str(name) + '.jpg', frame)
            cv2.imwrite('E:/aa.jpg', frame)
            print(path + 'p_smoke9'+str(name) + '.jpg')
            name += 1

        c = c + 1

    cap.release()
    print(videopath + ' ok')
