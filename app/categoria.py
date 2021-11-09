from flask import Flask, request, jsonify
from pathlib import Path
import os



app = Flask(__name__)

@app.route('/api/get_content', methods=['POST'])

def ordenar():
    order = ""
    reverse_order = ""
    data = request.get_json(force=True)
    path = data['path']
    
    if 'order' in data.keys():
        order = str(data['order'])
    if 'reverse_order' in data.keys():
        reverse_order = str(data['reverse_order'])

    if order == "size" and reverse_order == "" or reverse_order == "False":
        j=0
        dic={}
        paths = sorted(Path(path).iterdir(), key=os.path.getsize)
        for i in paths:
            dic[j] = [str(i)]
            j+=1
        return jsonify(dic)

    elif order == "size" and reverse_order == "True":
        j=0
        dic={}
        paths = sorted(Path(path).iterdir(), key=os.path.getsize)
        paths.reverse()
        for i in paths:
            dic[j] = [str(i)]
            j+=1
        return jsonify(dic)
    
    elif order == "" and reverse_order == "True":
        j=0
        dic={}
        paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
        paths.reverse()
        for i in paths:
            dic[j] = [str(i)]
            j+=1
        return jsonify(dic)

    else:
        j=0
        dic={}
        paths = sorted(Path(path).iterdir(), key=os.path.getmtime)
        for i in paths:
            dic[j] = [str(i)]
            j+=1
        return jsonify(dic)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'Mensaje':'Viva Peru!'})


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)