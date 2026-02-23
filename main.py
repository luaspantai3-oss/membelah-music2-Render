from flask import Flask, request, send_file
import os
from spleeter.separator import Separator

app = Flask(__name__)
separator = Separator('spleeter:2stems')

@app.route('/')
def home():
    return "Spleeter API aktif!"

@app.route('/separate', methods=['POST'])
def separate():
    file = request.files['file']
    filename = "input.wav"
    file.save(filename)

    separator.separate_to_file(filename, 'output')

    return send_file("output/input/vocals.wav", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
