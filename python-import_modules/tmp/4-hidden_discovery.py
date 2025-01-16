#!/usr/bin/env python3

import marshal
import types
import sys
import os

def get_names_from_pyc(pyc_file_path):
    """Extracts names from a .pyc file, filtering out those starting with '__'.

    Args:
        pyc_file_path (str): The path to the .pyc file.

    Returns:
        list: A sorted list of names extracted from the .pyc file, 
              excluding those starting with '__'.
    """
    names = []
    try:
        with open(pyc_file_path, 'rb') as f:
            # Skip the magic number and timestamp
            f.read(8)
            code_obj = marshal.load(f)
            
            for const in code_obj.co_consts:
                if isinstance(const, types.CodeType):
                    code_obj = const
                    break

            for name in code_obj.co_names:
                if not name.startswith('__'):
                    names.append(name)
                    
            for const in code_obj.co_consts:
                if isinstance(const, types.CodeType):
                    for name in const.co_names:
                         if not name.startswith('__'):
                                names.append(name)


    except Exception as e:
        print(f"Error reading pyc file: {e}", file=sys.stderr)
    return sorted(list(set(names)))
    

if __name__ == "__main__":
    pyc_file_path = "/tmp/hidden_4.pyc"  # Correct path to the .pyc file
    if not os.path.exists(pyc_file_path):
        print(f"Error: File not found: {pyc_file_path}", file=sys.stderr)
        sys.exit(1)


    names = get_names_from_pyc(pyc_file_path)
    for name in names:
        print(name)
