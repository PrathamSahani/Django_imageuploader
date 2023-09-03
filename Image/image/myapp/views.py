from django.shortcuts import render
from .forms import ImageForm
from .models import Image


# Create your views here.
def home(reqest):
    if reqest.method =="POST":
        form = ImageForm(reqest.POST, reqest.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    
    img = Image.objects.all()
    return render(reqest,'myapp/home.html', {'img':img, 'form': form})