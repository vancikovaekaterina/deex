import urllib.parse

# Define the base URL
base_url = "https://example.com/search"

# Define the query parameter 'q' and additional query parameters
query = "python programming"
query_params = {
    "page": 1,
    "sort": "relevance",
    "lang": "en"
}

# Merge the dictionaries and encode the query parameters
full_query_params = {**{"q": query}, **query_params}
encoded_query = urllib.parse.urlencode(full_query_params, quote_via=urllib.parse.quote)

# Construct the full URL
full_url = f"{base_url}?{encoded_query}"

print(full_url)
