from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from project.models import Project
from .forms import ManagerRegisterForm,DeveloperRegistrationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView,LogoutView
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import ListView


# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegisterForm
    template_name = 'user/Managerregister.html'
    success_url = "/user/login/"
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Manager'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        if user is not  None:
            try:
                subject = "manager...Welcome to my site..."
                message = "You have been register on my website...\n thank you..."
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                print(e)
            login(self.request,user)
        return super(ManagerRegisterView,self).form_valid(form)
        

class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegistrationForm
    template_name = 'user/Developerregister.html'
    success_url = "/user/login"    
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Developer'
        return super().get_context_data(**kwargs)
    
    def form_valid(self,form):
        #email = form.cleaned_data.get('email')
        user = form.save()
        if user is not None:
            try:
                subject = "manager...Welcome to my site..."
                message = "You have been register on my website...\n thank you..."
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, from_email, recipient_list)
            except Exception as e:
                print(e)
            login(self.request,user)
        return super(DeveloperRegisterView,self).form_valid(form)

class UserLoginView(LoginView):
    template_name = 'user/login1.html'
    success_url = "/user/dashboard/"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/dashboard/'
            else:
                return '/user/dashboard/'
            # if self.request.user.is_customer:
            #     return '/user/dashboard/'
    # def get_redirect_url(self):
    #     if self.request.user.is_authenticated:
    #         if self.request.user.is_customer:
    #             return '/user/dashboard/'        

def dashboard(request):
    return render(request,'index.html')                

    # def form_valid(self,form):
    #     user=form.save()
    #     if user is not None:
    #          subject = "Developer...Welcome to my site..."
    #          message = "You have been register on my website...\n thank you..."
    #          from_email = settings.EMAIL_HOST_USER
    #          recipient_list = [user.email]
    #          send_mail(subject, message, from_email, recipient_list)
    #          login(self.request,user)
    #     return super(OwnerRegisterView,self).form_valid(form)  
    #     #return super(CustomerRegisterView,self).form_valid(form)   

    # def form_valid(self,form):
    #     user=form.save()
    #     if user is not None:
    #          subject = "Developer...Welcome to my site..."
    #          message = "You have been register on my website...\n thank you..."
    #          from_email = settings.EMAIL_HOST_USER
    #          recipient_list = [user.email]
    #          send_mail(subject, message, from_email, recipient_list)
    #          login(self.request,user)
    #     return super(CustomerRegisterView,self).form_valid(form)        
                      
class UserLogoutView(LogoutView):
    template_name = "user/logout.html"
#     success_url = '/user/home/'
    
# def dashboard(request):
#     return render(request,'user/home.html')

class managerlogin(LoginView):
    template_name = "user/managerlogin.html" 
    def get_redirect_url(self):
         if self.request.user.is_authenticated:
             if self.request.user.is_manager:
                 return './managerpage/'
             else:
                 return '/user/developerpage/'


class ManagerPage(ListView):            
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()
        
        return render(request, './managerpage.html',{
            'projects':project,
        })

    template_name = 'templates/managerpage.html'

class ManagerDashboardView(ListView):            
    
    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()
        
        return render(request, 'user/manager_dashboard.html',{
            'projects':project,
        })

    template_name = 'user/manager_dashboard.html'


class ContactUs(ListView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()

        return render(request, './contactus.html', {
            'projects': project,
        })

    template_name = 'templates/contactus.html'


class AboutUs(ListView):

    def get(self, request, *args, **kwargs):
        project = Project.objects.all().values()

        return render(request, './aboutus.html', {
            'projects': project,
        })

    template_name = 'templates/aboutus.html'
