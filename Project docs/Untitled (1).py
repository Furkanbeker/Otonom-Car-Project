#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


# Open the image file
image = Image.open('C:/Users/hakan/OneDrive/Desktop/speed_limit_sign.jpg')

# Extract the text from the image using pytesseract
text = pytesseract.image_to_string(image)

# Search the extracted text for the speed limit value
speed_limit = None
for word in text.split():
    if word.isdigit():
        speed_limit = int(word)
        break

# Print the speed limit value
if speed_limit is not None:
    print(f'Speed limit: {speed_limit}')
else:
    print('Unable to detect speed limit')


# In[ ]:




