from flask import Flask, render_template
import helpers

app = Flask(__name__)
@app.route("/")
def page_index():
  return render_template('list.html', candidates = helpers.get_all())

@app.route("/candidate/<int:pk>")
def page_candidate(pk):
    '''
    Карточки кандидатов по pk
    :param pk:
    :return:
    '''
    return render_template('card.html', candidate = helpers.get_by_pk(pk))

@app.route("/skill/<skill>")
def page_skills(skill):
    '''
    Страница с поиском кандидатов по навыку
    :param skill:
    :return:
    '''
    candidates = helpers.get_by_skill(skill.lower())
    return render_template("skill.html", candidates = candidates, amount = len(candidates) )

app.run()