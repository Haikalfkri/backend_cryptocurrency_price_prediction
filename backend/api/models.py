from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

# Role Model
class Role(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

# User Manager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, role=None):
        if not email:
            raise ValueError('The Email field must be set')

        # set default role to user
        if role is None:
            role, _ = Role.objects.get_or_create(name='user')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        admin_role, _ = Role.objects.get_or_create(name='admin')

        user = self.create_user(username, email, password, role=admin_role)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class CryptoData(models.Model):
    coint_name = models.CharField(max_length=255)
    date = models.DateField()
    open = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        db_table = 'crypto_data'
        managed = False

    def __str__(self):
        return self.coint_name