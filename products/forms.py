from django import forms
from .models import Collectable, Platform


class CollectableForm(forms.ModelForm):

    class Meta:
        model = Collectable
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        platforms = Platform.objects.all()

        self.fields['platform']
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


