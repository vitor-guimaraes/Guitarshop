from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from datetime import date
from django.urls import reverse


# 1. Create View
# 2. Create URL paths, linking views.py with urls.py
# 3. Create HTML page on templates folder
# 4. Include App.urls file on Project.urls file
# 5. Add app to installed apps on Project settings.py
# 6. Add BASE_DIR to settings file to pick up global templates


guitars = {
        "Old Black": "Neil Young",    
        "Micawber": "Keith Richards",    
        "Greeny": "Peter Green/Gary Moore/Kirk Hammett",
        "Mustang": "Kurt Cobain",
        "Nº2": "Jimmy Page"
}


def index(request): 
    all_guitars = list(guitars.keys())
    all_guitarists = list(guitars.values())

    # guitar_path = reverse("guitarlist")
    # guitar_list = f"<h1><a href='{guitar_path}'></a></h1>"
        # return HttpResponse(guitar_list)

    return render(request, "guitars/index.html", {
        "guitars": all_guitars,
        "guitarists": all_guitarists
    })


def guitar_list(request):
    all_guitars = list(guitars.keys())

    return render(request, "guitars/guitarlist.html", {
        "guitars": all_guitars
    })


def guitar_details(request, slug):
    context = {
        "slug": slug,
        "details": "These are the details for guitar with slug: " + slug,
    }
    return render(request, 'guitars/guitar.html', context)