from django.shortcuts import render
from django.contrib import messages
from .forms import ContactFeedbackForm
from django.shortcuts import redirect
from django.core.mail import mail_admins
from resume.models import ResumeProfilePicture,ResumeProfile

def my_contact(request):
    resume = ResumeProfile.objects.get(pk=1)
    resume_pic = ResumeProfilePicture.objects.get(pk=2)
    if request.method == 'POST':
        f = ContactFeedbackForm(request.POST)
        if f.is_valid():
            # send contact feedback to mail
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Contact Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            mail_admins(subject, message)

            # save contact feedback to database
            f.save()
            messages.add_message(request, messages.INFO, 'Contact Feedback Submitted.')
            return redirect('contact:my_contacts')
    else:
        f = ContactFeedbackForm()
    context = {
            'form': f,
            'resume_pic': resume_pic,
            'resume': resume
        }
    return render(request, 'contact/contact.html', context)