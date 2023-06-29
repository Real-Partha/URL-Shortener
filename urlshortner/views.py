from django.shortcuts import render
from .models import Url
from .forms import UrlForm
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def redirect(request, link):
    current_obj = Url.objects.filter(shortened_link=link)
    if len(current_obj) == 0:
        return render(request, 'error.html')
    else:
        context = current_obj[0]
        context.access_count += 1
        context.save()
        return render(request, 'redirect.html', {'obj': context}) 
    
def shorten(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_link']
            all_chars = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]
            short_link = ''
            for i in range(6):
                short_link += random.choice(all_chars)
            while len(Url.objects.filter(shortened_link=short_link)) != 0:
                short_link = ''
                for i in range(6):
                    short_link += random.choice(all_chars)
            new_obj = Url(original_link=original_website, shortened_link=short_link)
            new_obj.save()
            return render(request, 'shorturl.html', {'form': form, 'chars': short_link})
    else:
        form = UrlForm()
        return render(request, 'shorten.html', {'form': form})