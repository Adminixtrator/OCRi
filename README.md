# OCR - Optical Character Recognition

## Setting up on Heroku
### Add the two build packs to your heroku app
    https://github.com/heroku/heroku-buildpack-apt
    heroku/python
    
### Ensure you already have your requirements file and apt file then run the following in your heroku CLI
    heroku config:set TESSDATA_PREFIX=./.apt/usr/share/tesseract-ocr/4.00/tessdata
    
### Then add this in your python file 
    pt.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'

$_Once all is done, you can now deploy_

### Check out https://ocrn.herokuapp.com/


## Colaborators
    vahiwe@gmail.com
    minixtrator@gmail.com
