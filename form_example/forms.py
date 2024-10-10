from django import forms
from django.core.exceptions import ValidationError

RADIO_CHOICES = (
    ("Value One", "Value One"),
    ("Value Two", "Value Two"),
    ("Value Three", "Value Three"),
    ("Value Four", "Value Four"),
)
BOOK_CHOICES_LIST = [
    ["1", "Deep Learning with Keras"],
    ["2", "Web Development with Django"],
    ["3", "Brave New World"],
    ["4", "The Great Gatsby"],
]
BOOK_CHOICES = (
    (
        "Non-Fiction",
        (("1", "Deep Learning with Keras"), ("2", "Web Development with Django")),
    ),
    ("Fiction", (("3", "Brave New World"), ("4", "The Great Gatsby"))),
)

class OrderForm(forms.Form):
    item_a = forms.IntegerField(min_value=0, max_value=100)
    item_b = forms.IntegerField(min_value=0, max_value=100)
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("item_a", 0) + \
            cleaned_data.get("item_b", 0) > 100:
                self.add_error(None, "The total number of items must be 100 or less")

def validate_lowercase(value):
    if value.lower() != value:
        raise ValidationError("{} is not lowercase.".format(value))
    return value.lower()


class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    # date_input = forms.DateField(input_formats=["%d/m/%y", "%d/%m/%Y"])
    date_input = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    book_you_own = forms.MultipleChoiceField(required=False, choices=BOOK_CHOICES)
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")

    def clean_text_input(self):
        value = self.cleaned_data["text_input"]
        return value.lower()


class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    integer_input = forms.IntegerField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))


class NewsletterSignupForm(forms.Form):
    signup = forms.BooleanField(label="Sign up to newsletter?", required=True)
    email = forms.EmailField(
        help_text="Enter your email address to subscribe", required=False
    )

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data["signup"] and not cleaned_data.get("email"):
            self.add_error(
                "email",
                "Your email address is \
            required if signing up for the newsletter.",
            )
