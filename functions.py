def add_quote(quotes, filename):
    new_quote = input("Enter a new quote: ")
    quotes.append(new_quote)
    
    with open(filename, 'a') as file:
        file.write(new_quote + '\n')
