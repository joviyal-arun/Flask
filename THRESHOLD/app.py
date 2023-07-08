from flask import *  
import cv2 
import numpy as np
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'img')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/',methods=['POST','GET'])
def homepage():
    if request.method=='GET':
        return render_template('display.html')

@app.route("/threshod_value", methods=['POST'])
def threshod_value():
    if request.method=='POST':
        threshold_value = request.form.get('myRange')
        input_image = os.path.join(app.config['UPLOAD_FOLDER'], 'input.jpg')
        read_image=cv2.imread(input_image)
        color_converting = cv2.cvtColor(read_image, cv2.COLOR_BGR2GRAY)
        ret, thresh1 = cv2.threshold(color_converting, int(threshold_value), 255, cv2.THRESH_BINARY)
        cv2.imwrite('static/img/output.png',thresh1)
        output_image = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
        return render_template("display.html", user_image=input_image,user_image1=output_image)
 

if __name__ == "__main__":
    app.run(debug=True)


