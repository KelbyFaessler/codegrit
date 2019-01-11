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
    about page
    """

    return render(
        request,
        'about.html',
        context={}
    )