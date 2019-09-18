# import statements
from Book import book


class Shelf:
    shelves = {}

    def add_book(self, b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price):
        dict_key = str.upper(b_name[:2])
        if dict_key not in self.shelves.keys() or len(self.shelves.keys()) == 0:
            btemp: book = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
            self.shelves[str.upper(dict_key)] = [btemp]
        else:
            is_isbn_present = False
            for i in self.shelves.get(dict_key):
                if i.b_isbn == b_isbn:
                    is_isbn_present = True
                    break
            if is_isbn_present:
                i.incrementCounter()
            else:
                btemp: book = book(b_isbn, b_name, b_lang, b_origin, b_authors, b_version, b_price)
                self.shelves.get(dict_key).append(btemp)

    def get_books(self):
        ret = list()
        #print("\nPrinting all books\n" + "*" * 18)
        shelves = self.shelves.keys()
        for tmp_shelf in shelves:
            for tmp_book in self.shelves.get(tmp_shelf):
                #print("Book : {}\tISBN : {}\tCount : {}".format(tmp_book.b_name, tmp_book.b_isbn, tmp_book.b_counter))
                ret.append(str("{}, {}, {}".format(tmp_book.b_name, tmp_book.b_isbn, tmp_book.b_counter)).split(','))
        return ret

    def search_isbn(self, b_isbn):
        shelves = self.shelves.keys()
        for tmp_shelf in shelves:
            for tmp_book in self.shelves.get(tmp_shelf):
                if b_isbn is tmp_book.b_isbn:
                    # Print book details and exit
                    print("Book Name \t: {} {}\n"
                          "ISBN \t\t: {}\n"
                          "Location \t: {}\n"
                          "Language \t: {}\n"
                          "Pub Origin \t: {}\n"
                          "Authors \t: {}\n"
                          "Price \t\t: {}\n"
                          "Count \t\t: {}"
                          .format(tmp_book.b_name, tmp_book.b_version, tmp_book.b_isbn, tmp_shelf, tmp_book.b_lang,
                                  tmp_book.b_origin, tmp_book.b_authors, tmp_book.b_price, tmp_book.b_counter))



