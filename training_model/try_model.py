from xml.etree import ElementTree
import csv
import os

def writeToCSV(csvwriter, tree):
    root = tree.getroot()

    for tweet in root.findall('tweet'):
        data = []
        data.append(tweet.find('content').text)
        data.append(tweet.find('sentiment/polarity/value').text)
        csvwriter.writerow(data)

directory = os.fsencode('corpus')
output = open('corpus/corpus.csv', 'w', newline='', encoding = 'utf-8')
csvwriter = csv.writer(output)
csvwriter.writerow(['text', 'sentiment'])

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    path = ''.join(['corpus/',filename])

    if filename.endswith(".xml"): 
        tree = ElementTree.parse(path)
        writeToCSV(csvwriter, tree)