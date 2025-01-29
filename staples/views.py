from django.shortcuts import render
from .models import StapleItem
from django.contrib.auth.decorators import login_required

@login_required
def render_staples_list(request):
    """
    Renders the user's personal staples list
    """
    staples = StapleItem.objects.filter(user=request.user)
    return render(
        request, 
        "staples/staples.html", 
        {"staples": staples}
    )