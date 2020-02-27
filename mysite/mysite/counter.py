import operator


def count(article):
    dicti = {}
    words = article.split()
    word_count = len(words)
    for word in words:
        if word in dicti:
            dicti[word] += 1
        else:
            dicti[word] = 1

    var = sorted(dicti.items(), key=operator.itemgetter(1), reverse=True)
    return var, word_count
