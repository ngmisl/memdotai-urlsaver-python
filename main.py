import requests
import metadata_parser
import os
from dotenv import load_dotenv

url = "https://api.mem.ai/v0/mems"


def get_metadata(input_url):
    page = metadata_parser.MetadataParser(url=input_url, search_head_only=True)
    meta_title = page.metadata["og"]["title"]
    meta_desc = page.metadata["og"]["description"]
    return f"{meta_title}\n{meta_desc}"


def main():
    save_url = input("Enter Url: ")

    # make sure to add a .env: API = <APIKEY>
    load_dotenv()
    api_key = os.getenv("API")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"ApiAccessToken {api_key}",
    }

    meta = get_metadata(save_url)
    data = {"content": f"Title: {meta}\nURL: {save_url}"}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Successfully saved")
    else:
        print("Failed to save: {response.status_code}")


if __name__ == "__main__":
    main()
