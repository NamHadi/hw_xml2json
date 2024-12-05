report = """
Task Report:

1. The TSV file was downloaded from the provided URL.
2. The XML structure was designed to have a root <Sentences> element, containing multiple <Sentence> elements, each with <Word> elements. Each field in the TSV file was represented as a sub-element within <Word>.
3. The JSON structure mirrors the XML hierarchy, representing sentences as lists of dictionaries (one per word).
4. The conversion back to TSV ensures identical formatting with the original file.
5. Libraries Used: csv, xml.etree.ElementTree, json.
6. Challenges: Proper alignment of fields and ensuring compatibility with the original format. Addressed by consistent ordering of fields and spacing.
"""

print(report)

with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report)
