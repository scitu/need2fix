import os
import json
import pytz
from django.utils import timezone
from django.db import models
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from app import building_info, division_list

def get_upload_path(instance, filename):
    return os.path.join(instance.requester.username, filename)


usermodel = get_user_model()


class Task(models.Model):
    STATUS_CHOICES = [
        ('1', 'รับเรื่อง'),
        ('2', 'ดำเนินการ'),
        ('3', 'เสร็จสิ้น'),
    ]

    DIVISION_CHOICES = [(k, v) for k, v in division_list.items()]


    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    building = models.CharField(max_length=32)
    floor = models.CharField(max_length=32)
    room = models.CharField(max_length=32, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    done_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES)
    division = models.CharField(max_length=2, blank=True, choices=DIVISION_CHOICES, null=True)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)
    requester = models.ForeignKey(usermodel, blank=True, on_delete=models.PROTECT, related_name='request_set')
    operator = models.ForeignKey(usermodel, null=True, blank=True, on_delete=models.SET_NULL, related_name='task_set')

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.pk:
            self.status = '1'
            if 'user' in kwargs:
                self.requester = kwargs['user']
        self.full_clean()
        if self.status == '3':
            self.done_date = timezone.now()
        super(Task, self).save(*args, **kwargs)
        
    def clean(self, *args, **kwargs):
        if self.status in ('2', '3') and not self.operator:
            raise ValidationError('Null Operator exeption')        
        if self.operator and not self.operator.groups.filter(name='mechanic'):
            raise ValidationError('Operator must be in Mechanic group.')

        if self.building in building_info:
            if self.floor in building_info[self.building]:
                if self.room in building_info[self.building][self.floor]:
                    # if (self.room != "อื่นๆ"):      
                         pass
                    # else:
                    #     raise ValidationError('invalid room available room are {}'\
                    #     .format(list(building_info[self.building][self.floor])))
                else:
                    raise ValidationError('invalid room available room are {}'\
                        .format(list(building_info[self.building][self.floor])))
            else:
                raise ValidationError('invalid floor available floor are {}'\
                    .format(list(building_info[self.building])))
        else:
            raise ValidationError('invalid building available building are {}'\
                .format(list(building_info)))
        return True