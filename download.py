import requests

# Download the file
url = "https://example.com/dependency_trees_from_ud.tsv"  # Replace with actual URL
response = requests.get(url)

# Save the file
with open("dependency_trees_from_ud.tsv", "wb") as f:
    f.write(response.content)

print("File downloaded: dependency_trees_from_ud.tsv")
