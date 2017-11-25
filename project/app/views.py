from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_me': 'Coming from views.py'}
    return render(request, 'app/index.html', context=my_dict)
