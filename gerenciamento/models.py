from django.db import models
from django.conf import settings

class Dados_Status(models.Model):

    status = models.CharField(
        max_length=15,
        blank=True,
        help_text='Seu status atual',
    )

    turno = models.CharField(
        max_length=2,
        blank=True,
        help_text='Turno atual de trabalho',
    )

    user_name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='',
    )

    # LOAN_STATUS = (
    #     ('Online', 'Online'),
    #     ('Offline', 'Offline'),
    #     ('Refeição', 'Refeição'),
    #     ('Pausa', 'Pausa'),
    #     ('Férias', 'Férias'),
    # )

    # status = models.CharField(
    #     max_length=15,
    #     choices=LOAN_STATUS,
    #     blank=True,
    #     default='Online',
    #     help_text='Seu status atual',
    # )

    # LOAN_TURNO = (
    #     ('C1', 'C1'),
    #     ('C2', 'C2'),
    #     ('T1', 'T1'),
    #     ('T2', 'T2'),
    #     ('T3', 'T3'),
    # )

    # turno = models.CharField(
    #     max_length=2,
    #     choices=LOAN_TURNO,
    #     blank=True,
    #     default='C1',
    #     help_text='Turno atual de trabalho',
    # )

# class Dados_Teste(models.Model):
    
#     status = models.CharField(
#         max_length=15,
#         blank=True,
#         help_text='Seu status atual',
#     )

#     turno = models.CharField(
#         max_length=2,
#         blank=True,
#         help_text='Turno atual de trabalho',
#     )
