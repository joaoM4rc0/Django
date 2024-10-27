from django.shortcuts import render
# Create your views here.
def blog(request):
    print('blog')
    context = {
        'text': 'olá blog'
    }
    return render(
            request, 
            'blog/index.html',
            context
        )
def exemplo(request):
    print('exemplo')
    context = {
        'text': 'olá exemplo',
        'title': 'site de exemplo -'
    }
    return render(
        request, 
        'blog/exemplo.html',
        context
    )