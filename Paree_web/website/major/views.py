from django.shortcuts import render
from django.contrib import messages
from major.prediction import prepros

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == "POST":
        text = request.POST['text']
        ans = prepros(text)
        # messages.success(request, "The text type is : "+ans)
    return render(request, "index.html", {"prediction": ans, "text":text})