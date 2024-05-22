from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def delete(request):
    return render(request, 'delete.html')

def update(request):
    return render(request, 'update.html')

def insert(request):
    return render(request, 'insert.html')

