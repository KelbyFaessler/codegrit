from django.shortcuts import render
from core.forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect

def index(request):
    """
    main homepage
    """

    return render(
        request,
        'index.html',
        context={}
    )

def about(request):
    """
    about page: has copy and redirects to the signup form page via
                the signup button at the end of the copy
    """

    return render(
        request,
        'about.html',
        context={}
    )

def contact(request):
    """
    contact page: simple page that just provides support email address
    """

    return render(
        request,
        'contact.html',
        context={}
    )

def signup(request):
    """
    signup page: form to collect user info if they want to sign up
    """
    if request.method == "POST":
        form = UserForm(request.POST)        
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            #redirect
            return HttpResponseRedirect('index.html')
    else:
        form = UserForm()

    return render(
        request,
        'signup.html',
        context={'form': form}
    )

def terms(request):
    """
    terms and conditions page: basic terms, gives credibility to site
    """

    return render(
        request,
        'terms.html',
        context={}
    )