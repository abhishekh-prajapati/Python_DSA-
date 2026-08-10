def iscaptal(word):
    if word == word.upper():
        return True
    else:
        return False
word = "g"
saloni = "SALONI"
abhi = "Abhi"

print(iscaptal(word))
print(iscaptal(saloni))
print(iscaptal(abhi))
