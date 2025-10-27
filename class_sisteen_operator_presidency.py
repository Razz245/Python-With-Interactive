# Arithmetic precedence
result = 2 + 3 * 4
print(result)  # 14, not 20, because * before +

# Using parentheses
result = (2 + 3) * 4
print(result)  # 20

# Logical precedence
a = True
b = False
c = True
print(a or b and c)      # True, because 'and' evaluated first
print((a or b) and c)    # True, parentheses change the order

#AND gate
"""
True AND True   → True
True AND False  → False
False AND True  → False
False AND False → False
"""
#OR gate
"""
True OR True    → True
True OR False   → True
False OR True   → True
False OR False  → False

"""
#NOT gate
"""
NOT True  → False
NOT False → True
NOR = NOT (OR) → OR gate এর output উল্টো
"""


# AND Gate
and_result = a and b and c
print("AND result:", and_result)  # False, কারণ b False

# OR Gate
or_result = a or b or c
print("OR result:", or_result)    # True, কারণ a True

# NOR Gate (NOT OR)
nor_result = not (a or b or c)
print("NOR result:", nor_result)  # False, কারণ a True → OR True → NOR False
