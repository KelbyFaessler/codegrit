from django.shortcuts import render

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

    return render(
        request,
        'signup.html',
        context={}
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