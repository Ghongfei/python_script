import os
import cv2

videos_src_path = r'E:\Crawling\baidu\out_shot\外拍视频\1121_火灾持械跌倒'
videos_save_path = r'E:\Crawling\baidu\out_shot\1'
videos = os.listdir(videos_src_path)

for each_video in videos:
    print('Video Name:', each_video)
    each_video_name, _ = each_video.split('.')
    os.mkdir(videos_save_path + '\\' + each_video_name)
    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '\\'
    each_video_full_path = os.path.join(videos_src_path, each_video)
    cap = cv2.VideoCapture(each_video_full_path)
    frame_count = 1
    success = True

    while (success):
        if cap.isOpened():
            success, frame = cap.read()
        else:
            success = False
        # if success == True:
        if(frame_count % 10 == 0):
            try:
                cv2.imwrite(each_video_save_full_path + "\\" + each_video_name + "_armed_fall_fire_" + "%06d.jpg" % frame_count, frame)
            except:
                print('error')
        frame_count = frame_count + 1

    cap.release()
    print('Final frame:', frame_count)