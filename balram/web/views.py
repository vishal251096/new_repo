from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, Combo
from django.utils import timezone
from django.http import HttpResponse
from django.core.mail import send_mail

class IndexView(TemplateView):
    template_name = 'index.html'

class ProductListView(ListView):
    model = Product
    
    def get_queryset(self):
        return Product.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')


class ProductDetailView(DetailView):
    model = Product

def contact_view(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
            sender_name = request.POST.get('name', '')
            sender_email = request.POST.get('email', '')
            message = "{0} has sent you a new message: \n\n{1}".format(sender_name, request.POST.get('message', ''))
            send_mail('New Enquiry', message, sender_email, ['info@balramfurnitures.com'])
            return render(request, 'thanks.html')
    return render(request, 'contact.html')
        



class AboutView(TemplateView):
    template_name = 'about.html'

class ComboListView(ListView):
    model = Combo

    def get_queryset(self):
        return Combo.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class ComboDetailView(DetailView):
    model = Combo

