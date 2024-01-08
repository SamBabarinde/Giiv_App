from django.shortcuts import render, redirect
from .forms import SignUpForm, SetPasswordForm, PasswordResetForm
from django.contrib.auth import logout
from django.contrib import messages
from .decorators import user_not_authenticated
from django.contrib.auth.decorators import login_required

# for user error solving
from django.contrib.auth import get_user_model
User = get_user_model()

# for user email verification
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token

# for email passsword reset
from django.db.models.query_utils import Q
# from typing import protocol


def activateAccount(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        return redirect('userauth:login')
        messages.success(request, f"Your email is successfully confirmed, please proceed to login")
    else:
        messages.error(request, "Activation link invalid or expired, please request for a new activation link")
        
    return redirect('core:home')


def activateEmail(request, user, to_email):
    email_subject = "Activate Your Account"
    email_message = render_to_string("userauth/email_activation_template.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(email_subject, email_message, to=[to_email])
    
    if email.send():
        messages.success(request, f"Dear {user}, your verification mail has been sent to {to_email}, please click on confirmation link \
                     to confirm your email and complete your registration")
        return redirect('userauth:login')
    else:
        for error in list(form.errors.values()):
            messages.error(request, f"Problem sending message to {to_email}, please verify that your email is correct")
        
    
@user_not_authenticated
def signUp(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            
            return redirect("userauth:login")
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
        
        
    else:
        form = SignUpForm()
    
    context = {
        "form": form
    }
    
    return render(request, "userauth/signup.html", context)


def signOut(request):
    logout(request)
    return redirect('core:index')


# @user_not_authenticated
# def signIn(request):
    
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         try:
#             user = User.objects.get(email=email)
#             user = authenticate(request, email=email, password=password)
            
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Hi {user.username}, you've been logged in")
#                 return redirect('core:index')
            
#             else:
#                 messages.warning(request, f"There is an error, please check your details.")
                
#         except:
#             messages.warning(request, f"user with {email} does not exist")    
            
#     context = {
            
#         }
    
#     return render(request, 'userauth/login.html', context)


@login_required
def changePassword(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed successfully")
            return redirect('userauth:login')
        
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
            
    form = SetPasswordForm(user)
    
    context = {
        'form': form
    }
    return render(request, 'userauth/password_change.html', context)


@user_not_authenticated
def resetPassword(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            right_user = get_user_model().objects.filter(Q(email=user_email)).first()
            
            if right_user:
                email_subject = "Reset Your Password"
                email_message = render_to_string("userauth/reset_password_template.html", {
                    'user': right_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(right_user.pk)),
                    'token': account_activation_token.make_token(right_user),
                    'protocol': 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(email_subject, email_message, to=[right_user.email])
                
                if email.send():
                    messages.success(request, f"Dear {right_user}, your password reset link has been sent to {right_user.email} if an account exists with the email, please click on confirmation link \
                                to confirm your email and reset your password")
                    return redirect('userauth:login')
                
                else:
                    for error in list(form.errors.values()):
                        messages.error(request, f"Problem sending mail to {right_user.email}, please verify that your email is correct")
                        
        else:
            for error in list(form.errors.values()):
                messages.error(request, f"Problem resetting password")  
                  
            return redirect('core:home')
        
    form = PasswordResetForm(request.POST)
        
    return render(
        request=request,
        template_name='userauth/email_reset_password.html',
        context= {'form': form}
    )
    
def confirmResetPassword(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
        
    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, f"Your password is successfully changed, please proceed to login")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, f"Problem resetting password")  

        form = SetPasswordForm(user)
        return render(request, 'userauth/login.html', {'form': form})
        
    else:
        messages.error(request, "Reset link invalid or expired, please request for a new activation link")
    
    messages.error(request, "Password reset not successful, now redirecting back to the homepage")
    return redirect('core:home')
