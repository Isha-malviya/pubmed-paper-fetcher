import argparse
from pubmed_fetcher.fetcher import fetch_pubmed_results, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="Query string to search PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    args = parser.parse_args()

    results = fetch_pubmed_results(args.query, debug=args.debug)
    if not results:
        print("No papers found with non-academic affiliations.")
        return

    if args.file:
        save_to_csv(results, args.file)
        print(f"Results saved to {args.file}")
    else:
        for row in results:
            print(row)

if __name__ == "__main__":
    main()