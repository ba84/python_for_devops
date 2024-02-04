import re

#re.match()

text = "The quick brown fox"
pattern = "quick"

search = re.search(pattern, text)

print(search)
if search:
    print("Yes", search.group())
else:
    print("No")

text2 = "The quick brown fox jumps over the lazy brown do"
pattern2 = "o"

replac = "K"

new_text = re.sub(pattern2, replac, text2)
print(new_text)