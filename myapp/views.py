from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.http import JsonResponse

def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ImageForm()

    img = Image.objects.all().order_by('-date')
    return render(request, 'myapp/home.html', {'img': img, 'form': form})


def like_image(request):
    image_id = request.POST.get('image_id')
    image = Image.objects.get(id=image_id)


    liked_images = request.session.get('liked_images', [])

    if image_id in liked_images:

        image.likes -= 1
        liked_images.remove(image_id)
        liked = False
    else:

        image.likes += 1
        liked_images.append(image_id)
        liked = True

    image.save()
    request.session['liked_images'] = liked_images

    return JsonResponse({
        'likes': image.likes,
        'liked': liked
    })


