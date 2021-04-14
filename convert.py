from PIL import Image
from pytesseract import pytesseract
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
	text = pytesseract.image_to_string(img)
	return text

