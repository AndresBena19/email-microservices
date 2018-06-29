from django.shortcuts import render
from .forms import FileForm
from django.shortcuts import render, redirect
from .models import File_Upload

from django.http import HttpResponseRedirect


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = FileForm()
    return render(request, 'formfile.html', {'form': form})

