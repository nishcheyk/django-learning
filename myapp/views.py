from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import ContactForm
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves data to the database
            return JsonResponse({"message": "Form submitted successfully!"}, status=201)
        return JsonResponse({"error": "Invalid form data"}, status=400)

    form = ContactForm()
    return render(request, "contact.html", {"form": form})


def save_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description", "")

        if name and price:
            product = Product(name=name, price=price, description=description)
            product.save()
            return JsonResponse({"message": "Product saved successfully!"}, status=201)

        return JsonResponse({"error": "Invalid data"}, status=400)

    return render(request, "product_form.html")


@csrf_exempt
def save_product_json(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            price = data.get("price")
            description = data.get("description", "")

            if name and price:
                Product.objects.create(name=name, price=price, description=description)
                return JsonResponse({"message": "Product saved successfully"}, status=201)

            return JsonResponse({"error": "Invalid data"}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return render(request, "Product.html") or HttpResponse("Template not found", status=404)



from .forms import ProfileForm
from .models import Profile

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile-list')
    else:
        form = ProfileForm()
    return render(request, 'upload_profile.html', {'form': form})


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})

