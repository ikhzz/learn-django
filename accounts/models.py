from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from uuid import uuid4

class AccountsManager(BaseUserManager):
  def create_user(self, email, username=None, password=None):
    if not email:
      raise ValueError("Email is required")
    user = self.model(
      email = self.normalize_email(email),
      username = username,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_superuser(self, email, password=None):
    user = self.create_user(
      email,
      password = password,
    )
    user.is_admin = True
    user.save(using=self._db)
    return user

def fileUpload():
  # should try upload to database storage
  filename = uuid4().hex
  return 'assets/img/'+filename

def imageDefault():
  return 'assets/img/default.jpg'

# Create your models here.
class Accounts(AbstractBaseUser):
  # required property, password and hash is built in
  email = models.EmailField(unique=True)
  username = models.CharField(max_length=50)
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(auto_now=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)  

  profile_image = models.ImageField(null=True, blank=True, default=imageDefault, upload_to=fileUpload)
  role = models.CharField(default="costumer", max_length=8)
  
  objects = AccountsManager()

  # set login field as email
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def has_perm(self, perm, obj=None):
    return self.is_admin

  def has_module_perms(self, app_label):
    return True

  def __str__(self):
      return self.username

  #required property as method
  @property
  def is_staff(self):
    return self.is_admin

  @property
  def is_superuser(self):
    return self.is_admin