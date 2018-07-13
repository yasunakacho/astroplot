from django import forms
from .models import Alert

class AlertForm(forms.Form):
    user = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    coin = forms.IntegerField(widget = forms.HiddenInput(), required=True)
    high_price = forms.IntegerField(widget = forms.NumberInput(), required=False, label='When Price is Above')
    low_price = forms.IntegerField(widget = forms.NumberInput(), required=False, label='When Price is Below')

