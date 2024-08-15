import os

def say_hello() -> str:  # Function takes no parameters
    print("Hello, world")
    print()
    # If no return statement, return None


say_hello()  # Call function (arguments, if any, in () )
x: str = say_hello()
print(f"{x = }")

x = 50
print(f"{x = }")

def get_hello():
    return "Hello, world"  # Function returns value


h = get_hello()  # Store return value in h
print(h)
print()


def sqrt(num: int | float) -> float:  # Function takes exactly one argument
    return num ** .5


m = sqrt(1234)  # Call function with one argument
n = sqrt(2)
p = sqrt("abc")



print(f"m is {m:.3f} n is {n:.3f}")


def grep(search_term, *file_paths, show_file_name=False):
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    if show_file_name:
                        print(file_path, end=": ")
                    print(raw_line.rstrip())

def spam(p1, p2, *, p3, p4): 
    pass

spam(5, 10, p3=15, p4=20)



grep('bird', '../DATA/alice.txt', '../DATA/parrot.txt', show_file_name=True)


