import json

__data = []


def load_candidates_from_json(path):
    """Функция загружает весь список из Json файла"""
    global __data
    file = open(path, "r", encoding="utf - 8")
    __data = json.load(file)
    file.close()
    return __data


def get_candidate(candidate_id):
    """Возвращает одного кандидата по его id"""
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"]
            }
    return {'not_found': 'Кандидат не найден'}


def get_candidates_by_name(candidate_name):
    """Возвращает кандидатов по имени"""
    # for candidate in __data:
    #     if candidate_name == candidate["name"]:
    #         return candidate_name
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]


def get_candidates_by_skill(skill_name):
    """Возвращает кандидатов по навыку"""
    all_candidate_skill = []
    for candidate in __data:
        skill_list = candidate["skills"].lower().split(", ")
        if skill_name.lower() in skill_list:
            all_candidate_skill.append(candidate)
    return all_candidate_skill
