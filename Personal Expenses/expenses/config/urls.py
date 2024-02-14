from django.urls import re_path, include
from django.conf.urls.static import static
from django.conf import settings
from account.views import LoginView, RegisterView, LogoutView
from django.views.generic.base import RedirectView
from finances import urls as finances_urls


urlpatterns = [
    re_path(r"^$", view=RedirectView.as_view(url="login"), name="root"),
    re_path(
        r"^login$", view=LoginView.as_view(), name=LoginView.view_name
    ),
    re_path(r"^logout$", view=LogoutView.as_view(), name=LogoutView.view_name),
    re_path(r"^register$", view=RegisterView.as_view(), name=RegisterView.view_name),
    re_path(r"", include((finances_urls, "finances"))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)