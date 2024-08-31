import json


def json_reader(dicts):
    with open("js.json", "w") as outfile:
        json.dump(dicts, outfile)


def json_converter():
    with open("js.json", "r") as outfile:
        json_object = json.load(outfile)

    print(json_object)


def main():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    json_reader(x)
    json_converter()


if __name__ == "__main__":
    main()
