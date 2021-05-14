from django.db import models
from rooms.models import Room

class Active_Room_query(models.QuerySet):
    def active(self):
        return self.filter(active=True)


class Active_Room_Maneger(models.Manager):
    def get_queryset(self):
        return Active_Room_query(
            model=self.model,
            using=self._db,
            hints=self._hints
            )
    def active(self):
        return self.get_queryset().active()
    
    

class Active_Room(Room):
    objects = Active_Room_Maneger()
    class Meta:
        proxy = True
        verbose_name = 'Active Rooms'
        verbose_name_plural = 'Active Rooms'
        
