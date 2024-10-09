from django.shortcuts import render, redirect
from .forms import ExampleForm, UserLoginForm

# Create your views here.
def form_example(request):
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, 'form_example.html', {"method": request.method})

def form_django_example(request):
    form = ExampleForm()
    for name in request.POST:
        print("{} : {}".format(name, request.POST.getlist(name)))
    return render(request, 'form_django.html', {'form': form})

def user_login(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            for name in request.POST:
                print("{} : {}".format(name, request.POST.getlist(name)))
        return render(request, "success_login.html")

    else:
        form = UserLoginForm()
    for name in request.POST:
        print("{} : {}".format(name, request.POST.getlist(name)))
    return render(request, 'form_login.html',  {"method": request.method, "form": form})

def success(request):
    return render(request)