from django import forms
from .models import Collectable, Platform, SellCollectable, Review


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


class SellCollectableForm(forms.ModelForm):
    class Meta:
        model = SellCollectable
        fields = '__all__'
        labels = {
            'collectable_item': 'Collectable Item',
            'platform': 'Platform',
            'additional_information': 'Additional information',
            'full_name': 'Full Name',
            'contact_number': 'Contact Number',
            'email': 'Email',
            'image': 'Image',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('full_name', 'email',
                  'product_type', 'body',)
