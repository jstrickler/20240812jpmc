fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []
for f in fruits:
    value = f.title()
    f0.append(value)
print(f"f0: {f0}\n")

#    [value for var in iterable]
f1 = [f.title() for f in fruits]   # list comprehension
print(f"f1: {f1}\n")

f2 = [f.title() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Guido', 'van Rossum', 'Python', '1956-01-31'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Ada', 'Lovelace','Babbage calculator', '1815-12-10'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]
print(f"{dobs = }\n")

products = [p[2][:3] for p in people]
print(f"{products = }\n")

dobs_gen = (p[-1] for p in people)
print(f"{dobs_gen = }\n")

for dob in dobs_gen:
    print(dob)

