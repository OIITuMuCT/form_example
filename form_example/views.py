from django.shortcuts import render, redirect
from .forms import ExampleForm, UserLoginForm


# Create your views here.
def form_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = ExampleForm()

    return render(
        request, "form_example.html", {"method": request.method, "form": form}
    )


def form_django_example(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            # for name in request.POST:
            #     print("{}:{}".format(name, request.POST.getlist(name)))
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    #     return render(
    #         request, "form_django.html", {"method": request.method, "form": form}
    #     )
    else:
        form = ExampleForm()
    return render(request, "form_django.html", {"method": request.method, "form": form})


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
    return render(request, "form_login.html", {"method": request.method, "form": form})
