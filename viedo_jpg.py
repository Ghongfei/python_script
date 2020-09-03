import os
import cv2

videos_src_path = r'E:\text_video'
videos_save_path = r'E:\text_video'
videos = os.listdir(videos_src_path)

for each_video in videos:
    print('Video Name:', each_video)
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '/' + each_video_name)
    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
    each_video_full_path = os.path.join(videos_src_path, each_video)
    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True
    while (success):
        success, frame = cap.read()
        # if success == True:
        if(frame_count%5 == 0):
            cv2.imwrite(each_video_save_full_path + "%06d.jpg" % frame_count, frame)
        frame_count = frame_count + 1
    print('Final frame:', frame_count)