from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)  # <-- FILES in all caps
        if form.is_valid():
            form.save()
            return redirect('/')  # redirect after successful upload
    else:
        form = ImageForm()  # create an empty form if not POST

    img = Image.objects.all().order_by('-date')  # newest first
    return render(request, 'myapp/home.html', {'img': img, 'form': form})
