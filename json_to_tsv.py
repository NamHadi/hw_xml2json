import json
import csv

# Converting JSON to TSV
def json_to_tsv(input_json, output_tsv):
    with open(input_json, encoding="utf-8") as json_file:
        data = json.load(json_file)

    with open(output_tsv, "w", encoding="utf-8", newline="") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")

        for sentence in data:
            for word in sentence:
                row = [word[key] for key in sorted(word.keys())]
                writer.writerow(row)
            writer.writerow([])  # Add an empty row between sentences

# Convert and save
json_to_tsv("sample.json", "sample.tsv")
print("JSON converted to TSV: sample.tsv")
