import os

from flask import Flask, request, render_template, send_from_directory
from processing_audio import process_wav_to_jpg

app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    # target = os.path.join(APP_ROOT, 'static/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = os.path.join(target, filename)
        print ("Accept incoming file:", filename)
        print ("Save it to:", os.path.join(target, 'filename'))
        upload.save(destination)
        process_wav_to_jpg(destination, destination)
        os.remove(destination) 
        fname = filename.split('.')[0] + '.png' 
    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete_display_image.html", image_name=fname)

@app.route(r'/upload\<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
