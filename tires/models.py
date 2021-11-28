from django.db                  import models


class Tire(models.Model):
    trimid             = models.IntegerField()
    front_width        = models.IntegerField()
    front_aspect_ratio = models.IntegerField()
    front_wheel        = models.IntegerField()
    rear_width         = models.IntegerField()
    rear_aspect_ratio  = models.IntegerField()
    rear_wheel         = models.IntegerField()

    class Meta: 
        db_table = 'tires'

class UserTire(models.Model):
    user = models.ForeignKey('users.User' ,on_delete=models.CASCADE)
    tire = models.ForeignKey('tires.Tire', on_delete=models.SET_NULL, null=True)

    class Meta: 
        db_table = 'user_tires'
