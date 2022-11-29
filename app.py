from flask import Flask, json, jsonify, url_for, request
from db import table_scan,create_album,get_album,delete_album, patch_album
app = Flask(__name__)

@app.route("/albums/",methods=["GET","POST"])
def all_or_create():
    try:
        if request.method == "GET":
            return_object = table_scan()
        elif request.method == "POST":
            return_object = {"message":"sucess","data":create_album(request.json)}
        return jsonify(return_object),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400
        

@app.route("/albums/<int:album_id>",methods=["GET","DELETE","PATCH"])
def get_mutate_one(album_id):
    try:
        if request.method == "GET":
            return_object = get_album(album_id)
        elif request.method == "DELETE":
            delete_album(album_id)
            return_object = {"message":"album %s deleted" % str(album_id)}
        elif request.method == "PATCH":
            updated = patch_album(album_id,request.json)
            return_object = {"message":"album %s updated" % str(album_id),"data":updated}
        return jsonify(return_object),200
    except Exception as e:
        print(e)
        return jsonify({"message":"invalid request"}),400

