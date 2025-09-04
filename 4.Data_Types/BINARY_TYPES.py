print("=== Python Data Types Tutorial ===")


#  BINARY TYPES: bytes, bytearray, memory
# Handles binary data or memory-efficient operations.
print("\n=== bytes, bytearray, memory ===")

# Bytes: immutable binary data
data = b"hi"
print(f"Bytes: {data}")  # Output: b'hi'

# Bytearray: mutable binary data
mutable_data = bytearray(b"hi")
mutable_data[0] = 72  # Change 'h' to 'H'
print(f"Bytearray: {mutable_data}")  # Output: bytearray(b'Hi')

# Memory: view of byte data
mem = memoryview(b"hi")
print(f"Memory first byte: {mem[0]}")  # Output: 104 (ASCII for 'h')