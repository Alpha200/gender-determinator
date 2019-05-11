import xml.etree.ElementTree as ET
import csv

# Download file from https://raw.githubusercontent.com/freedict/fd-dictionaries/master/eng-deu/eng-deu.tei
tree = ET.parse('eng-deu.tei')
root = tree.getroot()

ns = {"tei": "http://www.tei-c.org/ns/1.0"}

entries = root.findall('./tei:text/tei:body/tei:entry/tei:sense/tei:cit/tei:gramGrp/tei:gen/../..', ns)

results = [(
    entry.find("./tei:quote", ns).text.lower(),
    entry.find("./tei:gramGrp/tei:gen", ns).text.lower()
) for entry in entries]

results = list(set([result for result in results if result[0].find(" ") == -1]))
results.sort(key=lambda x: len(x[0]), reverse=True)

with open("genderdeterminator/words.csv", "w") as word_file:
    writer = csv.writer(word_file)
    writer.writerows(results)
