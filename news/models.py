from django.db import models
from django.utils import timezone 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import send_push


class LatestProblems(models.Model):
    description = models.TextField(verbose_name='Суть проблемы')
    date_created = models.DateTimeField(default=timezone.now,verbose_name='Дата и время создания')
    date_updated = models.DateTimeField(blank=True, null=True, verbose_name='Дата обновления')
    status = models.CharField(max_length=255, verbose_name='Закрытие кейса/интеракции')
    comment = models.TextField(blank=True, verbose_name='Доп. инф-ия')
    
    class Meta:
        db_table = 'latest_problems'
        ordering = ['-date_created', '-date_updated']
        verbose_name = 'Актуальная проблема'
        verbose_name_plural = 'Актуальные проблемы'

    def __str__(self):
        return f'{self.id}'

@receiver(post_save, sender=LatestProblems)
def update_problems(sender, instance, **kwargs):
    print('Receiver')
    