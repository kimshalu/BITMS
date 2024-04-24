import re

# Search for a pattern in a string
text = "The quick brown fox jumps over the lazy dog."
pattern = r"fox"
match = re.search(pattern, text)
if match:
    print("Pattern '{}' found at index {}.".format(pattern, match.start()))
else:
    print("Pattern '{}' not found.".format(pattern))

# Find all occurrences of a pattern in a string
text = "The cat and the hat sat on the mat."
pattern = r"cat"
matches = re.findall(pattern, text)
print("Occurrences of pattern '{}' found: {}".format(pattern, matches))

# Replace all occurrences of a pattern in a string
text = "I love cats, but I also love dogs."
pattern = r"cats"
replacement = "dogs"
new_text = re.sub(pattern, replacement, text)
print("Original text:", text)
print("Text after replacement:", new_text)

# Split a string based on a pattern
text = "apple,banana,orange,grape"
pattern = r","
parts = re.split(pattern, text)
print("Splitting the text based on pattern '{}': {}".format(pattern, parts))
