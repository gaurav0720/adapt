from django.shortcuts import render
from .emailHelper import EmailHelper
from django.core.mail import send_mail
from email.mime.text import MIMEText

def index(request):
    if request.method == 'POST':
        if 'contact_name' in request.POST:
            contact_name = request.POST['contact_name']
            contact_email = request.POST['contact_email']
            contact_message = request.POST['contact_message']

            contact_message = "<strong>An user tried to contact you.</strong><br><br>These are the contact details:<br><strong>Name:</strong>{0}<br><strong>Email:</strong>{1}<br><strong>Message:</strong>{2}".format(contact_name, contact_email, contact_message)
            mail = MIMEText(contact_message, 'html')
            send_mail('New user contacted at ADAPT Marketplace', mail, 'adaptmarketplace@gmail.com', ['ADAPTMarketplace@uabmc.edu', 'adaptmarketplace@gmail.com'], fail_silently=False)

            EmailHelper.send_uab_message('New user contacted at ADAPT Marketplace', contact_message, ['ADAPTMarketplace@uabmc.edu'])

            return render(request, 'index.html', {'contact_success': "success"})
    return render(request, 'index.html')
