from flask import Flask, flash, request, redirect, render_template
from keras.models import load_model
import numpy as np
import os
import cv2


app = Flask(__name__)
model = load_model('best_model_96_test.h5')

UPLOAD_FOLDER = '/Users/sai/Desktop/python/DS/app/static/images/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
classes = {0: 'bird', 1: 'boar', 2: 'dog', 3: 'dragon', 4: 'hare', 5: 'horse',
           6: 'monkey', 7: 'ox', 8: 'ram', 9: 'rat', 10: 'snake', 11: 'tiger', 12: 'zero'}


@app.route('/')
def hello():
    return render_template('home.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/success', methods=['POST'])
def display():
    if request.method == 'POST':
        image = request.files['photo']
        if image.filename == '':
            flash('No selected file')
            return render_template("home.html")
        if image and allowed_file(image.filename):
            image.save(os.path.join(
                UPLOAD_FOLDER, "display.png"))
            img = cv2.imread(UPLOAD_FOLDER + "display.png")
            img = cv2.resize(img, (300, 300), cv2.INTER_AREA)
            img = np.expand_dims(img, axis=0)
            pred = model.predict(img)
            pred = np.argmax(pred, axis=1)[0]

        return render_template("success.html", prediction=classes[pred - 1])

    return render_template("home.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
