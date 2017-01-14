from io import BytesIO
import requests
from PIL import Image
import pytesseract
url = 'http://static1.eniro.com/3.0.20/components/cgi-bin/txt2img.cgi?text=OTwTNQE8AAgSTAtdMgAfRjMQZiY1UnVaQU51bmEjaDVZYXMzVWNIVQ;E&font=Arial,22&fg=0,136,227&margin=0,3'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
print(pytesseract.image_to_string(img))
