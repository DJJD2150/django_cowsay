from django import forms
from http_forms_and_cows_app.models import CowsayModel

# Got help from Sohail Aslam and Kevin Blount in study hall.
class AddCowsayForm(forms.Form):
    cowsay = forms.CharField(max_length=120) 
