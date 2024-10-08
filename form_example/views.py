from django.shortcuts import render

# Create your views here.
def form_example(request):
    return render(request, 'form_example.html')