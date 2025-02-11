#!/usr/bin/python3
"""Defines function that converts csv to json"""
import csv
import json


import csv


def process_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Do something with the row data
                value = int(row[0])  # ValueError if row[0] is not a number
                print(value)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: CSV file contains invalid data (non-numeric values).")
    except IOError as e:  # IOErrors (e.g., file permissions)
        print(f"An I/O error occurred: {e}")
    except Exception as e:  # make sure unexpected errors get captured printed
        print(f"An unexpected error occurred: {e}")


# Example usage
process_csv("my_data.csv")
