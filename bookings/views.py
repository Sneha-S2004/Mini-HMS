from django.shortcuts import render, redirect
from .forms import BookingForm

def book_appointment(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = BookingForm()

    return render(request, 'bookings/book_appointment.html', {'form': form})
