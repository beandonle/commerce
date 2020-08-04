from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import util
import markdown2
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newPage(request): 
    return render(request, "enclyclopedia/newPage.html")

def randPage(request):
    label = random.choice(util.list_entries())
    return render(request, "encyclopedia/randPage.html", {
        "content": markdown2.markdown(util.get_entry(label)),
        "label": label
    })

def title(request, label):
    if (label in util.list_entries()):
        return render(request, "encyclopedia/title.html", {
            "content": markdown2.markdown(util.get_entry(label)),
            "label": label
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "label": label
        })


def search(request):
    if request.method == "POST":
        q = request.POST['q']
        entries = util.list_entries()
        searchResults = [entry for entry in entries if q in entry]

        if (q in entries):
            return render(request, "encyclopedia/title.html", {
            "content": markdown2.markdown(util.get_entry(q)),
            "label": q
        })
        elif searchResults: 
            return render(request, "encyclopedia/searchResults.html", {
                "results": searchResults,
                "q" : q
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "label": q
            })

def edit(request, page):
    txtArea = page