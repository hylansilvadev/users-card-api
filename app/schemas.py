def individual_serial(member) -> dict:
    return {
        'id': str(member['_id']),
        'name': member['name'],
        'tags': member['tags'],
        'intagram': member['instagram'],
        'linkedin': member['linkedin'],
        'github': member['github'],
    }


def list_serial(members) -> list:
    return [individual_serial(member) for member in members]
