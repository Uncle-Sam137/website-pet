from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import JobOfferForm
from .models import JobOffer

def home(request):
    if request.method == 'POST':
        form = JobOfferForm(request.POST)
        if form.is_valid():

            form.save()

            return HttpResponseRedirect('/')

    else:
        form = JobOfferForm()

    return render(request, 'base.html', {'form': form})



