from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from models import MobileNet
import os, time, json
from io import BytesIO
from base64 import b64encode
from math import floor
from PIL import Image

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = './static/img'

model = MobileNet()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/infer', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files.getlist('file')
        if len(f)<=3 and len(f)!=0:
            pred_list = []
            for i in f:
                #saveLocation = f.filename
                saveLocation = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(i.filename))
                i.save(saveLocation)
                print(saveLocation)

                inference, confidence = model.infer(saveLocation)
                # make a percentage with 2 decimal points
                confidence = floor(confidence * 10000) / 100
                print(confidence)

                # delete file after making an inference
                #os.remove(saveLocation)

                pred_list.append({'inference': inference, 'confidence': confidence, 'img': saveLocation, 'time': time.time()})               
                print(pred_list)
            
            pred_info = json.load(open('pred_info.json','r'))
            """
            empty_dict = {}
            json_dump = json.dumps(empty_dict)
            
            with open("pred_info.json","r+") as file:
                try:
                    pred_info = json.load(file)
                except:
                    pred_info = {}
                    pred_info=json.dump(pred_info,file)
            """
            print("printing pred info",pred_info)
            last_5 = sorted(pred_info, key = lambda i: i['time'], reverse=True)[0:5]
            print("printing last5",last_5)
            with open("pred_info.json", "w") as info:
                pred_info.extend(pred_list)
                json.dump(pred_info, info)
            return render_template('inference.html', pred_list=pred_list, last_5=last_5)
        else:
            err_msg = 'Please upload Min 1 or Max 3 files'
            return render_template('index.html', err_msg=err_msg)

        # respond with the inference


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
    #app.run(host='0.0.0.0', port=5000, debug=True)