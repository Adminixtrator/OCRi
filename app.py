import os
from flask import Flask, render_template, request
import pytesseract as pt
from PIL import Image

pt.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pt.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

# import our OCR function

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    img = Image.open(filename)
    text = pt.image_to_string(img)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
 


# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the upload page
@app.route('/', methods=['GET', 'POST'])
def upload_page():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run()
