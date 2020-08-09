from django import forms

from chat.models import Room


class RoomCreationForm(forms.ModelForm):
    # your_name = forms.CharField(label="Your name", max_length=100)

    class Meta:
        model = Room
        fields = ["name"]

    def clean(self):
        cleaned_data = self.cleaned_data
        if room_name := cleaned_data.get('name'):
            if '@' in room_name:
                msg = '@ not allowed in room names.'
                self._errors['name'] = self.error_class([msg])
                del cleaned_data['name']
        return cleaned_data
