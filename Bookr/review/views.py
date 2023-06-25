from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render( request, "index.html")

def search_result(request):

    search_text = request.GET.get("search", "")

    return render( request, "search.html", {"search_text":search_text})