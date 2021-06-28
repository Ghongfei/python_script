import cv2
import os

fname = 6
name = 0
url = "E:/picc/picc"

for filename in os.listdir(url):
    path = 'E:/fire_img/image' + str(fname)
    isExists=os.path.exists(path)
    if not isExists:
        os.mkdir(path) 
    else:
        pass
    for filename1 in os.listdir(url + '/' + filename):
        videopath = url + '/' + filename + '/'+ filename1
        cap = cv2.VideoCapture(videopath)
        if cap.isOpened():
            rel, frame = cap.read()
        else:
            rel = False
        time = 10
        c = 1
        while rel:  
            rel, frame = cap.read() 
            if c % time == 0: 
                try:
                    isExists=os.path.exists('E:/fire_img/image' + str(fname) + '/' + str(name) + '.jpg')
                    if not isExists:
                        cv2.imwrite('E:/fire_img/image' + str(fname) + '/' + str(name) + '.jpg',frame) 
                    else:
                        pass
                except Exception:
                    pass
                name = name + 1
            c = c + 1   
            cv2.waitKey(1)
        cap.release()
    name = 0
    fname += 1



