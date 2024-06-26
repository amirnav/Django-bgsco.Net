from django.shortcuts import render, redirect

from career.forms import HiringForm


def hiringView(request):
    if request.method == "POST":
        form = HiringForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:home')
    else:
        form = HiringForm()
    return render(request, "career/career.html", {"form": form})
