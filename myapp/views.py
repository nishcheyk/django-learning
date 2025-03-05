from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves data to the database
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
