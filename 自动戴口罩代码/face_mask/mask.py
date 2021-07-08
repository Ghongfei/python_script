import cv2 as cv
import dlib
import numpy as np
import random
import math


def mapping(mappic, roi):

    imggray = cv.cvtColor(mappic, cv.COLOR_BGR2GRAY)
    ret1, mask1 = cv.threshold(imggray, 250, 255, cv.THRESH_BINARY)
    mask_inv1 = cv.bitwise_not(mask1)
    img1_bg1 = cv.bitwise_and(roi, roi, mask=mask1)
    img2_fg1 = cv.bitwise_and(mappic, mappic, mask=mask_inv1)
    dst1 = cv.add(img1_bg1, img2_fg1)
    return dst1


def picturemix(img1, img2, maxminpos, dotsfocus):
    img1row, img1col, img1channel = img1.shape

    # 脸部所在区域
    pxmax = maxminpos[0]
    pxmin = maxminpos[2]
    pymax = maxminpos[1]
    pymin = maxminpos[3]

    if pxmin < 0:
        pxmin = 0
    if pymin < 0:
        pymin = 0
    if pymax > img1.shape[0]:
        pymax = img1.shape[0]
    if pxmax > img1.shape[1]:
        pxmax = img1.shape[1]

    img2 = cv.resize(img2, (pxmax-pxmin,pymax-pymin))

    # 口罩分成左右两半
    img2left = img2[0:pymax-pymin, 0:int((pxmax-pxmin)/2)]
    img2right = img2[0:pymax-pymin, int((pxmax-pxmin)/2):pxmax-pxmin]

    # 黑色背景
    whitebgleft = np.zeros(img1.shape, np.uint8)
    whitebgright = np.zeros(img1.shape, np.uint8)

    # 口罩贴到黑色背景上
    # 左
    whitebgleft[pymin:pymax, pxmin:int((pxmax-pxmin)/2+pxmin)] = img2left
    # 右
    whitebgright[pymin:pymax, int((pxmax - pxmin) / 2 + pxmin):pxmax] = img2right

    # 仿射变换
    # 左
    pts1 = np.float32([[pxmin-5, (pymax-pymin)/2 + pymin], [(pxmax-pxmin)/2 + pxmin, pymin], [(pxmax-pxmin)/2 + pxmin, pymax]])
    pts2 = np.float32([[dotsfocus[1][0], dotsfocus[1][1]], [dotsfocus[5][0], dotsfocus[5][1]], [dotsfocus[2][0], dotsfocus[2][1]]])
    M = cv.getAffineTransform(pts1, pts2)
    rotatedstleft = cv.warpAffine(whitebgleft, M, (img1col, img1row))
    # 右
    pts1 = np.float32([[pxmax+5, (pymax - pymin) / 2 + pymin], [(pxmax - pxmin) / 2 + pxmin, pymin], [(pxmax - pxmin) / 2 + pxmin, pymax]])
    pts2 = np.float32([[dotsfocus[3][0], dotsfocus[3][1]], [dotsfocus[5][0], dotsfocus[5][1]], [dotsfocus[2][0], dotsfocus[2][1]]])
    M = cv.getAffineTransform(pts1, pts2)
    rotatedstright = cv.warpAffine(whitebgright, M, (img1col, img1row))

    rotatedst = cv.bitwise_or(rotatedstleft, rotatedstright) + 255

    # # 中值模糊
    rotatedst = cv.medianBlur(rotatedst, 5)

    roi = img1[0:img1row, 0:img1col]
    dst = mapping(rotatedst, roi)
    img1[0:img1row, 0:img1col] = dst

    return img1


def maxmindot(nparr):
    max = np.argmax(nparr, axis=0)
    min = np.argmin(nparr, axis=0)
    xmax = max[0][0]
    ymax = max[0][1]
    xmin = min[0][0]
    ymin = min[0][1]
    return xmax, ymax, xmin, ymin


def getrotate(dotsfocus):
    dot2 = dotsfocus[2]
    dot5 = dotsfocus[5]
    if dot5[0]-dot2[0] == 0:
        return 0
    angle = math.atan((dot5[1] - dot2[1])/(dot5[0]-dot2[0]))*180/math.pi
    return angle

def getlinelen(dota, dotb):
    xa = dota[0]
    ya = dota[1]
    xb = dotb[0]
    yb = dotb[1]
    if xa < 0:
        xa = 0
    if ya < 0:
        ya = 0
    if xb < 0:
        xb = 0
    if yb < 0:
        yb = 0

    len = math.sqrt(math.pow(abs(xa-xb), 2) + math.pow(abs(ya-yb), 2))
    return len

