report = """
Task Report:

1. TSV file was downloaded from the provided URL.
2. The XML structure was designed to have a root, containing multiple elements. Each field in the TSV file was represented as a sub-elemen.
3. JSON structure resembles the XML hierarchy, representing sentences as lists of dictionaries.
4. The conversion back to TSV ensures identical formatting with the original file.
5. Libraries Used: csv, xml.etree.ElementTree, json.
6. Challenges: Proper alignment of fields and ensuring compatibility with the original format. Making the final tsv file identical to the initial tsv file
"""

print(report)

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report)
