from flask import Flask, json, jsonify, url_for, request
from pointers import options, return_object

app = Flask(__name__)

@app.route("/albums/",methods=["GET","POST"])
def all_or_create():
    try:
        data = options[request.method](decode(request))
        return jsonify({"data":data,**return_object[request.method]}),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400



@app.route("/albums/<string:album_id>",methods=["GET","DELETE","PATCH"])
def get_mutate_one(album_id):
    try:
        route_key,test = request.method+"_album", request.method in ["GET","DELETE"]
        payload = [{**decode(request),"album_id":album_id},album_id][test]
        data = options[route_key](payload)
        message = return_object[route_key]
        return jsonify(({"data":{**data}, **message},{**message})[data =={}]),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400


def decode(request):
    return request.json if request.get_json(silent=True) else {}

