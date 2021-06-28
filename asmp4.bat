ffmpeg  -i 1605603980_output.flv 1605603980_output.mp4
ffmpeg -i 2.mp4 -codec copy -bsf:v h264_mp4toannexb 2.ts
 