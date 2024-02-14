from django.core.mail import send_mail
from django.conf import settings

def send_limit_exceeded_mail(user, category, expense):
    subject = "Warning! You have exceeded your limit for category spending"
    message = f"""Hello {user.email}!
    We regret to inform you that you have exceeded your limit of purchases for {category.name} category with your latest purchase of {expense.name} 
    Either increase your limit or stop further spending.
    Thank you!
    """
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
