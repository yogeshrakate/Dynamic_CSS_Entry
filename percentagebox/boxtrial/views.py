from django.shortcuts import render

# Create your views here.
def home(request):
    px_size = 400
    return render(request, 'index.html', {'px_size':px_size})