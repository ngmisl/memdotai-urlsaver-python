import requests
import metadata_parser
import os
from dotenv import load_dotenv

url = "https://api.mem.ai/v0/mems"

saveUrl = input("Enter Url: ")

# make sure to add a .env: API = <APIKEY>
load_dotenv()
APIKEY = os.getenv("API")

headers = {
    "Content-Type": "application/json",
    "Authorization": "ApiAccessToken " + str(APIKEY),
}

# queries the title and description of the given URL
def getMetadata(input):
    page = metadata_parser.MetadataParser(url=input, search_head_only="true")
    metaTitle = page.metadata["og"]["title"]
    metaDesc = page.metadata["og"]["description"]
    return metaTitle + "\n" + metaDesc


def main():
    meta = getMetadata(saveUrl)
    data = {"content": "Title: " + meta + "\n" + "URL: " + saveUrl}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Successfully saved")
    else:
        print("Failed to save")


if __name__ == "__main__":
    main()
