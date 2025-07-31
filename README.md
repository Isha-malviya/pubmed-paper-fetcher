# PubMed Paper Fetcher

This project provides a command-line tool to search PubMed for papers authored by individuals affiliated with pharmaceutical or biotech companies.

## Features
- Accepts query as command-line input
- Filters non-academic authors (based on affiliation)
- Outputs CSV or prints to console
- Debug option for verbose logs

## Requirements
- Python 3.8+
- Poetry

## Installation
```bash
git clone <repo-url>
cd pubmed_paper_fetcher
poetry install
```

## Usage
```bash
poetry run get-papers-list "cancer treatment" -f results.csv -d
```

## Tools Used
- [Biopython](https://biopython.org/) for PubMed API access
- [Poetry](https://python-poetry.org/) for dependency management
- [ChatGPT](https://chat.openai.com/) for code generation and planning

---

## Project Structure
- `src/pubmed_fetcher/`: Core logic and CLI
- `README.md`: This file
- `pyproject.toml`: Poetry configuration
