from isbnlib import meta
import isbnlib

from django import template

register = template.Library()


#     'title' : book['Title'],
#     'cover' : isbnlib.cover(isbn),
#     'author': book['Authors'],
#     'year'  : book['Year'],
#     'lang'  : book['Language']

@register.simple_tag
def get_title(isbn):
    book = meta(isbn)
    return book['Title']

@register.simple_tag
def get_cover(isbn):
    book = meta(isbn)
    data = isbnlib.cover(isbn)
    try:
        return data['thumbnail']
    except:
        return 'http://tri-solution.com/addons/7G20/themes/firesale_mediatheme/images/no-image.png'


@register.simple_tag
def get_authors(isbn):
    book = meta(isbn)
    x = book['Authors']
    auth_list = ''
    for i in x:
        if x[len(x)-1] is i:
            auth_list += i
        else:
            auth_list += i + ", "
    return auth_list

@register.simple_tag
def get_year(isbn):
    book = meta(isbn)
    return book['Year']
