import isbnlib

#isbn = '9787564100474'
isbn1 = '9781118148693'

def test(isbnx):
    book = isbnlib.meta(isbnx)
    data = isbnlib.cover(isbnx)
    try:
        return data['thumbnail']
    except:
        print("Handled error ")


print(type(test(isbn1)))
