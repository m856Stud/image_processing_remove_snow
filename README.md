# Image Processing Course: Remove Snow On Image


# Setup and environment

To generate the recovered result you need:

1. Python 3 
2. tensorflow 1.6.0
3. keras 2.2.0
4. cv2

Download pre-traned model to use current algorithm. It can be found at:
https://drive.google.com/drive/folders/1xlH552gblaaD12ALmmN0h04t6ogDdHp9?usp=sharing
Then put it to the folder "modelParam".
To run
```
$ python3 ./predict.py -dataroot ./your_dataroot -datatype datatype -predictpath ./output_path -batch_size batchsize
```
Example:
```
$ python ./predict.py -dataroot ./testImg -predictpath ./output
$ python ./predict.py -dataroot ./testImg -datatype tif -predictpath ./output
```

*datatype default: tif, jpg ,png

# Run OpenCV test algorithm
To reproduce the result of bad quality of using only image processing algorithms 
```
$ python3 ./testcvfilters.py -dataroot ./your_dataroot -datatype datatype -predictpath ./output_path
```
Example:
```
$ python ./predict.py -dataroot ./testImg -predictpath ./outputFilterTest
```
