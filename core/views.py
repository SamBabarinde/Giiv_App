from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Item
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm


def index(request):
    context = {}
    return render(request, 'core/index.html', context)


def home(request):
    items = Item.objects.filter(is_available=True)
    categories = Category.objects.all()[0:3]
    
    context = {
        "items": items,
        "categories": categories,
    }
    return render(request, 'core/home.html', context)


@login_required
def details(request, pk):
    item = Item.objects.get(pk=pk)
    related_item = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]
    
    context = {
        "item": item,
        "related_item": related_item,
    }
    return render(request, 'core/details.html', context)


@login_required
def postItem(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            return redirect('core:details', pk=item.id)
        
    else:
        form = NewItemForm()
    
    context = {
        "form": form
    }
    return render(request, "core/post-item.html", context)


def searchItem(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_available=True)
    categories = Category.objects.all()
    category_id = request.GET.get('c', 0)
    
    if category_id:
        items = items.filter(category_id=category_id)
        
    if query:
        items = items.filter(Q(title__icontains=query) | Q(description__icontains=query))
    
    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    }
    return render(request, 'core/search.html', context )