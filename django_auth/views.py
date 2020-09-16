from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .models import User
from .forms import SignUpForm
from institute.models import Student, Official
from workers.models import Worker

# Create your views here.

class LoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name='django_auth/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_student:
            return reverse('students:student_home')
        elif user.is_official:
            return reverse('officials:official_home')
        elif user.is_worker:
            return reverse('workers:staff_home')

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'django_auth/signup.html'
    form_class = SignUpForm

    success_message = "Sign Up Successful!"

    def get_success_url(self):
        user = self.object
        if user.is_student:
            return reverse('students:student_home')
        elif user.is_official:
            return reverse('officials:official_home')
        elif user.is_worker:
            return reverse('workers:staff_home')

    def form_valid(self, form):
        response = super().form_valid(form)
        is_student = form.cleaned_data.get('is_student')
        is_official = form.cleaned_data.get('is_official')
        is_worker = form.cleaned_data.get('is_worker')
        entity_id = form.cleaned_data.get('entity_id')
        if is_student:
            Student.objects.filter(regd_no = entity_id).update(user = form.instance)
        elif is_official:
            Official.objects.filter(emp_id = entity_id).update(user = form.instance)
        elif is_worker:
            Worker.objects.filter(staff_id = entity_id).update(user = form.instance)

        return response

class PasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, auth_views.PasswordChangeView):
    template_name = 'django_auth/password_change.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_student:
            return reverse('students:student_home')
        elif user.is_official:
            return reverse('officials:official_home')
        elif user.is_worker:
            return reverse('workers:staff_home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Change Password'
        return context


class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'django_auth/password_change.html'
    subject_template_name = 'django_auth/password_reset_subject.txt'
    email_template_name = 'django_auth/password_reset_email.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset Password'
        return context

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'django_auth/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset Password eMail Sent'
        return context

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'django_auth/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reset New Password'
        return context

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'django_auth/password_reset_complete.html'


    



    

