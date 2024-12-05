import json
import xml.etree.ElementTree as ET

# Converting XML to JSON
def xml_to_json(input_xml, output_json):
    tree = ET.parse(input_xml)
    root = tree.getroot()
    data = []

    for sentence in root.findall("Sentence"):
        sentence_data = []
        for word in sentence.findall("Word"):
            word_data = {field.tag: field.text for field in word}
            sentence_data.append(word_data)
        data.append(sentence_data)

    # Save JSON
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Convert and save
xml_to_json("sample.xml", "sample.json")
print("XML converted to JSON: sample.json")
