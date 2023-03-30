import re

text = "I like learning and programming!"
match = re.search('ing', text)  # to find a single pattern
print(match.group())
print(match.span())  # to get the start and end position

matches = re.findall('ing', text)

for m in matches:
    print(m)  # prints multiple matches

for match in re.finditer('ing', text):
    print(match)  # can access individual match object w


# pattern like search
pattern = r'(\d{3})-(\d{3})-(\d{4})'

search_text = "My phone number is 779-529-0789"

match = re.search(pattern, search_text)
print(match.group())
print(match.group(1))


# exclusion
data = "Hello! How are you, Chinmay?"
pattern_exclude = r'[^,! ?]+'  # '^' to exclusion
list_of_words = re.findall(pattern_exclude, data)
cleaned_data = ' '.join(list_of_words)
print(cleaned_data)
