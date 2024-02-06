#Code to convert an array to an image
#install Pillow and Numpy to run this

from PIL import Image
import numpy as np

def back2ImgConv(arr,shape):

	img_arr = arr.reshape(shape)
	img_gr = Image.fromarray(img_arr.astype('uint8'),'L')
	img_gr.show()

back2ImgConv()
