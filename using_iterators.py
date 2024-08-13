fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

rev_fruits = reversed(fruits)
print(rev_fruits)
for fruit in rev_fruits:
    print(fruit, end=" ")
print("\n")

# for (i = 0; i < len(fruits); i++) {
#      printf(fruits[i])
# }

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(list(enumerate(fruits)))


