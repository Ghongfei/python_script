import cv2

cap = cv2.VideoCapture('C:\\Users\\Administrator\\Desktop\\V00409-091522.mp4')
if not cap.isOpened():
    print('video is not opened')
else:
    num = 0
    name = 2
    fps = cap.get(cv2.CAP_PROP_FPS)  
    framecount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    videoWriter = cv2.VideoWriter('C://Users//Administrator//Desktop//resultVideo1_'+str(name)+'.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,frameSize=(1920,1080))
            
    while(1):
        success,frame = cap.read()
        if success:
            num += 1
            videoWriter.write(frame)
            if (num % 750 == 0):
                videoWriter.release()
                name += 1
                videoWriter = cv2.VideoWriter('C://Users//Administrator//Desktop//resultVideo1_'+str(name)+'.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,frameSize=(1920,1080))
                print('ok')
        else:
            print('end')
            break
    cap.release()