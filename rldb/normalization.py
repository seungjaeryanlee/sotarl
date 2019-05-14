import find
from .db import entries


def get_human_normalized_score(entry):
    """
    Return human-normalized score of the entry.
    """
    human_entries = find.find_all({
        'env-title': entry['env-title'],
        'source-title': 'Human',
    })
    random_entries = find.find_all({
        'env-title': entry['env-title'],
        'source-title': 'Random',
    })

    if len(human_entries) > 1:
        print("[WARNING] More than one human entries were found for environment '{}'.".format(entry['env-title']))
        human_entries.sort(key=lambda entry: entry['score'], reverse=True)
    if len(random_entries) > 1:
        print("[WARNING] More than one random entries were found for environment '{}'.".format(entry['env-title']))
        random_entries.sort(key=lambda entry: entry['score'], reverse=True)

    return (entry['score'] - random_entries['score']) / (human_entries['score'] - random_entries['score'])
