print("=== Python Variables Tutorial ===")

# 📌 WHAT IS A VARIABLE?
# A variable is like a labeled box that stores data.
# - Name: the label (e.g., 'age')
# - Value: the data inside (e.g., 21)
# Python is dynamically typed, so no need to specify the data type.

print("\n=== Creating Variables ===")
# Create variables with different data types
name = "Hamim"          # String: stores text
age = 21                # Integer: whole number
height = 5.9            # Float: decimal number
is_student = True       # Boolean: True or False

# Print variables to see their values
print(f"Name: {name}")          # Output: Name: Hamim
print(f"Age: {age}")            # Output: Age: 21
print(f"Height: {height}")      # Output: Height: 5.9
print(f"Student? {is_student}") # Output: Student? True

# 🎯 NAMING RULES
# - Allowed: letters, numbers, underscores (_)
# - Must start with: letter or underscore
# - Cannot start with: number
# - Cannot use: special characters (!, @, #) or reserved keywords (if, while)

print("\n=== Valid and Invalid Variable Names ===")
# Valid names
user_name = "Alex"      # Uses underscore
score2 = 95             # Uses number after letter
_temp = 25.0            # Starts with underscore
print(f"Valid names: {user_name}, {score2}, {_temp}")

# Invalid names (uncomment to see errors)
# 2score = 95           # Error: cannot start with number
# user@name = "Alex"    # Error: special character @
# if = "test"           # Error: reserved keyword

# 🔄 DYNAMIC TYPING
# Python allows changing a variable's value and type anytime.

print("\n=== Dynamic Typing ===")
age = 21                # Integer
print(f"Age as integer: {age}, Type: {type(age)}")  # Output: Age as integer: 21, Type: <class 'int'>
age = "Twenty-one"      # Now a string
print(f"Age as string: {age}, Type: {type(age)}")  # Output: Age as string: Twenty-one, Type: <class 'str'>

# 🔍 CHECKING VARIABLE TYPES
# Use type() to check the data type of a variable.

print("\n=== Checking Types ===")
x = 42
y = "Python"
z = 3.14
print(f"Type of {x}: {type(x)}")  # Output: Type of 42: <class 'int'>
print(f"Type of {y}: {type(y)}")  # Output: Type of Python: <class 'str'>
print(f"Type of {z}: {type(z)}")  # Output: Type of 3.14: <class 'float'>

# 🌟 VARIABLE SCOPE
# Variables can be local (inside a function) or global (outside).

print("\n=== Variable Scope ===")
global_var = "I'm global!"  # Global: accessible everywhere

def my_function():
    local_var = "I'm local!"  # Local: only accessible in this function
    print(local_var)          # Output: I'm local!
    print(global_var)         # Output: I'm global!

my_function()
print(global_var)             # Output: I'm global!
# print(local_var)            # Error: local_var is not defined

# 🔄 TYPE CONVERSION
# Convert between types using int(), str(), float(), etc.

print("\n=== Type Conversion ===")
number = "42"              # String
num_int = int(number)      # Convert to integer
num_float = float(number)  # Convert to float
print(f"String to int: {num_int + 8}")    # Output: 50
print(f"String to float: {num_float + 0.5}")  # Output: 42.5

text = str(100)            # Convert number to string
print(f"Number to string: {text + ' points'}")  # Output: 100 points

# 🛠 BEST PRACTICES
# - Use descriptive names (e.g., total_price instead of x)
# - Use snake_case for variable names
# - Avoid excessive global variables
# - Comment complex logic

print("\n=== Best Practices Example ===")
item_price = 50.00      # Descriptive name for price
tax_rate = 0.1          # 10% tax rate
total_price = item_price * (1 + tax_rate)  # Calculate total with tax
print(f"Total price with tax: ${total_price}")  # Output: Total price with tax: $55.0