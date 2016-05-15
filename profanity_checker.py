def read_text():
    quotes = open("movie_quotes.txt")
    contents_file = quotes.read()
    print contents_file
    quotes.close()


read_text()