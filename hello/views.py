from django.shortcuts import render


def hello(request):
    return render(request, 'index.html', context={'name':"tousif, Docker serving your applocation"})
