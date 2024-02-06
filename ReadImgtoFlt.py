from PIL import Image
import numpy as np

def imgConv(img_path):

	img = Image.open(img_path)
	img_rs = img.resize((128,128))
	img_gr = img_rs.convert('L')
	img_arr = np.array(img_gr)
	img_gr.show()
	img_1d = img_arr.flatten()

	return img_1d



test_img = 'D:/TMO/DTCE-Dummy results only/data/Test-2/33.png'
txt_filloc = 'C:/Users/WA2/Desktop/temp.txt' 
arr = imgConv(test_img)
np.savetxt(txt_filloc,arr,fmt='%.6f')


