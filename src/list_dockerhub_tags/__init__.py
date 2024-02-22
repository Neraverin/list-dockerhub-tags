""" Simple util to print all image tags from Dockerhub """

import argparse
import json
import requests

def print_docker_tags(repository):
    next_page = f"https://hub.docker.com/v2/repositories/library/{repository}/tags?page=1&page_size=1000"

    while next_page != "null":
        response = requests.get(next_page, timeout=10)
        data = response.json()

        for tag in data["results"]:
            print(tag["name"])

        next_page = data.get("next", "null")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List all tags from Dockerhub registry")
    parser.add_argument("registry", type=str, help="Dockerhub registry name")
    args = parser.parse_args()

    print_docker_tags(args.registry)
