from flask import Flask
import helpers

app = Flask(__name__)
@app.route("/")
def page_index():
    '''
    Главная страница
    :return:
    '''
    candidates = helpers.get_all()
    text = "<pre>"
    for candidate in candidates:
        text += f"Имя кандидата - {candidate['name']}\n"
        text += f"Позиция кандидата - {candidate['position']}\n"
        text += candidate['skills'] + "\n\n"
    text += "</pre>"
    return text

@app.route("/candidate/<int:pk>")
def page_candidate(pk):
    '''
    Страница с поиском кандидатов по pk
    :param pk:
    :return:
    '''
    candidate = helpers.get_by_pk(pk)
    text = f"<img src = '"\
           f"{candidate['picture']}'>\n"\
           f"<pre>Имя кандидата - {candidate['name']}\n"\
           f"Позиция кандидата - {candidate['position']}\n" \
           f"{candidate['skills']}</pre>"
    return text

@app.route("/skill/<skill>")
def page_skills(skill):
    '''
    Страница с поиском кандидатов по навыку
    :param skill:
    :return:
    '''
    candidates = helpers.get_by_skill(skill.lower())
    print(candidates)
    text = "<pre>"
    for candidate in candidates:
        text += f"Имя кандидата - {candidate['name']}\n"
        text += f"Позиция кандидата - {candidate['position']}\n"
        text += candidate['skills'] + "\n\n"
    text += "</pre>"
    return text

app.run()