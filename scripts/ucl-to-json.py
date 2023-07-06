#!/usr/bin/env python
import pathlib
import json

import ucl


def main():
    for path in pathlib.Path(".").glob("*.ucl"):
        name, _ = path.name.split(".", 1)

        with open(path) as file_ucl, open(f"{name}.json", "w") as file_json:
            data = ucl.load(file_ucl.read())
            json.dump(data, file_json, indent=2)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
