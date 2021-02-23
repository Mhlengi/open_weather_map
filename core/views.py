from django.shortcuts import render


def index(request):
    template_variables = {'a': 1, 'b': 2}
    return render(request, 'core/index.html', template_variables)
