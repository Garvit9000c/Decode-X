from PIL import Image
from pytesseract import pytesseract
  
image_path = r"./img.png"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
 
# Passing the image object to 
# image_to_string() function
# This function will
# extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
