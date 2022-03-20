from utils1 import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/<int:id>")
def page_main(id):
    return render_template("list.html", candidates=get_candidate(id))

#
# @app.route("/candidate/<int:id>")
# def page_candidate(id):
#     return get_candidate_id(id, all_candidates)
#
#
# @app.route("/skills/<skill>")
# def page_skills(skill):
#     return get_candidate_skills(skill, all_candidates)
#
# @app.route("/sanya")
# def sanek():
#     return "Привет Саня!)"

if __name__ == '__main__':
    app.run()

