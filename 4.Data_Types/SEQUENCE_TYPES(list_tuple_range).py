print("=== Python Data Types Tutorial ===")


#  SEQUENCE TYPES: list, tuple, range
# Stores ordered collections or number sequences.

print("\n=== list, tuple, range ===")

# List: mutable, ordered collection
fruits = ["apple", "banana", "orange"]

print(f"List: {fruits}")  # Output: ['apple', 'banana', 'orange']
print(f"First: {fruits[0]}")  # Output: apple

# Tuple: immutable, ordered collection
point = (5, 10)
print(f"Tuple: {point}, Y-coordinate: {point[1]}")  # Output: 10

# Range: number sequence for loops
print("Range (0-2):", end=" ")
for i in range(3):
    print(i, end=" ")  # Output: 0 1 2
print()