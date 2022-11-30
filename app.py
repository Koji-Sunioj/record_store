from flask import Flask, json, jsonify, url_for, request
from pointers import options, return_object
app = Flask(__name__)

@app.route("/albums/",methods=["GET","POST"])
def all_or_create():
    try:
        data = options[request.method](request.get_json(silent=True))
        return jsonify({"data":data,**return_object[request.method]}),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400
        

@app.route("/albums/<string:album_id>",methods=["GET","DELETE","PATCH"])
def get_mutate_one(album_id):
    try:
        payload = {"data":request.get_json(silent=True),"album_id":album_id}
        data = options[request.method+"_album"](payload)
        return jsonify({"data":data,**return_object[request.method+"_album"]}),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400