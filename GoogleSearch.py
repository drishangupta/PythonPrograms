import googlesearch

def google_search(query, num_results=5):
    search_results = googlesearch.search(query, stop=num_results, pause=2.0)
    return search_results

if __name__ == "__main__":
    search_query = input("Enter What You Want To Search for")
    top_5_results = google_search(search_query)

    print(f"Top 5 results for '{search_query}':")
    for i, result in enumerate(top_5_results, 1):
        print(f"{i}. {result}")



