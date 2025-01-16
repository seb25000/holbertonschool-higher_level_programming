#!/usr/bin/python3


if __name__ == "__main__":
    import importlib.util
    import os

    file_path = "variable_load_5.py"
    
    spec = importlib.util.spec_from_file_location("variable_load_5", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    print(module.a)
