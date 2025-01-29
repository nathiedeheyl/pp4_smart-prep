from django.shortcuts import render, get_object_or_404, reverse
from .models import StapleItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import StapleHandling

@login_required
def render_staples_list(request):
    """
    Renders the user's personal staples list and handles form submissions
    """
    staples = StapleItem.objects.filter(user=request.user)

    if request.method == "POST":
        form = StapleHandling(request.POST)
        if form.is_valid():
            staple = form.save(commit=False)
            staple.user = request.user
            staple.save()

    form = StapleHandling()
    
    return render(
        request, 
        "staples/staples.html", 
        {
            "staples": staples,
            "comment_form": form,
        },
    )


@login_required
def edit_staple(request, staple_id):
    """
    View to edit staples list items
    """

    staple = get_object_or_404(StapleItem, pk=staple_id, user=request.user)

    if request.method == "POST":
        form = StapleHandling(request.POST, instance=staple)
        if form.is_valid():
            form.save()
            messages.add_message(request,
            messages.SUCCESS, 'Staple Item Updated!')
        else:
            messages.add_message(request,
            messages.ERROR, 'Error updating staple item!')
        
    return HttpResponseRedirect(reverse('staples'))
