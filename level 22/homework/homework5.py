def resevsed_same(word):
    if word[::-1] == word:
        return "true"
    else:
        return "false"

print(resevsed_same("wow"))