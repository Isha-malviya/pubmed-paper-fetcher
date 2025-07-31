import csv
import re
from typing import List, Dict
from Bio import Entrez

Entrez.email = "ishamalviya207@gmail.com"  # Change this to your email

def fetch_pubmed_results(query: str, debug: bool = False) -> List[Dict]:
    handle = Entrez.esearch(db="pubmed", term=query, retmax=20)
    record = Entrez.read(handle)
    ids = record["IdList"]
    if debug:
        print(f"Found {len(ids)} articles")
    if not ids:
        return []
    
    handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline", retmode="text")
    data = handle.read()
    # Simple MEDLINE parser
    return parse_medline_data(data, debug=debug)

def parse_medline_data(raw_data: str, debug: bool = False) -> List[Dict]:
    results = []
    entries = raw_data.strip().split("\n\n")
    for entry in entries:
        lines = entry.split("\n")
        paper = {
            "PubmedID": "",
            "Title": "",
            "Publication Date": "",
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": ""
        }
        affiliations = []
        authors = []

        for line in lines:
            if line.startswith("PMID"):
                paper["PubmedID"] = line.split("- ")[-1].strip()
            elif line.startswith("TI"):
                paper["Title"] = line.split("- ")[-1].strip()
            elif line.startswith("DP"):
                paper["Publication Date"] = line.split("- ")[-1].strip()
            elif line.startswith("AU"):
                authors.append(line.split("- ")[-1].strip())
            elif line.startswith("AD"):
                affiliations.append(line.split("- ")[-1].strip())
            elif line.startswith("FAU") and "@" in line:
                paper["Corresponding Author Email"] = re.findall(r"[\w\.-]+@[\w\.-]+", line)[0]

        for affil in affiliations:
            if not re.search(r"university|college|institute|school|hospital", affil, re.I):
                paper["Company Affiliation(s)"].append(affil)

        if paper["Company Affiliation(s)"]:
            paper["Non-academic Author(s)"] = authors
            results.append(paper)
            if debug:
                print(f"Selected paper: {paper['PubmedID']} - {paper['Title']}")
    return results

def save_to_csv(results: List[Dict], filename: str):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