def comparelinelen(dotsfocus):
    d0 = dotsfocus[0]
    d5 = dotsfocus[5]
    d4 = dotsfocus[4]
    len1 = getlinelen(d0, d5)
    len2 = getlinelen(d4, d5)
    if len1 > len2:
        if len2/len1 < 0.4:
            return True
    elif len1 < len2:
        if len1/len2 < 0.4:
            return True
    else:
        return False

def changcolor(maskimg, mcolor):
    rows, cols, channels = maskimg.shape

    for i in range(rows):
        for j in range(cols):
            pv0 = maskimg[i, j, 0]
            pv1 = maskimg[i, j, 1]
            pv2 = maskimg[i, j, 2]

            if pv0 < 255 and pv1 < 255 and pv2 < 255:
                maskimg[i, j, 0] = mcolor[0]
                maskimg[i, j, 1] = mcolor[1]
                maskimg[i, j, 2] = mcolor[2]

    return maskimg

def rotateimg(src, ro):
    row, col ,c = src.shape
    rotatedst = np.zeros(src.shape)
    if ro > 0 and ro < 75:
        roangle = -(90-ro)
        M = cv.getRotationMatrix2D((col/2, row/2), roangle, 1.0)
        rotatedst = cv.warpAffine(src, M, (col, row))
    elif ro < 0 and ro > -75:
        roangle = 90+ro
        M = cv.getRotationMatrix2D((col / 2, row / 2), roangle, 1.0)
        rotatedst = cv.warpAffine(src, M, (col, row))

    return rotatedst

def automask(dst):
    faceimg = dst.copy()
    gray = cv.cvtColor(faceimg, cv.COLOR_BGR2GRAY)
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    dets = detector(gray, 1)

    dots = []
    dotsfocus = []
    for faced in dets:
        shape = predictor(faceimg, faced)
        for i, pt in enumerate(shape.parts()):
            pt_pos = (pt.x, pt.y)
            #cv.circle(faceimg, pt_pos, 8, (0, 255, 0), 10)
            if (2 <= i <= 14) or i == 28:
                dots.append(pt_pos)
            if i == 2 or i == 14 or i == 3 or i == 13 or i == 28 or i == 8:
                dotsfocus.append(pt_pos)


    dots = np.array(dots).reshape((-1, 1, 2))
    try:
        xmax, ymax, xmin, ymin = maxmindot(dots)
    except:
        return 0

    if comparelinelen(dotsfocus):
        return 0

    faceangle = getrotate(dotsfocus)
    if (faceangle > 0 and faceangle < 75) or (faceangle < 0 and faceangle > -75):
        faceimgrotate = rotateimg(faceimg, faceangle)
        faceimgrotatedst = automask(faceimgrotate)
        print(faceangle)
        return faceimgrotatedst


    xmax = dots[xmax][0][0]
    ymax = dots[ymax][0][1]
    xmin = dots[xmin][0][0]
    ymin = dots[ymin][0][1]

    # 口罩图片路径

    ran = random.randint(0, 7)
    maskpath = "data/mask/mask" + str(ran + 1) + ".png"
    mask = cv.imread(maskpath)
    try:
        mask.shape
    except:
        ran = random.randint(0, 7)
        maskpath = "data/mask/mask" + str(ran + 1) + ".png"
    mcolor = [243, 137, 187]

    r = random.randint(0, 8)
    if r > 6:
        r0 = random.randint(0, 7)
        if r0 == 0:
            maskpath = "data/mask/mask1.png"
        if r0 == 1:
            maskpath = "data/mask/mask2.png"
        if r0 == 2:
            maskpath = "data/mask/mask3.png"
        if r0 == 3:
            maskpath = "data/mask/mask4.png"
        if r0 == 4:
            maskpath = "data/mask/mask5.png"
        if r0 == 5:
            maskpath = "data/mask/mask6.png"
        if r0 == 6:
            maskpath = "data/mask/mask7.png"
        mask = cv.imread(maskpath)

    else:
        r1 = random.randint(0, 8)
        if r1 == 0:
            mcolor = [216, 121, 96]
        if r1 == 1:
            mcolor = [213, 75, 5]
        if r1 == 2:
            mcolor = [193, 112, 255]
        if r1 == 3:
            mcolor = [178, 241, 243]
        if r1 == 4:
            mcolor = [71, 145, 230]
        if r1 == 5:
            mcolor = [71, 145, 18]
        if r1 == 6:
            mcolor = [67, 79, 221]
        if r1 == 7:
            mcolor = [20, 215, 248]
        try:
            mask = changcolor(mask, mcolor)

        except:
            mask = cv.imread(maskpath)
    try:
        mask.shape
    except:
        print('fail to read mask image')
        return 0
    maskkouzao = picturemix(dst, mask, [xmax, ymax, xmin, ymin], dotsfocus)

    return maskkouzao

