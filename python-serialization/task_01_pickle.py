#!/usr/bin/python3
"""
Creates a Class
"""
import json
import pickle


class Student:
    """
    Class that defines student
    """

    def __init__(self, first_name, last_name, age):
        """ Initialize the attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)
        return new_dict

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)


try:
    with open("student.pkl", "wb") as f:
        student_1 = Student("John", "Doe", 30)
        pickle.dump(student_1, f)
except FileNotFoundError:
    print("Error: student.pkl not found")
except IOError as e:
    print(f"I/O error: {e}")
except Exception as e:  # catch all other exceptions
    print(f"An unexpected error occurred: {e}")


try:
    with open("student.pkl", "rb") as f:
        new_student = pickle.load(f)
    print(new_student.__dict__)
except FileNotFoundError:
    print("Error: student.pkl not found")
except pickle.PickleError as e:
    print(f"Pickling error: {e}")
except AttributeError as e:
    print(f"AttributeError: {e}")  # In case the class definition changed.
except EOFError:
    print("Error: Unexpected end of file during unpickling.")
except IOError as e:
    print(f"I/O error: {e}")
except Exception as e:  # Catch all other exceptions
    print(f"An unexpected error occurred: {e}")
