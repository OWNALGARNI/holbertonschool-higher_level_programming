#!/usr/bin/python3
import requests
import csv

URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()

    for post in posts:
        print(post["title"])


def fetch_and_save_posts():
    response = requests.get(URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code != 200:
        return

    posts = response.json()

    structured_posts = [
        {"id": post["id"], "title": post["title"], "body": post["body"]}
        for post in posts
    ]

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        writer.writeheader()
        writer.writerows(structured_posts)
