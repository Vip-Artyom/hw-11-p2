from utils1 import *
from flask import Flask, render_template

app = Flask(__name__)

data = load_candidates_from_json("candidates.json")


@app.route("/")
def page_main():
    return render_template("list.html", candidates=data)


@app.route("/candidate/<int:id>")
def page_candidate(id):
    candidate = get_candidate(id)
    return render_template("single.html", candidate=candidate)


@app.route("/search/<candidate_name>")
def page_search_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_len=len(candidates))


@app.route("/skills/<skill>")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill)
    return render_template("skills.html", candidates=candidates, candidates_len=len(candidates), skill=skill)


if __name__ == '__main__':
    app.run()
