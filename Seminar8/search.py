from model import get_disciplines_dict, get_pupil_dict


def search_discipline(name):
    disc_dict = get_disciplines_dict()

    if name.capitalize() in disc_dict.keys():

        return True, disc_dict[name.capitalize()]

    return False, ''


def search_pupil(discipline, pupil_name):
    pupil_dict = get_pupil_dict(discipline)
    name_to_search = pupil_name.capitalize()

    if name_to_search in pupil_dict.keys():
        return True
    else:
        return False
