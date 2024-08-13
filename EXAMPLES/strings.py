
a = "My hovercraft is full of EELS"

print("original:", a)
print("upper:", a.upper())
print("lower:", a.lower())
print("swapcase:", a.swapcase()) # Swap upper and lower case
print("title:", a.title())  # All words are capitalized
print("e count (normal):", a.count('e'))
print("e count (lower-case):", a.lower().count('e')) # Methods can be chained. The next method is called on the object returned by the previous method. 
print("found EELS at:", a.find('EELS'))
print("found WOLVERINES at:", a.find('WOLVERINES')) # Returns -1 if substring not found

b = "graham"
print("Capitalized:", b.capitalize()) # Capitalizes first character of string, only if it is a letter

x = "spam     "
print("|" + x.rstrip() + "|")
 # .lstrip()  .strip()


data = "Joe:Blow:Pittsburgh:PA"
fields = data.split(':')
print(fields)

words = "one two three"
print(words.split())

print(len(data))

s1 = "foo"
s2 = "bar"
s3 = s1 + s2
print(s3)


#  function(obj, ...)    len(s3)
#  obj.method(obj, ...)          s3.upper()

my_data = ["one", 2, "three", 4]
print(",".join(str(x) for x in my_data))








