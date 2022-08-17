from django.db import models
from django.conf import settings

class Dados_Status(models.Model):
    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='',
    )

    LOAN_STATUS = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Refeição', 'Refeição'),
        ('Pausa', 'Pausa'),
        ('Férias', 'Férias'),
    )

    status = models.CharField(
        max_length=15,
        choices=LOAN_STATUS,
        blank=True,
        default='Online',
        help_text='Seu status atual',
    )

    LOAN_TURNO = (
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('T1', 'T1'),
        ('T2', 'T2'),
        ('T3', 'T3'),
    )

    turno = models.CharField(
        max_length=2,
        choices=LOAN_TURNO,
        blank=True,
        default='C1',
        help_text='Turno atual de trabalho',
    )


# from multiprocessing.reduction import AbstractReducer
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# class CustomAccountManager(BaseUserManager):
#     def create_user(self, email, user_name, first_name, password, **other_fields):

#         if not email:
#             return ValueError(_('Você deve colocar um e-mail'))
#         email = self.normalize_email(email)
#         user = self.model(
#             email=email,
#             user_name=user_name,
#             first_name=first_name,
#             **other_fields)
#         user.set_password(password)
#         user.save()
#         return user

# class NewUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(
#         gettext_lazy('email adress'),
#         unique=True)
#     user_name = models.CharField(
#         max_leght=150,
#         unique=True)
#     first_name = models.CharField(
#         max_length=150)
#     start_date = models.DateTimeField(
#         default=timezone.now)
#     about = models.TextField(
#         gettext_lazy('about'),
#         max_length=500,
#         blank=TRUE)
#     is_staff = models.BooleanField(
#         default=False)
#     is_active = models.BooleanField(
#         default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['user_name']

#     def __str__(self):
#         return self.user_name