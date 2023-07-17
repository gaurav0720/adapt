from django.shortcuts import render
from .emailHelper import EmailHelper
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        if 'contact_name' in request.POST:
            contact_name = request.POST['contact_name']
            contact_email = request.POST['contact_email']
            contact_message = request.POST['contact_message']

            contact_message = "An user tried to contact you. These are the contact details: Name: {0}, Email: {1}, Message:{2}".format(contact_name, contact_email, contact_message)
            send_mail('New user contacted at ADAPT Marketplace', contact_message, 'adaptmarketplace@gmail.com', ['ADAPTMarketplace@uabmc.edu', 'adaptmarketplace@gmail.com'], fail_silently=False)

            EmailHelper.send_uab_message('New user contacted at ADAPT Marketplace', contact_message, ['ADAPTMarketplace@uabmc.edu'])

            return render(request, 'index.html', {'contact_success': "success"})
    return render(request, 'index.html')
