import lxml.html

page = open("index.html", "r", encoding='utf-8')
p = parse(page)
print(p)