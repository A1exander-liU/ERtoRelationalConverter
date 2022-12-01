import json
end = '\033[0m'
underline = '\033[4m'

"""
Bonus Project - COMP 2714

Toco Tachibana (A01279235)
Alexander Liu (A01309846)
"""


def print_references(er_model: dict):
    """
    Print foreign key references.
    :param er_model: a dict
    :precondition: er model contains all the keys necessary
    :postcondition: prints all the foreign key references based on the er model
    :return: nothing
    """
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


def pretty_print(entity: dict):
    """
    Prints the given relational model that is represented as a dict
    :param entity: the relational model to print out as a relational schema
    :precondition: the entity must be a valid relational model represented as a dict
    :postcondition: the formatted print will look like this: EntityName[underlined pk's, attributes]
    :return: nothing
    """
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
    """
    Pick the primary key from the list of candidate keys.

    :param data: ER model as a dictionary
    :precondition: data is a dictionary containing an element with "key" as a key and a list as a value
    :postcondition: create a new element with the key "pk" to the passed dictionary
    """
    data['pk'] = [data['key'][0]]


def decompose_composite(data: dict):
    """
    Decompose composite attributes into atomic attributes.

    :param data: ER model as a dictionary
    :precondition: data is a dictionary containing elements with "composite" and "attribute" as keys
    :postcondition: retrieve values associated with the key "composite"
                    and append them to the list associated with the key "attributes"
    """
    for _ in data['composite']:
        for attributes in _.values():
            for attribute in attributes:
                data['attribute'].append(attribute)


def create_new_relation(data: dict, relation: dict) -> dict:
    """
    Creates a new relational model represented in json and appends it to the data.
    :param data: all the entity types in the conceptual model represented in json
    :param relation: all the relationships in the conceptual model represented in json
    :precondition: data is a dict that holds all the entity types, relation is a dict that represents the relationship
    to create a relational schema from
    :postcondition: adds a correct relational schema based on the relationship
    :return: a dict that is the relationship converted in a relational schema represented in json
    """
    list_of_participating_entities = [relation['data'][0], relation['data'][1]]
    new_entity_name = relation['data'][0].title() + relation['name'].title() + relation['data'][1].title()
    list_of_pk = []

    for entity in data:
        if entity['entity'] in list_of_participating_entities:
            list_of_pk.append(f"{entity['entity']}{entity['pk'][0].title()}")

    new_entity = {'entity': new_entity_name, 'key': list_of_pk, 'attribute': [], 'multivalued': [], 'composite': []}

    return new_entity


def extract_multivalued_relation(data: dict, resource: list):
    for attribute in data["multivalued"]:
        resource.append({"entity": data["entity"].title() + attribute.title(),
                         "key": [data["key"][0], attribute],
                         "attribute": []})


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)

    print("String representation of ER model...")
    for entity in er_model["data"]:
        print(entity)
    print()

    print("Convert conceptual design to relational model...")
    multivalued = []

    for entity in er_model["data"]:
        pick_primary(data=entity)
        decompose_composite(data=entity)
        extract_multivalued_relation(data=entity, resource=multivalued)

    er_model["data"].extend(multivalued)

    for entity in er_model["data"]:
        pretty_print(entity)

    for relation in er_model['relation']:
        pretty_print(create_new_relation(er_model['data'], relation))
    print()
    print_references(er_model)


if __name__ == "__main__":
    main()
