from django.shortcuts import render, redirect, get_object_or_404
from .models import Publisher
from django.contrib import messages
from .forms import ExampleForm, UserLoginForm, NewsletterSignupForm, \
    OrderForm, ExamplePlaceholderForm, PublisherForm, SearchForm


# Create your views here.
def index(request):
    context = Publisher.objects.all()
    return render(request, "index.html", {"context" : context})

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


def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk=pk)
    else:
        publisher = None
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            updated_publisher = form.save()
            if publisher is None:
                messages.success(request, "Publisher  '{}' was created.".format(updated_publisher))
            else:
                messages.success(request, "Publisher '{}' was updated.".format(updated_publisher))
            return redirect("publisher_edit", updated_publisher.pk)
            
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "publisher.html", {"method": request.method, "form": form})
