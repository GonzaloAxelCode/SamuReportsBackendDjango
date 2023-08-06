
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.set_password(password)
        user.save()
        Settings.objects.create(user=user)
        Profile.objects.create(user=user)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email,  password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nickname = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    photo_url = models.CharField(
        max_length=255, default="https://res.cloudinary.com/ddksrkond/image/upload/v1688411778/default_dfvymc.webp")
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    desactivate_account = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'first_name', 'last_name']
    SET_USERNAME_RETYPE = True
    USERNAME_RESET_SHOW_EMAIL_NOT_FOUND = False

    def __str__(self):
        return f"{self.nickname}"

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.nickname

    def get_short_name(self):
        return self.nickname


class Profile(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"Profile of {self.user.nickname}"


class Settings(models.Model):
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    email_notifications = models.BooleanField(default=True)
    theme_name = models.BooleanField(default=False)

    def __str__(self):
        return f"Settings of {self.user.nickname}"
