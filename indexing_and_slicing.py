fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

print(fruits[0], fruits[8], fruits[-1])
print()
# print(fruits[99])

#   start-at stop-before count-by

print(fruits[3:7])  # elements 3 -> 6
print(fruits[6:11])
print(fruits[0:3])
print(fruits[:3])
pos = fruits.index('banana')
print(fruits[pos:len(fruits)])
print(fruits[pos:])
print(fruits[-4:])

s = "Mississippi"
print(s[:4])
print(s[-4:])
print(s[3:7])

# for VAR in ITERABLE:      cf. foreach
#     ...use VAR...

#  for (i = 0; i < 10; i++)   NOT IMPLEMENTED IN OUR FAVORITE LANGUAGE

for fruit in fruits:
    # fruit = fruits[0]
    # fruit = fruits[1]
    # ...
    print(fruit.title())
print()

for ch in s:
    print(ch.upper())
print()

for i in range(10):
    print(i)
print()

