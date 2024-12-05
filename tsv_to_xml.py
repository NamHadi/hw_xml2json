import csv
import xml.etree.ElementTree as ET

# Convert TSV to XML
def tsv_to_xml(input_tsv, output_xml):
    root = ET.Element("Sentences")  # Root element
    
    with open(input_tsv, encoding="utf-8") as tsv_file:
        reader = csv.reader(tsv_file, delimiter="\t")
        sentence = None
        for row in reader:
            if not row:  # Empty row indicates a new sentence
                sentence = None
                continue

            if sentence is None:
                sentence = ET.SubElement(root, "Sentence")
            
            word = ET.SubElement(sentence, "Word")
            for i, value in enumerate(row):
                ET.SubElement(word, f"Field{i}").text = value

    # Save XML
    tree = ET.ElementTree(root)
    tree.write(output_xml, encoding="utf-8", xml_declaration=True)

# Convert and save
tsv_to_xml("dependency_trees_from_ud.tsv", "sample.xml")
print("TSV converted to XML: sample.xml")
