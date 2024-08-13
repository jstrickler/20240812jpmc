s1 = "spam\n"   # all 4 are the same
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

#  """ use a null string ("") for empty strings"""
print("Guido's the ex-BDFL of Python")
print()
print('Guido is the ex-"BDFL" of Python')
print()
print("""Guido's the ex-"BDFL" of Python""")

query = """
select *
from customers
where state = 'ID'
"""

regex = r"xx\bthe\b"
print(regex)

print(len("spam\n"))
print(len(r"spam\n"))

