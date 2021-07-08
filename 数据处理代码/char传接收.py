from ctypes import *

ll = cdll.LoadLibrary('D:/pycvtest2/x64/Debug/pycvtest2.dll')

# 传char *
path = bytes("D:/pig1/pig_50000.jpg","gbk")
#path = create_string_buffer('D:/pig1/pig_50000.jpg'.encode('gbk'), 21)

#接收char *

pathres = ll.showimg(path)

result = string_at(pathres)

print(result.decode("gbk"))



'''
#include "pch.h"
#include "framework.h"
#include "pycvtest2.h"

#include <iostream>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui_c.h>

using namespace std;
using namespace cv;

extern "C"
{

	_declspec(dllexport)char * showimg(char* path);
	char * showimg(char* path)
	{
		Mat src = imread(path);
		if (src.empty()) {
			cout << "could not read image..." << endl;
		}
		line(src, Point(10, 10), Point(100, 100), Scalar(255, 0, 0), 5, LINE_8);
		imshow("image show", src);
		waitKey(0);
		return path;
	}
}
'''