# from django.shortcuts import render

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

# Create your views here.

def home(request):
    # Include an empty contact form for the home page and pass any 'sent' flag from query params
    form = ContactForm()
    sent = request.GET.get('sent')
    return render(request, 'home.html', {'form': form, 'sent': sent})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                print("Data saved to database")
                return redirect(reverse('home') + '?sent=1')
            except Exception as e:
                # Log and redirect with an error flag so UI can show a friendly message
                print('Error saving contact form:', e)
                return redirect(reverse('home') + '?sent=0')
        else:
            print("form is not valid")
            # Render home with the form (so errors can be inspected if template uses them)
            return render(request, 'home.html', {'form': form})
    else:
        return redirect('home')

def success_view(request):
    return render(request, 'success.html')  # Create a success.html template

def projects_all(request):
    """Render a full projects listing page."""
    # For now use static data in template; later this can query a Project model
    return render(request, 'projects.html')


def blogs_all(request):
    """Render a full blog/articles listing page."""
    return render(request, 'blogs.html')


def events_all(request):
    """Render a full events listing page."""
    return render(request, 'events.html')