import hashlib
import webbrowser
# import antigravity
import numpy as np

k = lambda a, b, *c: a * b * c


def fn(a, b, *c):
    print(c)
    return a * b * c


(k(1, 4))
(k(1, 5, 3))
(k(1, 7, 3, 4))
(k(1, 9, 3, 4, 5))


(fn(1, 4))
(fn(1, 5, 3))
(fn(1, 7, 3, 4))
(fn(1, 9, 3, 4, 5))


# First class functions
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Header One')


def outer_fn(message):
    msg = message

    def inner_fn():
        print(message)

    return inner_fn


my_fn = outer_fn("Hi")
print(my_fn)
my_fn()


webbrowser.open("https://xkcd.com/353/")


def geohash(latitude, longitude, datedow):
    '''Compute geohash() using the Munroe algorithm.

    >>> geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
    37.857713 -122.544543

    '''
    # https://xkcd.com/426/
    h = hashlib.md5(datedow, usedforsecurity=False).hexdigest()
    p, q = [('%f' % float.fromhex('0.' + x)) for x in (h[:16], h[16:32])]
    print('%d%s %d%s' % (latitude, p[1:], longitude, q[1:]))


geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
