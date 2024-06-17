from django.shortcuts import render

# Create your views here.
def myfun(request):
    return render(request, 'files/feedback.html')