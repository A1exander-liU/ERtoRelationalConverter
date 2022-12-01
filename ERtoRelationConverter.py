import json


def pick_primary(data: dict) -> str:
    return data["key"]


def decompose_composite(data: dict):
    for _ in data["composite"]:
        for attribute in _.items:
            data["attribute"].push(attribute)


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)


if __name__ == "__main__":
    main()
