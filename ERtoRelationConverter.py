import json


def convert(file):
    er_model = json.load(file)
    keys = er_model["key"]
    attributes = er_model["attributes"]
    multi_valued = er_model["multivalued"]
    composite = er_model["composite"]
    return


def main():
    file = open("sample.json")
    convert(file)


if __name__ == "__main__":
    main()
