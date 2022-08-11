from django.db import models


class Dados_Status():
    user_name = models.CharField(
        max_length=150,
        unique=True)
    status = (
        ('Online', 'Online'),
        ('Offline', 'Offline'),
        ('Refeição', 'Refeição'),
        ('Pausa', 'Pausa'),
        ('Férias', 'Férias'),
    )
    turno = (
        ('C1', 'C1'),
        ('C2', 'C2'),
        ('T1', 'T1'),
        ('T2', 'T2'),
        ('T3', 'T3'),
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
