from flask import Blueprint, jsonify
from .model import HtmlData, ResultPage
from config import DATA_DIR
import os

betcsgo = Blueprint('betcsgo', __name__, url_prefix="/betcsgo")

@betcsgo.route("/html", methods=["GET"])
def bet():
    _data = HtmlData.get_last_html()
    html = _data['html'].decode('unicode-escape')
    return jsonify( {"data": html, "message" : True, "length":len(html)} )


@betcsgo.route("/task/<int:number>", methods=["GET"])
def task(number):
    path = os.path.join( DATA_DIR, "task.txt" )
    with open(path, "a", encoding="utf8") as f:
        f.write("{}\n".format( number ))
    return "Task : {}".format(number)


@betcsgo.route("/result/<int:number>", methods=["GET"])
def page_result(number):
    result = ""
    _data = ResultPage.get_match_result( number )
    if _data:
        result = _data["data"].decode('unicode-escape')
    return jsonify({"result":  result, "message":True, "m_id": number, "length" : len(result)})
