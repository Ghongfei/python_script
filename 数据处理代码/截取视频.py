import cv2
import os
videoname = '48.mp4'
path = 'E:/打架视频4/' + videoname
name = 294
starttime = 76
endtime  = 83

num = 0
cap = cv2.VideoCapture(path)
if not cap.isOpened():
    print('video is not opened')
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(3)), int(cap.get(4)))
framesum = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(framesum)
videoWriter = cv2.VideoWriter('E:/打架视频_cut/'+str(name)+'.mp4',
                              cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, frameSize=size)
videoWriter1 = cv2.VideoWriter('E:/无打架片段/' + videoname, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, frameSize=size)
while True:
    success, frame = cap.read()

    if success:
        num += 1
        if (num >= int(starttime * fps) and num < int(endtime * fps))\
                or (num >= int(103 * fps) and num < int(142 * fps))\
                or (num >= int(164 * fps) and num < int(167 * fps)):

            videoWriter.write(frame)
            print(num)
    #     else:
    #         videoWriter1.write(frame)
    # if num == framesum - 1:
    #     break
    if num == int(479 * fps):
        break
print('ok')
cap.release()




