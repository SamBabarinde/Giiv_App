from django.shortcuts import render, get_object_or_404, redirect
from core.models import Item
from .models import Conversations, ChatMessage
from django.contrib.auth.decorators import login_required

from .forms import ChatMessageForm


@login_required
def New_conversation(request, ipk):
    item = get_object_or_404(Item, pk=ipk)
    
    if item.created_by == request.user:
        return redirect('base:dashboard')
    
    conversation = Conversations.objects.filter(item=item).filter(members__in=[request.user.id])
    
    if conversation:
        return redirect("chats:dm", pk=conversation.first().id)
    
    if conversation:
        pass
    
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        
        if form.is_valid:
            conversation = Conversations.objects.create(item=item);
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            return redirect("core:details", pk=ipk)
        
    else:
        form = ChatMessageForm()
        
    context = {
        "form": form
    }        
    return render(request, "chats/new.html", context)
            
    
@login_required
def inbox(request):
    conversation = Conversations.objects.filter(members__in=[request.user.id])

    context={
        "conversation": conversation
    }
    return render(request, "chats/inbox.html", context)


@login_required
def directMessage(request, pk):
    conversation = Conversations.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method =='POST':
        form = ChatMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect('chats:dm', pk=pk)
        
    else:
        form = ChatMessageForm()
        
    context = {
        "conversation": conversation,
        "form": form
    }
    return render(request, "chats/directmessage.html", context)