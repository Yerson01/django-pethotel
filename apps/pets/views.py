from django.shortcuts import render


def add_pet(request):
    return render(request, 'pages/add_pet.html')
