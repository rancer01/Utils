#16 bit floating to val
import numpy as np
from PIL import Image
def FloatNormConv(hexa):
	inBin = bin(int(hexa,16,))[2:].zfill(16)

	Sign = int(inBin[0])
	Exp = int(inBin[1:6],2)
	Frac = int(inBin[6:],2)

	valSign = -2*(Sign-1/2)
	valExp = 2**(Exp - 15)
	valFrac = Frac/(1024)

	valDeci = valSign*valExp*(valFrac+1)
	return valDeci

def FltStrNrmConv(hex_string):
	hexvals = [hex_string[i:i+4] for i in range(0,len(hex_string),4)]
	decival = []
	for val in hexvals :
		decival.append(FloatNormConv(val))
	return decival

temp = FltStrNrmConv("571657c35898592658ef579c5507537e53a2552e577c5876581b56985624570757f8573e554c5409537a541b54cb5589564656e456ec566d56b7583b58de58ec592759555913581e55ae53d452f254ae571658555807566855955630576b56b25460529252e8540c54cc5595569357805774568a56345768597759735974596c5933589957985655558b55cf5756584457f55656555b5608577f569e540a520c529e53dc54dd55ec5714580b5826579c56a456a4598e5988597e596a593e590658fb591058f258bc58b958ae5829567e552955ca5773569754005208529253bc54d355f8571f580a5845582d57315608595e596a59815989597f599a5a015a645a875a755a3a59d859365859570256c757b3569a541952aa540b54bf550355675661577558175834575c558558b05916599259c359d05a165a895ad05af25b0f5b0e5ae85a9a5a1c596558e358945701544653a05553565b559654ba556756ac57b65822577855a2586058fe5975596a5944597859e25a235a5d5aa95adf5b005b115b045ac15a5f59b6584d557b549155d956e055d1546554d1560c571f57e3577b561e58bb58ee58d758725818581d585e588958d3595459bd5a035a3e5a6e5a875a815a365960583a56fb56cf56e855d654585467557a56ae57b657af56c2589a5883584857ec57635727571356ed57435822589658e0591859445971599859af59a2594d58cc584d57c15652548353fc54d0564d57df582b57a05810581b581a580f57db573a569f5683571258065869589f58b958c658cc58c358e0590358cc5866581a57c656c8556154cc550055ec57a2584457fa56bb57135750578f57a95718565a56645743582f5878585258175811580b5817586f586757755668563f56755691567c5666560f55fb570857d3575b553655f756a857275790579b5716569456db57e65811568354f054c25514568a5859581955f3550354e754db555455f5562c5640564f56a556f2568154ad55d45790586a5891588a585657e55793580d57b8553051ee513451de551a581b577c548f5336533e530c53de546554a35599569556be569b563554b555c6582f595c599559795961591358bf5899580a553a51ac50e4516c54a957a556c853345152523a532054305458544e5592571e574756aa562f54c0559d583259a45a0b5a165a2759cd593a58d0582555785218514651ea54c5577b56925382526653ac54ac55c355d95554565457b85760564055bc54a95575582a59b85a2e5a485a6859fe594658d0583455e553585226525454dc577c56e554eb54c0551155be56e5571e569e572157c156e855fd55dc548b553357de596d59e75a025a2c59de593e58d458455649545b5388534054ee575d575d56225610562b566b570b5775576f5780579a57375714573954315494563d581f589358bd58e758d958ab588c581b56785551552454ba550956be575f56c0569b56da56f257365800584d584a582a580157c65785535253e454cd55cf566f56bc56d4571257a857da57475689567e56b8564e5633572457be5753574057db5810584358ce594c596358ec581156d1563552ee53a05486552f5570556f557d5640572356f4569f56e7577b57fc582b587658b5589258345836587e58a858f5595659b759f8597358245617552a534253aa543a54aa54d354d8554f569857aa57795723578a582d589b58f3593b5959590c589b588658aa58df5925595159a25a0459b1589356bc54f755ff55c0552154ac54c255275597568f57f5582b57945747581a58a558b558b258f258f75898585d588458d45908593959aa5a1059da58fe578354f958f05895574055665522559a557c55f057525791567256065726582858225819588858e458b9585658345847586658bf595d59da59cb5908577754b759a85957582e55f3556a55ac559e561556c3567055795547562c5718575e57bc586458e858f0587b580957d7581758865918599559a5590b57b654e859365928584a568355e455e1566b5733572d56ce566b560155df560656555721583e58c558d35864580c585258cd591a59465954592858b657c2554c58ca58ef587a578556ba564b56fa57cc576b570e56f7567155c2556e5593566a57d9588658bb5866581b5899593a5959592b58c5583a57aa571455c758b058a6584257c9575156e2577457e4573356b7566955ba551954e55571569757b7586258bc5882584058a35915591d58ea5889581d57d457f35746587c5836579a577557b157a95813582457c657bb570e559e54c254b055d257b65857586c5871583f582d588558d558ec58f158e858d858cd58c6583c5802581258295849584c58425855582758195874580e560954df54bd55df580758965858581157ff5819586458a858d158fa5915591458fc58e4584c56d557ca587358c45897586a584a57955739581257d2560b54e254af558a576f584d5832580b5815584b589a58b758a4589b5885584d581d5815575d")

txt_filloc = 'C:/Users/WA2/Desktop/tempout.txt'
np.savetxt(txt_filloc,temp,fmt='%.6f')
img_arr = np.reshape(temp,(30,30))
img_gr = Image.fromarray(img_arr.astype('uint8'),'L')
img_gr.show()