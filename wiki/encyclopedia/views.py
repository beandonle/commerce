from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django import forms

from . import util
import markdown2
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

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
            "message": 'The requested page ' + label + ' was not found.'
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
                "message": 'Search for ' + q + ' is invalid.'
            })

def edit(request, label):
    if request.method == "GET":
        content = util.get_entry(label)
        return render(request, "encyclopedia/editPage.html", {
            "content" : content,
            "title" : label
        })
    elif request.method == "POST":
            title = request.POST["title"]
            content = request.POST["editedContent"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:title", args=(title,)))

def newPage(request): 
    if request.method == "POST":
        if (request.POST.get("title") in util.list_entries()):
            title = request.POST.get("title")
            return render(request, "encyclopedia/error.html", {
                "message" : 'The entry ' + title + ' already exists.'
            })

        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("encyclopedia:title", args=(title,)))
        else:
                return render(request, "encyclopedia/newPage.html", {
                    "form" : form
                })
    return render(request, "encyclopedia/newPage.html", {
        "form" : NewEntryForm()
    })