from PIL import Image
from pytesseract import pytesseract
from googletrans import Translator
translator = Translator()
#path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#pytesseract.tesseract_cmd = path_to_tesseract


def Simplifier(text):
	string=""
	for i in text:
		if i .isalnum() or i.isspace() or i=='.':
			string = string + i.lower()
		else:
			string = string + ' ' 
	return string
	
	
def Text_convertor(img_,flag):
	img=Image.open(img_)
	if (flag):
		text=pytesseract.image_to_string(img,lang='hin')
	else:
		text=pytesseract.image_to_string(img)
	return text


def English(string):
	value=translator.translate(string)
	return value.text
