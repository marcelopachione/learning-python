# ================================================================================
# STRING FUNCTIONS
# ----------------------------------------
# Strings are one of the most used data types in Python.
# This section covers type conversion, transformations, formatting,
# indexing, slicing, cleanup, and search operations on strings.
# ================================================================================

# ---------------------------------------
# Type Conversion: Numbers to Strings
# ---------------------------------------
name = "Marcelo"
print(type(name))  # <class 'str'>

age = 24
print(type(age))   # <class 'int'>
print("Your Age is: " + str(age))  # Must convert int to str for concatenation

age = age + 5       # ➜ 29 (int)
age = str(age)      # Convert to string
print(type(age))    # ➜ <class 'str'>

# age = age + 5     # Error: Cannot add int to str

# ---------------------------------------
# String Length
# ---------------------------------------
password = "123a58478as"
print(len(password))  # ➜ 11

if len(password) < 8:
    print("Your Password is too short!")

# ---------------------------------------
# Counting Substrings
# ---------------------------------------
text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""

print(text.count("Python"))  # ➜ 2 (case-sensitive)
print(text.count("python"))  # ➜ 1
print(text.count("$"))       # ➜ 1

# ---------------------------------------
# Replacing Characters
# ---------------------------------------
price = "1234,56"
print(price.replace(",", "."))  # ➜ 1234.56

phone = "176-1234-56"
print(phone.replace("-", "/"))   # ➜ 176/1234/56
print(phone.replace("-", ""))    # ➜ 176123456

# ---------------------------------------
# Phone Number Cleanup Challenge
# ---------------------------------------
# Convert the messy phone number into a clean number format with only digits:
# Input: "+49 (176) 123-4567"
# Output: "00491761234567"

raw_number = "+49 (176) 123-4567"
clean_number = raw_number.replace(
    "+49", "0049").replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
print(clean_number)  # ➜ 00491761234567

# ---------------------------------------
# Combining Strings
# ---------------------------------------
first_name = "Michael"
last_name = "Scott"
full_name = first_name + "-" + last_name
print(full_name)  # ➜ Michael-Scott

folder = "C:/Users/Marcelo/"
file = "report.csv"
full_file_path = folder + file
print(full_file_path)  # ➜ C:/Users/Marcelo/report.csv

# ---------------------------------------
# String Formatting
# ---------------------------------------
name = "Sam"
age = 34
is_student = False

# Method 1: String Concatenation
print("My name is " + name + ", I am " + str(age) +
      " years old, and student status is " + str(is_student) + ".")

# Method 2: f-Strings (Recommended)
print(
    f"My name is {name}, I am {age} years old, and student status is {is_student}.")

# f-String Expression and Escape Example
print(f"2 + 3 = {2 + 3}")      # ➜ 2 + 3 = 5
print(f"{{This is me}}")       # ➜ {This is me}

# ---------------------------------------
# Splitting Strings
# ---------------------------------------
stamp = "2026-09-20 14:30"
print(stamp.split(" "))  # ➜ ['2026-09-20', '14:30']

csv_file = "1234,Max,USA,1970-10-05,M"
print(csv_file.split(","))  # ➜ ['1234', 'Max', 'USA', '1970-10-05', 'M']

# ---------------------------------------
# Repeating Strings
# ---------------------------------------
print("ha" * 3)              # ➜ hahaha
print("=" * 30)              # ➜ ==============================

# ---------------------------------------
# Indexing and Slicing
# ---------------------------------------
text = "Python"

print(text[0])    # ➜ P (first character)
print(text[-6])   # ➜ P (same as above)
print(text[5])    # ➜ n (last character)
print(text[-1])   # ➜ n
print(text[3])    # ➜ h

date = "2026-09-20"
print(date[0:4])  # ➜ 2026 (year)
print(date[:4])   # ➜ 2026
print(date[5:7])  # ➜ 09 (month)
print(date[8:])   # ➜ 20 (day)
print(date[-2:])  # ➜ 20

# ---------------------------------------
# Whitespace Cleanup
# ---------------------------------------
text = " Engineering".lstrip()
print(text)  # ➜ "Engineering"

text = "Engineering ".rstrip()
print(text)  # ➜ "Engineering"

text = "  Engineering ".strip()
print(text)  # ➜ "Engineering"

text = "Data Engineering".strip()
print(text)  # ➜ "Data Engineering"

text = "###Abc###".strip("#")
print(text)  # ➜ "Abc"

# ---------------------------------------
# Case Conversion
# ---------------------------------------
text = "python PROGRAMMING"
print(text.lower())  # ➜ python programming
print(text.upper())  # ➜ PYTHON PROGRAMMING

search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)  # ➜ True

# ---------------------------------------
# Search Functions
# ---------------------------------------
phone = "+48-176-12345"
print(phone.startswith("+49"))         # ➜ False

email = "marcelo@outlook.com"
print(email.endswith("gmail.com"))     # ➜ False

file = "data_backup.csv"
print(file.endswith(".csv"))           # ➜ True

print("@" in email)                    # ➜ True

url = "https://api.company.com/v1/data"
print("/api" in url)                   # ➜ True

# ---------------------------------------
# Partial Extraction Using find()
# ---------------------------------------
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[phone1.find("-") + 1:])  # ➜ 176-12345
print(phone2[phone2.find("-") + 1:])  # ➜ 654-16548
print(phone3[phone3.find("-") + 1:])  # ➜ 654-16548

print(phone1.find("-"))              # ➜ 3


# ---------------------------------------
# String Cleanup Challenge
# ---------------------------------------
# Input:  "968-Maria, ( D@ta Engineer );; 27y"
# Goal:   name: maria | role: data engineer | age: 27
