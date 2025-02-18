#!/usr/bin/python3
"""Defines function that fetches posts"""
import csv
import requests


def fetch_and_print_posts(url="https://jsonplaceholder.typicode.com/posts"):
    """function fetches and prints"""
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    print("Status Code: {}".format(res.status_code))

    if res.headers.get("Content-Type") == "application/json; charset=utf-8":
        json_data = res.json()
        for post in json_data:
            print(post["title"])
    else:
        print("Unexpected content type:", res.headers.get("Content-Type"))


def fetch_and_save_posts(url="https://jsonplaceholder.typicode.com/posts",
                         csvfile="posts.csv"):
    """
    Fetches all posts from JSONPlaceholder and saves them in a csv file.
    Args:
        url (str): The URL to fetch posts from.
        csvfile (str): The name of the CSV file to save the data to.
    """
    try:
        res = requests.get(url)
        res.raise_for_status()  # Raise HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return

    try:
        json_data = res.json()
    except ValueError as e:
        print(f"Failed to parse JSON: {e}")
        return
    filtered_data = [{key: post[key] for key in ('id', 'title', 'body')}
                     for post in json_data]

    headers = ['id', 'title', 'body']

    try:
        with open(csvfile, "w", newline="") as file:
            csv_write = csv.DictWriter(file, fieldnames=headers)
            csv_write.writeheader()
            csv_write.writerows(filtered_data)
        print(f"Data saved to {csvfile}")
    except IOError as e:
        print(f"Failed to write to file: {e}")


if __name__ == "__main__":
    fetch_and_print_posts()  # Call the function to print titles
    fetch_and_save_posts()    # Call the function to save to CSV
