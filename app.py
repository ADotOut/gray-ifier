# Program to Upload Color Image and convert into Black & White image
import os
from flask import  Flask, request, redirect, url_for, render_template
import numpy as np
import cv2
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
def load_mainpage():
    return render_template("upload.html")
    


@app.route("/convert", methods=['POST'])
def upload_image():
    file = request.files['file']
    filename = secure_filename(file.filename)
    filedata = conv2grayscale(file.read())
    with open(os.path.join("static/", filename), 'wb') as filee:
        filee.write(filedata)
    display_msg = "Image uploaded"
    return render_template("upload.html", filename=filename, message=display_msg)
    
def conv2grayscale(image):
    somevar = np.fromstring(image, dtype='uint8')
    decoded = cv2.imdecode(somevar, cv2.IMREAD_UNCHANGED)
    converted = cv2.cvtColor(decoded, cv2.COLOR_RGB2GRAY)
    status, encoded = cv2.imencode(".png", converted)
    print(status)
    return encoded
    
@app.route("/display/<filename>/")
def get_processed_file(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()