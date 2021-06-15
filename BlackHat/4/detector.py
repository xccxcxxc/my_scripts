# -*- coding: utf-8 -*-

"""与 recapper.py 配套使用，检查生成的图片是否包含人脸。如果包含，则增加一个相框"""
import cv2
import os
ROOT = '/home/kali/Desktop/pictures'
FACES = '/home/kali/Desktop/faces'
TRAIN = '/home/kali/Desktop/training'


def detect(srcdir=ROOT, tgtdir=FACES, train_dir=TRAIN):
    for fname in os.listdir(srcdir):
        # 检查结尾字符串，也可以为可选的元组
        if not fname.upper().endswith('.JPG'):
            continue
        fullname = os.path.join(srcdir, fname)
        newname = os.path.join(tgtdir, fname)
        img = cv2.imread(fullname)
        if img is None:
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        training = os.path.join(train_dir, 'haarcascade_frontalface_alt.xml')
        cascade = cv2.CascadeClassifier(training)
        rects = cascade.detectMultiScale(gray, 1.3, 5)
        try:
            # 可迭代对象任一不为空
            if rects.any():
                print('got a face')
                rects[:, 2:] += rects[:, :2]
        except AttributeError:
            print(f'No faces found in {fname}')
            continue
            # highlight the faces in the image
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)
        cv2.imwrite(newname, img)


if __name__ == '__main__':
    detect()
