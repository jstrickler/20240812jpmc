person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(person[0], person[1])

first_name, last_name, product, dob = person   # iterable unpacking

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
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
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]
print(type(people[0]), people[0])
print(people[0][0])
print(people[0][0][0])
print()

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # ...
    print(first_name, last_name, product, dob)
print()


print("spam" * 10)

flags = [1, 2, 3] * 5
print(flags)




