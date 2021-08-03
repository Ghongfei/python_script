import os
import cv2

videos_src_path = r'/media/vtouch/项目/Crawling/baidu/out_shot/监控摄像头拍摄视频/20210620_0701'
videos_save_path = r'/media/vtouch/项目/Crawling/baidu/out_shot/1'
videos = os.listdir(videos_src_path)

for each_video in videos:
    print('Video Name:', each_video)
    each_video_name, _ = each_video.split('.')

    os.mkdir(videos_save_path + '/' + each_video_name)

    each_video_save_full_path = os.path.join(videos_save_path, each_video_name) + '/'
    each_video_full_path = os.path.join(videos_src_path, each_video)

    cap = cv2.VideoCapture(each_video_full_path)

    # 设置分辨率
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    frame_count = 1
    success = True

    while (success):
        if cap.isOpened():
            success, frame = cap.read()
        else:
            success = False

        # if success == True:
        if (frame_count % 50 == 0):
            try:
                cv2.imwrite(each_video_save_full_path + "/" + each_video_name + "_xinzao_yw04_" + "%06d.jpg" % frame_count, frame)
                # cv2.imwrite(
                #     each_video_save_full_path + "/" + each_video_name + "_gongsiwaipai_gd01_" + "%06d.jpg" % frame_count,
                #     frame)
            except:
                print('error')

        frame_count = frame_count + 1

    cap.release()
    print('Final frame:', frame_count)
