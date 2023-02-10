def make_django_title_list_from_tuple(choices: tuple) -> list:
    return [(title, title) for title in choices]
