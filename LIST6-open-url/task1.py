import crawl

soup = crawl.crawl("https://www.ii.uni.wroc.pl/~marcinm/", 13, crawl.action)
soup2 = crawl.crawl("https://pl.wikipedia.org/wiki/Python", 3, crawl.action)
soup3 = crawl.crawl('https://www.ii.uni.wroc.pl/~marcinm/dyd/python/', 3, crawl.action) 

print("\n\nII.UNI.WROC.PL/~MARCINM\n\n")
for i in soup:
    print(i)
print("\n\nWIKIPEDIA\n\n")
for i in soup2:
    print(i)
print("\n\nDYD/PYTHON/\n\n")
for i in soup3:
    print(i)


"""
g1, g2- generator

def sum (g1, g2):
    for i in g1:
        yield i
    for i in g2:
        yield i

def sum (g1, g2):
    yield from g1
    yield from g2

def f():
    yield <...>
    for c in child(<...>):
        yield from f(...)

"""