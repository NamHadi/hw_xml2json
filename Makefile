# Define the "all" target, which depends on other targets
all: download tsv_to_xml xml_to_json json_to_tsv check_tsv generate_report


download:
	python download.py


tsv_to_xml:
	python tsv_to_xml.py


xml_to_json:
	python xml_to_json.py


json_to_tsv:
	python json_to_tsv.py


check_tsv:
	python check_tsv.py

# Target to generate a report
generate_report:
	python generate_report.py
