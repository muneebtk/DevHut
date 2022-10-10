from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None):
        if not email:
            raise ValueError('User must have a email address')
        if not first_name:
            raise ValueError('User must have a first name')

        user=self.model(
        email=self.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name,email,password):
        user=self.create_user(
        email=self.normalize_email(email),
        first_name=first_name,
        last_name=last_name,
        password=password,
        )
        user.is_active=True
        user.is_admin=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50,unique=True)
    phone_number=models.CharField(max_length=10,unique=True)
    is_liked = models.BooleanField(default=False)
    followers = models.IntegerField(default=0)
    is_followed = models.BooleanField(default=False)
    image = models.ImageField(upload_to = 'user',blank=True)
    about = models.TextField(null=True,blank=True)

    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects= MyAccountManager()

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True
