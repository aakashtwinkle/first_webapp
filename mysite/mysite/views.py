from django.shortcuts import render
from . import counter
from . import name

def home(request):
    return render(request, 'index.html', {'key1': 'value1'})


def result(request):
    age = request.GET['user_age']
    namee = request.GET['name']
    article = request.GET['article']
    name_age=name.name(age, namee)
    var, word_count = counter.count(article)
    return render(request, 'result.html', {'age_name': name_age, 'article': article, 'word_count': word_count,
                                           'dicti': var})
