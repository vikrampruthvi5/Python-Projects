"""
Goal is to use requests and bs4 to get the list of books and to be able to download them programatically.
"""

# imports
import requests
from bs4 import BeautifulSoup as bs


# from tkinter_creator import libraryGenesis


class extractor:
    # Global variables
    search = "tkinter"
    import requests
    book_list = []  # List of all books, Each book is in form of dictionary

    def print_books_data(self, list):
        if len(list) == 0:
            print("IP Address is banned. Do not relaunch the program")
            exit(0)
        else:
            print(list)
            #l = libraryGenesis()
            #l.start_process()

    def __init__(self):
        url = 'http://gen.lib.rus.ec/search.php?req=' + self.search + '&lg_topic=libgen&open=0&view=simple&res=25&phrase=0&column=def'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text

        # Converting plain text into soup
        soup = bs(plain_text, "html.parser")

        for book in soup.findAll('a', {'title': 'Gen.lib.rus.ec'}):
            href = book.get('href')
            book_data = self.download_book(href)  # Gets each book data from the method
            book_name = book_data[0]
            book_author = book_data[1]
            book_link = book_data[2]
            self.book_list.append({"name": book_name, "author": book_author, "link": book_link})
        self.print_books_data(self.book_list)

    def download_book(self, url):
        book_data = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text

        # Converting plain text into soup
        soup = bs(plain_text, "html.parser")
        for book in soup.findAll('td', {'id': 'info'}):
            plain_text = str(book)
            soup = bs(plain_text, "html.parser")

            # Title for the book
            for i in soup.findAll('h1'):
                # print(i.get_text())
                book_data.append(i.get_text())

            count = 0
            # Author, publisher, isbn for the book
            for i in soup.findAll('p'):

                # Authors
                if count is 0:
                    text = str(i.get_text())
                    auth = text.split(':')
                    # print(auth[1].strip())
                    book_data.append(auth[1].strip())
                    count += 1

            # Title for the book
            for i in soup.findAll('a'):
                # print(i.get('href'))
                book_data.append(i.get('href'))
                break
            # print()

            # print("- "*100, "\n")
            return book_data

