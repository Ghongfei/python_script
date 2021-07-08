import cv2
import os

def RotateClockWise90(img):
    trans_img = cv2.transpose(img)
    new_img = cv2.flip(trans_img, 1)
    return new_img

if __name__=="__main__":
    for i in range(0,35):
        path1 = 'E:/B2/Pig_' + str(i)
        for filename1 in os.listdir(path1):
            filenamee = path1 + "/" + filename1
            print(filenamee)
            img = cv2.imread(filenamee)
            clock90_img = RotateClockWise90(img)
            cv2.imwrite(filenamee,clock90_img) 
            
