import json
end = '\033[0m'
underline = '\033[4m'


def print_references(er_model: dict):
    table_name = ""
    table_attributes = []
    print("References: ")
    for relation in er_model["relation"]:
        table_name = relation.get("name")
        table_attributes = relation.get("data")

    for entity in er_model["data"]:
        if entity.get("entity") in table_attributes:
            table = table_attributes[0].title() + table_name.title() + table_attributes[1].title()
            foreign_key = entity.get("entity") + entity.get("key")[0].title()
            reference = f"\t {table}.{foreign_key} references {entity.get('entity').title()}.{entity.get('key')[0]}"
            print(reference)


def pretty_print(entity):
    print(entity['entity'][0].capitalize() + entity['entity'][1:], end="")
    print("[", end="")
    i = 0
    for key in entity['key']:
        if i != len(entity['key']) - 1:
            print(f"{underline}{key}, {end}", end="")
        else:
            print(f"{underline}{key}{end}", end="")
        i += 1
    for attribute in entity['attribute']:
        print(f", {attribute}", end="")
    print("]")


def pick_primary(data: dict):
    data['pk'] = [data['key'][0]]


def decompose_composite(data: dict):
    for _ in data['composite']:
        for attributes in _.values():
            for attribute in attributes:
                data['attribute'].append(attribute)


def create_new_relation(data: dict, relation: dict) -> dict:
    list_of_participating_entities = [relation['data'][0], relation['data'][1]]
    new_entity_name = relation['data'][0].title() + relation['name'].title() + relation['data'][1].title()
    list_of_pk = []

    for entity in data:
        if entity['entity'] in list_of_participating_entities:
            list_of_pk.append(f"{entity['entity']}{entity['pk'][0].title()}")

    new_entity = {'entity': new_entity_name, 'key': list_of_pk, 'attribute': [], 'multivalued': [], 'composite': []}

    return new_entity


def main():
    with open("data2.json", "r") as er_model:
        er_model = json.load(er_model)

    for entity in er_model["data"]:
        pick_primary(data=entity)
        decompose_composite(data=entity)
        # extract_multivalued_relation(data=entity, resource=er_model)
        pretty_print(entity)

    for relation in er_model['relation']:
        pretty_print(create_new_relation(er_model['data'], relation))

    print_references(er_model)


if __name__ == "__main__":
    main()
