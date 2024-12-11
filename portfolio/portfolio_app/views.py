# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print("Data saved to database") 
            return redirect('success')  # Redirect to a success page after saving
        else:
            print("form is not valid")
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')  # Create a success.html template