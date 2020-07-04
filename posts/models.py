from django.db import models
import django.utils.timezone

from django.dispatch import receiver
import os

from .validators import validate_file_extension

import nltk
import slate3k as slate

# Create your models here.

class Document(models.Model):
    eBookName = models.CharField(max_length=200, default='', null=False, blank=False)
    eBookFile = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_file_extension], null=False, blank=False)
    eBookData = models.TextField(default='', null=True, blank=True, editable=False)
    createdDatetime = models.DateTimeField(auto_now_add=True)
    updatedDatetime = models.DateTimeField(auto_now=True)
    addedBy = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.eBookName

@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.eBookFile:
        if os.path.isfile(instance.eBookFile.path):
            os.remove(instance.eBookFile.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).eBookFile
    except Document.DoesNotExist:
        return False

    new_file = instance.eBookFile 
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)  
            
                 