from django.shortcuts import render, redirect,  get_object_or_404
from .models import Profile, Tweet
from .forms import StartupForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User





def index(request):
    return render(request, 'index.html')

@login_required
def tweet(request):
    if request.method == 'POST':
        form = StartupForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('tweet_list')
    else:
        form = StartupForm()
    return render(request, 'tweet.html' ,{'form':form})


def tweet_list(request):
    profiles = Profile.objects.all()
    return render(request, 'tweet_list.html', {'profiles':profiles})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm
    return render(request, 'registration/register.html', {'form':form})







def profile_view(request, profile_id):
    # Fetch the profile of the logged-in user
    print(profile_id)
    profiles =  Profile.objects.filter(id= profile_id)  # Get the profile for the logged-in user
    # Fetch all tweets associated with the user's profile
    return render(request, 'profile_view.html', {'profiles': profiles})