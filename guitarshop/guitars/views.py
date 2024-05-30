from django.shortcuts import render
from django.http import HttpResponse, Http404
from datetime import date


# 1. Create View
# 2. Create URL paths, linking views.py with urls.py
# 3. Create HTML page on templates folder
# 4. Include App.urls file on Project.urls file
# 5. Add app to installed apps on Project settings.py
# 6. Add BASE_DIR to settings file to pick up global templates

def index(request):
    return render(request, "guitars/index.html")

def guitar_list(request):
    return render(request, "guitars/guitarlist.html")

def guitar_details(request, slug):
    return render(request, "guitars/guitar.html")