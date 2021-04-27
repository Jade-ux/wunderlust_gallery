
from django import forms
from .models import Artwork, Category


class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        # This dunder includes all the fields
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-grey'