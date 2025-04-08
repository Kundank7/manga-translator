from flask import Flask, render_template, request
from scraper import download_image
from ocr import extract_text_from_image
from translator import translate_text
import os
import uuid

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    image_path = ""

    if request.method == 'POST':
        image_url = request.form['image_url']
        image_name = f"{uuid.uuid4()}.jpg"
        image_path = os.path.join('static/images', image_name)

        # Step 1: Download image
        download_image(image_url, image_path)

        # Step 2: OCR
        extracted_text = extract_text_from_image(image_path)

        # Step 3: Translate
        translated_text = translate_text(extracted_text)

    return render_template('index.html', translated_text=translated_text, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
