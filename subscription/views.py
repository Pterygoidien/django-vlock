from django.shortcuts import render
from .forms import SubscriptionForm

# Create your views here.

def home(request):

    if(request.method == 'POST'):
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        location = request.POST['location']
        print(email, first_name, last_name, location)

        return render(request, 'subscription/success.html', {'email': email})
    else:
        form = SubscriptionForm()

    return render(request, 'subscription/index.html', {'form': form})
