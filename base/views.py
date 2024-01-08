from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import EditItemForm


from core.models import Item

def support(request):
    
    context = {}
    return render(request, 'base/support.html', context)


@login_required
def dashboard(request):
    items = Item.objects.filter(created_by=request.user)
    
    context = {
        "items": items
    }
    return render(request, "base/dashboard.html", context)

@login_required
def deleteItem(request, pk):
    item = get_object_or_404(Item, created_by=request.user, pk=pk)
    item.delete()
    
    return redirect("core:delete")


@login_required
def editItem(request, pk):    
    item = get_object_or_404(Item, created_by=request.user, pk=pk)
    
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        
        if form.is_valid():
            form.save()
            
            return redirect('core:details', pk=item.id)
        
    else:
        form = EditItemForm(instance=item)
    
    context = {
        "form": form
    }
    return render(request, "core/post-item.html", context)