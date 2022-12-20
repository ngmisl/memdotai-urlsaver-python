import metadata_parser

saveUrl = input("Enter Url: ")

page = metadata_parser.MetadataParser(url=saveUrl, search_head_only="true")
metaDesc = page.metadata["og"]["description"]

print(metaDesc)
