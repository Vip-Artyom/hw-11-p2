import json


def load_candidates_from_json(path):
    """Функция загружает весь список из Json файла"""

    file = open(path, "r", encoding="utf - 8")
    data = json.load(file)
    file.close()
    return data


candidates = load_candidates_from_json("candidates.json")


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    return candidates[candidate_id-1]



def get_candidates_by_name(candidate_name, candidates):
    """Возвращает кандидатов по имени"""
    for candidate in candidates:
        if candidate_name == candidate["name"]:
            return candidate_name




def get_candidates_by_skill(skill_name, candidates):
    """Возвращает кандидатов по навыку"""
    all_candidate_skill = ""
    for candidate in candidates:
        skill_list = candidate["skills"].lower().split(",")
        if skill_name.lower() in skill_list:
            candidate_user = candidate["skills"]
            all_candidate_skill += candidate_user

    if len(all_candidate_skill) < 1:
        return "Такой навык не найден"
    else:
        return all_candidate_skill

