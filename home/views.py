from django.shortcuts import render
from .models import HomePageContent


def render_home(request):
    """
    Renders the home page
    """
    home_content = HomePageContent.objects.all().order_by('-updated_at').first()

    return render(
        request,
        "home/home.html",
        {"home_content": home_content},
    )