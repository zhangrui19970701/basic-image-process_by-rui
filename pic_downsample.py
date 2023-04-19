import os
import glob
import cv2
from skimage import io
#图片所在文件夹地址
Image_dir = '/home/rui/basic-image-process_by-rui/my_data/JPEGImages/*/'
#	*.jpg为图片格式后缀
Image_glob=os.path.join(Image_dir,'*.jpg')
Image_name_list=[]
Image_name_list.extend(glob.glob(Image_glob))
print(len(Image_name_list))

for Image_i in Image_name_list:
    print(Image_i)
    img = cv2.imread(Image_i,-1)
    #pyrDown只能降低尺寸的一半，若需要1/4，则降低两次
    #img = cv2.pyrDown(img)
    img_down = cv2.pyrDown(img)
    io.imsave(Image_i,img_down)

