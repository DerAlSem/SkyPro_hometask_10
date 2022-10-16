import json
DATA_SOURCE = 'candidates.json'

def load_candidates():
    """
    Загружает кандидатов из файла json (указать в DATA_SOURCE)
    :return:
    """
    with open(DATA_SOURCE, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates

def get_all():
    """
    Возвращает всех кандидатов
    """
    candidates = load_candidates()
    return candidates

def get_by_pk(pk):
    """
    Возвращает кандидата по его pk
    """
    candidates = load_candidates()
    for candidate in candidates:
        if candidate['pk'] == pk:
            return candidate
    return False

def get_by_skill(skill_name):
    """
    Возвращает кандидатов, подходящих по навыку.
    """
    candidates = load_candidates()
    fit_candidates = []
    print(skill_name)
    for candidate in candidates:
        skills = map(str.strip, candidate["skills"].lower().split(","))
        if skill_name in skills:
            fit_candidates.append(candidate)
    return fit_candidates