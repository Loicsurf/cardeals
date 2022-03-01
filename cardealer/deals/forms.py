from django import forms
from .models import Cars



class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', "type", "price", "stock", "image"]

    def is_valid(self):
        valid = super(CreateCarForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        car = super(CreateCarForm, self).save(commit=False)
        if commit:
            car.save()
        return car