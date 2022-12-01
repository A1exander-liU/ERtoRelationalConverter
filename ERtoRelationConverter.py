import json


def pick_primary(data: dict) -> str:
    return data["key"]


def main():
    with open("data.json", "r") as er_model:
        er_model = json.load(er_model)


if __name__ == "__main__":
    main()
