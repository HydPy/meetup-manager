import json
import re


def parser(issue: str):
    '''
    Extracts out:
    - Title of the talk
    - Abstract
    - Category
    - Duration
    - Level of Audience
    - Speaker's Bio
    '''

    # Regex for comments
    comments = r'(\<|\d+\.|One).+(-|\>|\.)$'
    details = re.sub(comments, '', issue, flags=re.M).strip()

    issue = re.split(r'\*\*.+\*\*', details, 7, flags=re.M)
    talk_details = {
        'title': None,
        'abstract': None,
        'category': None,
        'duration': None,
        'level': None,
        'bio': None,
        'pre-req': None
    }

    j = 1  # Index zero in list is empty
    for i in talk_details.keys():
        if j < len(issue):
            talk_details[i] = issue[j].strip()
            j += 1
        else:
            break

    talk_details = json.dumps(talk_details)

    return json.loads(talk_details)
