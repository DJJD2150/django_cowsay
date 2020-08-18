from django.shortcuts import render
import subprocess

from http_forms_and_cows_app.models import CowsayModel
from http_forms_and_cows_app.forms import AddCowsayForm

# Create your views here.
# Got help from Sohail Aslam in study hall, significant help from Detrich Schilling via 1-on-1 meeting
def index_view(request):
    if request.method == "POST":
        form = AddCowsayForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cow_mooove = CowsayModel.objects.create(
                cowsay = subprocess.check_output(['cowsay', data.get('cowsay')]).decode()
            )
            
            return render(request, 'index.html', {"form": form, "cow_mooove": cow_mooove})

    form = AddCowsayForm()
    return render(request, 'index.html', {"form": form})

def history_view(request):
    history = CowsayModel.objects.order_by('-id')[:10]
    return render(request, 'history.html', {"history": history})
