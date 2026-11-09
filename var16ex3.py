def compress(sentence):
    unique = []
    result = []

    for word in sentence.lower().split():
        try:
            pos = unique.index(word)
        except ValueError:
            unique.append(word)
            pos = len(unique) - 1
        result.append(str(pos))

    return "".join(result)
