from django import forms
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
    ["4", "The Great Gatsby"]
    ]
BOOK_CHOICES = (
    (
        "Non-Fiction", (
            ("1", "Deep Learning with Keras"),
            ("2", "Web Development with Django")
        )
    ),
    (
        "Fiction", (
            ("3", "Brave New World"),
            ("4", "The Great Gatsby")
        )
    )
)
class ExampleForm(forms.Form):
    text_input = forms.CharField()
    password_input = forms.CharField(widget=forms.PasswordInput)
    checkbox_on = forms.BooleanField()
    radio_input = forms.ChoiceField(choices=RADIO_CHOICES,widget=forms.RadioSelect)
    text_area = forms.CharField(widget=forms.Textarea)
    integer_input = forms.IntegerField()
    float_input = forms.FloatField()
    decimal_input = forms.DecimalField()
    email_input = forms.EmailField()
    date_input = forms.DateField(input_formats=["%d/m/%y", "%d/%m/%Y"])
    date_input2 = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial="Hidden Value")
    favorite_book = forms.ChoiceField(choices=BOOK_CHOICES)
    book_you_own = forms.MultipleChoiceField(choices=BOOK_CHOICES)
    hidden_input = forms.CharField(widget=forms.HiddenInput, initial='Hidden Value')


class UserLoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    integer_input = forms.IntegerField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))