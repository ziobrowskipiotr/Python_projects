import re

with open('zadanie2.csv', 'r') as f:
    new_text = ""
    for line in f:
        line = line.strip()
        if not re.match(r"^\d+,?$", line) and line.startswith(tuple("0123456789")):
            new_text += line + "\n"

    liczby = r"\d+"
    id = re.findall(liczby, new_text)

    for i in range(len(id)):
        id[i] = int(id[i])

    for i in range(len(id)):
        for j in range(len(id)):
            if id[i] == id[j] and i != j:
                id[j] += 1

    for i in range(len(id)):
        id[i] = str(id[i])

    new_text = re.sub(liczby, lambda x: id.pop(0), new_text)

print(new_text)
new_text = new_text.lower()
print(new_text)

word_list = re.findall(r'\b\w+\b|[.,]', new_text)

znaki = []
for word in word_list:
    chars = list(word)
    znaki.append(chars)

print(znaki)
print(len(new_text))

i = 0
while i < len(znaki):
    j = 0
    while j < len(znaki[i]) - 1:
        if ord(znaki[i][j]) == ord(znaki[i][j+1]) + 1 or ord(znaki[i][j+1]) == ord(znaki[i][j]) - 1:
            del znaki[i][j]
        else:
            j += 1
    if not znaki[i]:
        del znaki[i]
    else:
        i += 1

new_txt = ""
for znak in znaki:
    if znak == ',':
        new_txt += "".join(znak)
    else:
        new_txt += "".join(znak) + " "

print(new_txt)

tekst = ""
for line in new_txt:
    if not re.match(r"^\d+,?$", line) and line.startswith(tuple("0123456789")):
        tekst += line + "\n"

#print(tekst)