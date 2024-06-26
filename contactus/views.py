from django.shortcuts import render, redirect

from contactus.forms import ContactUsForm


def contactUs(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactUsForm()
    return render(request, "contactUs/contactUs.html", {"form": form})