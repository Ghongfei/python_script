import cv2 as cv
import math

def Srotate(angle,valuex,valuey,pointx,pointy, height):
    PI = 3.14159
    angle = -angle
    valuex = valuex
    valuey = height - valuey
    pointx = pointx
    pointy = height - pointy
    x = (valuex - pointx)*math.cos(PI / 180.0 * angle) - (valuey - pointy)*math.sin(PI / 180.0 * angle) + pointx
    y = (valuex - pointx)*math.sin(PI / 180.0 * angle) + (valuey - pointy)*math.cos(PI / 180.0 * angle) + pointy
    x = x
    y = height - y
    return x, y



src = cv.imread('E:/dlrb.jpg')
cx = 210
cy = 219
w = 399
h = 147
ro = 21

xmin = int(cx - w/2)
ymin = int(cy - h/2)
xmax = int(cx + w/2)
ymax = int(cy + h/2)
cv.rectangle(src, (xmin, ymin), (xmax, ymax), (255, 255, 0), thickness=1, lineType=8, shift=0)
print(src.shape)

x1, y1 = map(int, Srotate(ro, xmin, ymin, cx, cy, src.shape[0])) #左上
x2, y2 = map(int, Srotate(ro, xmax, ymax, cx, cy, src.shape[0])) #右下
x3, y3 = map(int, Srotate(ro, xmax, ymin, cx, cy, src.shape[0])) #右上
x4, y4 = map(int, Srotate(ro, xmin, ymax, cx, cy, src.shape[0])) #左下

cv.line(src, (x1, y1), (x3, y3), (255, 0, 0))
cv.line(src, (x3, y3), (x2, y2), (255, 0, 0))
cv.line(src, (x2, y2), (x4, y4), (255, 0, 0))
cv.line(src, (x4, y4), (x1, y1), (255, 0, 0))

cv.imshow('src', src)
cv.waitKey(0)
cv.destroyAllWindows()
