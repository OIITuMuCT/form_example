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


def validate_email_domain(value):
    if value.split("@")[-1].lower() != "example.com":
        raise ValidationError("The email address must be on the domain example.com")


class OrderForm(forms.Form):
    # text_input = forms.CharField(
    #     widget=forms.TextInput(attrs={"placeholder": "Text Placeholder"})
    # )
    magazine_count = forms.IntegerField(min_value=0, max_value=80)
    book_count = forms.IntegerField(min_value=0, max_value=50)
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False, validators=[validate_email_domain])

    def clean_email(self):
        return self.cleaned_data["email"].lower()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["send_confirmation"] and not cleaned_data.get("email"):
            self.add_error(
                "email",
                "Please enter an email address to receive the confirmation message.",
            )
        elif cleaned_data.get("email") and not cleaned_data["send_confirmation"]:
            self.add_error(
                "send_confirmation",
                "Please check this if you want to receive a confirmation email.",
            )
        item_total = cleaned_data.get("magazine_count", 0) + cleaned_data.get(
            "book_count", 0
        )
        if item_total > 100:
            self.add_error(None, "The total number of items must be 100 or less.")


def validate_lowercase(value):
    if value.lower() != value:
        raise ValidationError("{} is not lowercase.".format(value))
    return value.lower()


class ExampleForm(forms.Form):
    text_input = forms.CharField(
        widget=forms.TextInput
    )
    text_field = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Text placeholder"})
    )
    password_input = forms.CharField(min_length=8, widget=forms.PasswordInput)
    password_field = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password Placeholder"})
    )
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES, widget=forms.RadioSelect)
    text_area = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Text Area Placeholder"})
    )
    integer_input = forms.IntegerField(min_value=1, max_value=10)
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField(max_digits=5, decimal_places=3)
    email_input = forms.EmailField()
    email_field = forms.EmailInput(attrs={"placeholder": "Email Placeholder"})
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


class ExamplePlaceholderForm(forms.Form):
    text_field = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Text Placeholder"}))
    password_field = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password Placeholder"}))
    email_field = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email Placeholder"}))
    text_area = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Text Area Placeholder"}))