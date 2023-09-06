from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage 


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            #print(first_name)

            #store data in the database
            Form.objects.create(first_name=first_name, last_name=last_name,
                                email=email, date=date, occupation=occupation)
            
            #send an email when subitted
            message_body = f"A new job application was submitted. Thank you, \n {first_name}!"
            #string is the subject
            email_message = EmailMessage('Form Submission Confirmation')
            messages.success(request, 'Form submitted succesfully!', message_body, to=[email])
            # sends the email to the user 
            #go to settings.py to specify 
            email_message.send()

    return render(request, 'index.html')

