from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html', {'message': 'Welcome to the Homepage!'})