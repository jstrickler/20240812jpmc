
# scope
# local -> nonlocal -> global -> builtin

x = 5
print(x)

def spam(p1):
    x = 100  # local
    print(f"{x = }")
    
    r = 123   # local

    def foo():
        print(x)   # nonlocal

    return x

a = spam(x)
x = spam(x)

print(f"{x = }")


def ham():
    r = "abc"  # local

# print(animal)
