from PIL import Image
from pytesseract import pytesseract
from googletrans import Translator
translator = Translator()
#path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.tesseract_cmd = path_to_tesseract
def sp(t):
	s=""
	for i in t:
		if i .isalnum() or i.isspace() or i=='.':
			s=s+i.lower()
		else:
			s=s+' ' 
	return s
	
def con(img_):
	img=Image.open(img_)
	text1 = pytesseract.image_to_string(img,lang='hin')
	text2 = pytesseract.image_to_string(img)
	if (len(text1.split())>len(text2.split())):
		text=text1
	else:
		text=text2
	return text

def Eng(s):
	st=translator.translate(s)
	return st.text
