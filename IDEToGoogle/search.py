from googlesearch import search
#This imports the google libraries. The search would'nt happen without the google library. 
query=" Python Queries "
#This is basically the "search bar". The query is the part where you paste in your text and give the IDE/Terminal what to search
for url in search(query):
    print(url)
#This command prints out the results in the terminal. "For URL" extracts the URL from the search query.
#"print(url)" pastes the search results into the terminal