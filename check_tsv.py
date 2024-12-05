# Compare TSV files
def compare_tsv(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        if f1.read() != f2.read():
            print("ERROR")

# Check files
compare_tsv("dependency_trees_from_ud.tsv", "sample.tsv")
