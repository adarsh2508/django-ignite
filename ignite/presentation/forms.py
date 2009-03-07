from django.forms import ModelForm
from ignite.presentation.models import Presentation

class PresentationForm(ModelForm):
    class Meta:
        model = Presentation
        exclude = ('slug', 'created',)

