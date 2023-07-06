#!/usr/bin/env python
import pathlib
import json

import ucl
import toml


def main():
    for path in pathlib.Path(".").glob("*.ucl"):
        name, _ = path.name.split(".", 1)

        with open(path) as file_ucl, open(f"{name}.json", "w") as file_json, open(f"{name}.toml", "w") as file_toml:
            data = ucl.load(file_ucl.read())
            json.dump(data, file_json, indent=2)
            toml.dump(data, file_toml)

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
