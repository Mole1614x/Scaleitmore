from PIL import Image
from gtts import gTTS
import pttesseract
import os

from new import mage_to_sound

pytesseract.pytesseract.tesseract_cmd="C\Program Files\Tesseeract-OCR\tesseract.exe"

def convert_to_sound(image):

    try:
        open_image=Image.open(image)
        text=pytesseract.image_to_string(open_image)
        print(text_file)
        sound=gTTS(text_file, lang="en")
        sound.save("sound.mp3")
        os.system("sound.mp3")
        return True
    except Exception as bug:
        print("The error while executing the code\n",bug)
        return

if __name___=="_main_":
    image_to_sound("imagetext.jpg")
    input()
