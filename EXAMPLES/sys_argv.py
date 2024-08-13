import sys

print(f"sys.argv: {sys.argv}\n")
print(f"{sys.argv[0] = }")

if len(sys.argv) > 1:
    animal = sys.argv[1]  # First command line parameter
    print(f"animal: {animal}")
else:
    print("no arguments")
