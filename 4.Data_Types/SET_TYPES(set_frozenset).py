print("=== Python Data Types Tutorial ===")


# 🧩 SET TYPES: set, frozenset
# Stores unique items, mutable (set) or immutable (frozenset).
print("\n=== set, frozenset ===")

# Set: unique, unordered items
numbers = {1, 2, 2, 3}  # Duplicate 2 ignored
print(f"Set: {numbers}")  # Output: {1, 2, 3}

numbers.add(4)  # Add item
print(f"Updated: {numbers}")  # Output: {1, 2, 3, 4}

# Frozenset: immutable set
frozen = frozenset([1, 2, 2, 3])
print(f"Frozenset: {frozen}")  # Output: frozenset({1, 2, 3})