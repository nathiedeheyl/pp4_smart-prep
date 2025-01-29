from django.shortcuts import render
from .models import StapleItem
from django.contrib.auth.decorators import login_required
from .forms import StapleHandling

@login_required
def render_staples_list(request):
    """
    Renders the user's personal staples list
    """
    staples = StapleItem.objects.filter(user=request.user)
    add_staple = StapleHandling
    
    return render(
        request, 
        "staples/staples.html", 
        {
            "staples": staples,
        },
    )
