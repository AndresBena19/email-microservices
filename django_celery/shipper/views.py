from .forms import FileForm
from django.shortcuts import render, redirect


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('UPLOAD_FILE')
    else:
        form = FileForm()
    return render(request, 'response.html', {'form': form})
