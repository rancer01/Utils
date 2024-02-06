import numpy as np

txt_filloc = 'C:/Users/WA2/Desktop/temp.txt' 

txt_filloc1 = 'C:/Users/WA2/Desktop/temp2.txt' 
arr = np.loadtxt(txt_filloc)
k = []
print(len(arr))
for i in arr:
	hexarr = bin(np.float16(i).view('H'))[2:].zfill(16)
	print(hexarr)
	k.append(hex(int(hexarr,2))[2:])


np.savetxt(txt_filloc1,k,fmt='%s',newline = '_')
	