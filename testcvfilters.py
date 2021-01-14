import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time

from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser(description='Predict')
    parser.add_argument(
        '-dataroot', '--dataroot',
        type=str, default='./testImg',
        help='root of the image'
    )
    parser.add_argument(
        '-datatype', '--datatype',
        type=str, default=['jpg','tif','png'],
        help='type of the image'
    )
    parser.add_argument(
        '-predictpath', '--predictpath',
        type=str, default='./predictImg',
        help='root of the output'
    )
    return  parser.parse_args()

if __name__== '__main__':

    args = parse_args()

    selectNames = []

    data=[]
    print('Read img from:' , args.dataroot)
    fnames=os.listdir(args.dataroot)
    print('Len of the file:',len(fnames))

    if not os.path.exists(args.predictpath):
        os.mkdir(args.predictpath)

    for f in fnames:
        if f.split('.')[-1] in args.datatype:
            tmp=cv2.imread(args.dataroot+'/'+f)

            selectNames.append(f)
            if tmp.shape[1]<tmp.shape[0]:
                tmp=np.rot90(tmp)
            if tmp.shape[0]!=480 or tmp.shape[1]!=640:
                tmp=cv2.resize(tmp, (640, 480), interpolation=cv2.INTER_CUBIC)
            tmp=cv2.blur(tmp,(2,2))
            kernel = np.ones((5,5),np.uint8)

            tmp_gray = cv2.cvtColor(tmp, cv2.COLOR_BGR2GRAY)
            th, tmp_bin = cv2.threshold(tmp_gray, 127, 255, cv2.THRESH_OTSU)

            cv2.imwrite(args.predictpath+'/'+os.path.splitext(f)[0]+'bin.jpg', tmp_bin)
            tmp_canny=cv2.Canny(tmp_bin,100,200)
            tmp_canny = cv2.cvtColor(tmp_canny, cv2.COLOR_GRAY2RGB)
            tmp_res = cv2.add(tmp,tmp_canny)
            cv2.imwrite(args.predictpath+'/'+os.path.splitext(f)[0]+'.jpg', tmp_res)
