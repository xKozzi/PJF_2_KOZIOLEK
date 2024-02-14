from account.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView as AbstractLoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, View
from tools.views import AbstractView


class AccountGenericView(AbstractView):
    app_name = "account"


class LoginView(AbstractLoginView):
    view_name = "login"
    template_name = "login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        if self.request.user.is_authenticated:
            # Redirect authenticated users to the dashboard
            from finances.views import ExpensesListView

            return reverse(ExpensesListView.get_view_name())
        else:
            # If the user is not authenticated, redirect to some other page or URL
            return reverse(self.view_name)

    def form_invalid(self, form):
        for _, errors in form.errors.items():
            messages.error(self.request, errors[0])
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    view_name = "register"
    form_class = UserCreationForm
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "User successfully registered")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(LoginView.view_name)
    
    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(LoginView.view_name)
        return super().dispatch(*args, **kwargs)


class LogoutView(View):
    view_name = "logout"

    def get(self, request, *args, **kwargs):
        logout(request=request)
        return redirect(LoginView.view_name)
