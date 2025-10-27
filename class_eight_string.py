# === Class Eight: String in Python ===
# Developed by: Rajib Sharma
# Date: 27 October 2025

# ১️⃣ স্ট্রিং লেখার বিভিন্ন উপায়
single_quote = 'Hello, I am learning Python!'
double_quote = "This is also a string."
triple_quote = '''This is
a multi-line
string.'''

print(single_quote)
print(double_quote)
print(triple_quote)

# ২️⃣ স্ট্রিং কনক্যাটেনেশন (Joining)
first_name = "Rajib"
last_name = "Sharma"
full_name = first_name + " " + last_name
print("\nFull Name:", full_name)

# ৩️⃣ স্ট্রিং রিপিট করা
laugh = "Ha " * 3
print("\nLaugh Example:", laugh)

# ৪️⃣ স্ট্রিং ফরম্যাটিং (3 Methods)
name = "Rajib"
age = 25

# Old style (% formatting)
print("\nUsing %% formatting: My name is %s and I am %d years old." % (name, age))

# New style (str.format)
print("Using str.format(): My name is {} and I am {} years old.".format(name, age))

# f-string (Python 3.6+)
print(f"Using f-string: My name is {name} and I am {age} years old.")

# ৫️⃣ স্ট্রিং ইনডেক্সিং ও স্লাইসিং
word = "Python"
print("\nFirst letter:", word[0])
print("Last letter:", word[-1])
print("Slice [0:4]:", word[0:4])
print("Reverse:", word[::-1])

# ৬️⃣ কিছু দরকারি স্ট্রিং ফাংশন
sentence = "  Python is Fun!  "
print("\nOriginal:", sentence)
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title Case:", sentence.title())
print("Strip:", sentence.strip())
print("Replace:", sentence.replace("Fun", "Powerful"))
print("Split:", sentence.split())

# ৭️⃣ Escape Characters
print("\nUsing escape characters:")
print("He said, \"Python is awesome!\"")
print('It\'s a great language.')
print("Line1\nLine2\nLine3")
