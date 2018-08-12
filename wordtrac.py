# -*-coding:utf-8-*-

import re
import pytesseract
from PIL import Image

text=pytesseract.image_to_string(Image.open('test.jpg'),lang='chi_sim')
text = re.sub(r"\s{2,}","",text)
text = re.sub(r"\n","",text)
print(text)