import json


def print_references(er_model: list, table_name: str):
    table_attributes = []
    print("References: ")
    for relation in er_model["relation"]:
        if table_name in relation.get("name"):
            table_attributes = relation.get("data")

    for entity in er_model["data"]:
        if entity.get("entity") in table_attributes:
            table = table_attributes[0] + table_name + table_attributes[1]
            foreign_key = entity.get("entity") + entity.get("key")[0]
            reference = f"\t {table}.{foreign_key} references to {entity.get('entity')}.{entity.get('key')[0]}"
            print(reference)


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)

    print_references(er_model, "teaches")


### find_foreign_keys()


if __name__ == "__main__":
    main()
