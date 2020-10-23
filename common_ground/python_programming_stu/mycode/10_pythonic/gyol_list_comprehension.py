books = list()

books.append({'title': 'aaa', 'when': '11111', 'company': 'AAAAA', 'pages': 200, 'recommend': False})
books.append({'title': 'bbb', 'when': '22222', 'company': 'BBBBB', 'pages': 584, 'recommend': True})
books.append({'title': 'ccc', 'when': '33333', 'company': 'AAAAA', 'pages': 296, 'recommend': True})
books.append({'title': 'ddd', 'when': '44444', 'company': 'BBBBB', 'pages': 526, 'recommend': False})
books.append({'title': 'eee', 'when': '55555', 'company': 'CCCCC', 'pages': 246, 'recommend': True})

#print(books)
t_list = list()
c_list = set()
p_list = []
r_list = []

for b in books:
#    print(type(t), t['title'])
    t_list.append(b['title'])
    c_list.add(b['company'])
    if b['pages'] > 250:
        p_list.append(b['title'])
    if b['recommend'] == 1:
        r_list.append(b['title'])

print(t_list)
print(sorted(c_list))
print(p_list)
print(r_list)

# List Comprehension 서타일
print()
t_list = [b['title'] for b in books]
c_list = set(b['company'] for b in books)
p_list = [b['title'] for b in books if b['pages'] > 250]
r_list = [b['title'] for b in books if b['recommend'] == 1]
pages = sum(b['pages'] for b in books)

print(t_list)
print(sorted(c_list))
print(p_list)
print(r_list)
print(pages)