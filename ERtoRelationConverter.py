import json
end = '\033[0m'
underline = '\033[4m'


def pretty_print(entity):
    print(entity["entity"].capitalize(), end="")
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


def pick_primary(data: dict) -> str:
    return data["key"]


def decompose_composite(data: dict):
    for _ in data["composite"]:
        for attribute in _.items:
            data["attribute"].push(attribute)


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)
        for entity in er_model["data"]:
            pretty_print(entity)


if __name__ == "__main__":
    main()
