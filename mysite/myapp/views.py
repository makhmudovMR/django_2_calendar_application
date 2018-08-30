from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Entery
from .forms import EnteryForm


def index(request):
    enteries = Entery.objects.all()
    return render(request, 'myapp/index.html', context={'enteries': enteries})


def details(request, pk):
    entry = get_object_or_404(Entery, pk=pk)
    return render(request, "myapp/details.html", context={'entery': entry})


def add(request):
    if request.method == 'POST':
        form = EnteryForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']

            Entery.objects.create(
                name=name,
                date=date,
                description=description
            ).save()
            return HttpResponseRedirect('/myapp')
    else:
        form = EnteryForm()

    return render(request, "myapp/form.html", {"form": form})


def delete(request, pk):
    if request.method == 'DELETE':
        entery = get_object_or_404(Entery, pk=pk)
        entery.delete()
        return HttpResponseRedirect('myapp/')