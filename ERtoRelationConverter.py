import json


def pick_primary(data: dict) -> str:
    return data["key"][0]


def decompose_composite(data: dict):
    for _ in data["composite"]:
        for attributes in _.values():
            for attribute in attributes:
                data["attribute"].append(attribute)


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)

    for entity in er_model["data"]:
        primary_key = pick_primary(entity)
        decompose_composite(entity)


if __name__ == "__main__":
    main()
