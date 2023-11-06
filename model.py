import wikipedia

def get_wikipedia_info(query):
    # Get the information from Wikipedia.
    try:
        return wikipedia.summary(query, sentences=1)
    except wikipedia.exceptions.PageError:
        return "No information found for \"" + query + "\"."

choise = input('Enter what do you want to know >')

# Get the information about the United States.
info = get_wikipedia_info(choise)

# Display the information to the user.
print(info)
