from django.forms import ModelForm
from . import models

# Create the form class.
class BookForm(ModelForm):
    class Meta:
        model = models.WebNovel
        fields = ["name", "cover"]
