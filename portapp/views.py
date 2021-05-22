from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.
def homepage(request):

    if request.method == "POST":
        form1 = feedbackForm(request.POST)
        if form1.is_valid():
            try:
                form1.save()
                messages.success(request, 'Your feedback has been submitted successfully!')
                return redirect("/")
            except:
                pass    
    else:
        form1 = feedbackForm()

    dict1 = {
        'zform':form1
    }

    return render(request, 'portapp/porthome.html', dict1)