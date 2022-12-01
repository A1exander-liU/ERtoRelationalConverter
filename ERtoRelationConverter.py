import json
end = '\033[0m'
underline = '\033[4m'


def pretty_print(entity):
    print(entity["entity"][0].capitalize() + entity['entity'][1:], end="")
    print("[", end="")
    i = 0
    for key in entity["key"]:
        if i != len(entity["key"]) - 1:
            print(f"{underline}{key}, {end}", end="")
        else:
            print(f"{underline}{key}{end}, ", end="")
        i += 1
    i = 0
    for attribute in entity["attribute"]:
        if i != len(entity["attribute"]) - 1:
            print(f"{attribute}, ", end="")
        else:
            print(f"{attribute}", end="")
        i += 1
    print("]")


def pick_primary(data: dict):
    data["pk"] = [data["key"][0]]


def decompose_composite(data: dict):
    for _ in data["composite"]:
        for attributes in _.values():
            for attribute in attributes:
                data["attribute"].append(attribute)


def create_new_relation(data: dict, relation: dict) -> dict:
    list_of_participating_entities = [relation['data'][0], relation['data'][1]]
    first_entity = relation['data'][0].title()
    relationship_name = relation['name'].title()
    second_entity = relation['data'][1].title()
    new_entity_name = first_entity + relationship_name + second_entity
    list_of_pk = []

    for entity in data:
        if entity['entity'] in list_of_participating_entities:
            list_of_pk.append(f"{entity['entity'].title()}{entity['pk'][0].title()}")

    new_entity = {'entity': new_entity_name, 'key': list_of_pk, 'attribute': [], 'multivalued': [], 'composite': []}

    return new_entity


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)

    for entity in er_model["data"]:
        pick_primary(data=entity)
        decompose_composite(data=entity)
        # extract_multivalued_relation(data=entity, resource=er_model)
        pretty_print(entity)

    for relation in er_model["relation"]:
        pretty_print(create_new_relation(er_model['data'], relation))


if __name__ == "__main__":
    main()
