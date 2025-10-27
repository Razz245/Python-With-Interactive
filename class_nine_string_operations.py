
# Class Nine: String Operations, Indexing & Slicing
print("=== String Operations: Indexing & Slicing ===\n")

# Sample string
text = "PythonWithInteractive"

# 1️⃣ Indexing
print("Original String:", text)
print("First character:", text[0])
print("Last character:", text[-1])
print("Fifth character:", text[4])

# 2️⃣ Slicing
print("\n--- Slicing Examples ---")
print("First 6 characters:", text[:6])
print("Characters from index 6 to 10:", text[6:11])
print("Last 5 characters:", text[-5:])
print("Every 2nd character:", text[::2])
print("Reverse string:", text[::-1])

# 3️⃣ String Operations
print("\n--- String Operations ---")
greet = "Hello"
name = "Rajib"
combined = greet + " " + name
print("Concatenation:", combined)
print("Repetition:", "Ha! " * 3)
print("Check membership:", "Python" in text)
print("Length of string:", len(text))

# 4️⃣ Modifying case
print("\n--- Case Modification ---")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
