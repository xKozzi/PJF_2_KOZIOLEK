from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_add_user_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
