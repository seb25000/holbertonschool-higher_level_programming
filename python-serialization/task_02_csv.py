#!/usr/bin/python3
"""Defines function that converts csv to json"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Args:
        csv_filename (str): The name of the CSV file to convert.

    Returns:
        bool: True if the conversion was successful, False otherwise.
    """
    try:
        data = []
        with open(csv_filename, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                data.append(row)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Use indent pretty formatting

        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}")  # Optional: Print the specific error
        return False


if __name__ == '__main__':
    # Create a sample CSV file for testing
    with open("data.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"name": "John", "age": "28", "city": "New York"})
        writer.writerow({"name": "Alice", "age": "24", "city": "Los Angeles"})
        writer.writerow({"name": "Bob", "age": "22", "city": "Chicago"})
        writer.writerow({"name": "Eve", "age": "30", "city": "San Francisco"})

    csv_file = "data.csv"
    if convert_csv_to_json(csv_file):
        print(f"Data from {csv_file} has been converted to data.json")
    else:
        print(f"Failed to convert {csv_file} to data.json")
