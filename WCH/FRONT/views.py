from django.shortcuts import render
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request, 'base.html')
def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = BookingForm()
    dict_form={
        'form' : form
    }
    return render(request, 'booking.html', dict_form)