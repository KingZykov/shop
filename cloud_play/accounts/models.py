from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError('The Login must be set')
        login = self.normalize_email(login)
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        user = self.create_user(login, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    login = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10)
    last_login = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    # Эти поля встроены в PermissionsMixin, но надо добавить related_name, чтобы избежать конфликтов
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # изменить related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',  # изменить related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
      #  managed = False  # Django не будет создавать или изменять таблицу

    def __str__(self):
        return self.login

    @property
    def is_staff(self):
        return self.role == 'admin'
