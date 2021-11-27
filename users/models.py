from django.db                  import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, userid, password=None, **extra_field):
        if not userid:
            raise ValueError('Users must have an userid')

        user = self.model(
            userid = userid,
            **extra_field
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userid     = models.CharField(max_length=20, unique=True)
    is_admin   = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD  = 'userid'

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'users'