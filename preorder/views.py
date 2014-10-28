from django.shortcuts import render
from django.template import RequestContext
from django.core.mail import send_mail

from preorder.forms import CustomerForm

from mvp.utils import MAILCHIMP_LIST_ID, get_mailchimp_api

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def order(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            # Send an email confirmation
            
            user_email = form.cleaned_data['email']
            
            subject = "Thanks for Preordering Coding with Cats"
            message = "Thanks for preordering Coding with Cats. You'll be hearing from us soon about your order and you'll be coding with your cat's in no time!"
            from_email = "welcome@example.com"
            to_emails = [user_email] 
            send_mail(subject, message, from_email, to_emails, fail_silently=True)
            
            # Subscribe to mailchimp list
            m = get_mailchimp_api()
            m.lists.subscribe(MAILCHIMP_LIST_ID, {'email': user_email})
            
            return thanks(request)
        else:
            print form.errors
    else:
        form = CustomerForm()
        
    return render(request, 'order.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html', {})