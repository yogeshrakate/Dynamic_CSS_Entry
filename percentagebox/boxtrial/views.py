from django.shortcuts import render

# Create your views here.
def home(request):
    px_sizes = 4
    px_size_list = [200,300,400,500]
    return render(request, 'index.html', {'px_sizes':px_sizes, 'px_size_list':px_size_list})
