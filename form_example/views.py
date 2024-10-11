from django.shortcuts import render, redirect
from .forms import ExampleForm, UserLoginForm, NewsletterSignupForm, OrderForm, ExamplePlaceholderForm


# Create your views here.
def index(request):
    
    return render(request, "index.html")

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

def newsletter(request):
    if request.method == "POST":
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
    else:
        form = NewsletterSignupForm()
    return render(request, 'newsletter.html', {"method": request.method,"form": form})

def order(request):
    initial = {"email":"user@example.com"}
    form = OrderForm(request.POST, initial=initial)
    if form.is_valid():
        for name, value in form.cleaned_data.items():
            print("{}: ({}) {}".format(name, type(value), value))

    else:
        form = OrderForm(initial=initial)

    return render(request, "order_form.html", {"method": request.method, "form": form})

def example_placeholder(request):
    initial = {"text_field": "Text Value", "email_field": "user@example.com"}
    if request.method == "POST":
        
        form = ExamplePlaceholderForm(
            request.POST,
            initial=initial,
        )
        if form.is_valid():
            for name, value in form.cleaned_data.items():
                print("{}: ({}) {}".format(name, type(value), value))
            print("Форма прошла валидацию успешно")
    else:
        form = ExamplePlaceholderForm(initial=initial)
    return render(request, "form_exp_place.html", {"method": request.method, "form": form})
