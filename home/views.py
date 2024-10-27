from django.shortcuts import render
# Create your views here.
def home(request):
    print('home')
    context = {
        'text': 'olá home'
    }
    return render(
        request, 
        'home/home.html',
        context
        )