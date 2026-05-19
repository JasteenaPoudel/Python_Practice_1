# Exercise 1 — Unterminated String

# Write incorrect code:

# name = "Jasteena'

# Fix it.

# name = 'Jasteena"
name = "Jasteena"
name = 'jasteena'
print(name)

# Exercise 2 — Type Error

# Try:

# 5 + "Hello"

# Then fix it.

# Exercise 3 — Invalid Syntax

# Try:

# Hello"

# Understand why quotes are necessary.

print(5 + "Hello")
# We would get typeerror because we cant add string with integer

print(str(5) + "Hello")

# Hello"

# This gives a SyntaxError because:

# The text is not properly enclosed in quotes.
# Python treats words without quotes as variable names.

# Strings must start and end with matching quotes.

print('Hello')
