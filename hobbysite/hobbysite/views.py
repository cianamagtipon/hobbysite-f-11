from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html', {'message': 'Welcome to the Homepage!'})


def commissions_home(request):
    return render(request, 'commissions_home.html')

