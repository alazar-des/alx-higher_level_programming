#!/usr/bin/python3
"""Write all command line arguments to json file.
"""


import sys
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
if __name__ == "__main__":
    try:
        arg_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        arg_list = []
    finally:
        for i in range(1, len(sys.argv)):
            arg_list.append(sys.argv[i])
        save_to_json_file(arg_list, "add_item.json")
