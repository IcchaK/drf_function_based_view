from django.db import models
import django.utils.timezone

from django.dispatch import receiver
import os

# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    title = models.CharField(max_length=50, default='', null=False, blank=False)
    body = models.TextField(max_length=5000, default='', null=False, blank=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.docfile:
        if os.path.isfile(instance.docfile.path):
            os.remove(instance.docfile.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).docfile
    except Document.DoesNotExist:
        return False

    new_file = instance.docfile 
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)       

