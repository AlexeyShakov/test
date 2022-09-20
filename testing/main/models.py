from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import uuid


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    # "_" means that this function works only internally, an ordinary client must not know about that
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('Email address must be provided')
 
        if not password:
            raise ValueError('Password must be provided')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user        

    def create_user(self, email=None, password=None, **kwargs):
        return self._create_user(email, password, **kwargs)
    
    def create_superuser(self, email, password, **kwargs):
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
 
        return self._create_user(email, password, **kwargs)  


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'  # USERNAME_FIELD means that authentication will require this field(email)

    # We have to define it, the documentation says so
    objects = UserAccountManager()

    email = models.EmailField('email', unique=True, blank=False, null=False)
    full_name = models.CharField('full name', blank=True, null=True, max_length=400)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_verified = models.BooleanField('verified', default=False) # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def get_short_name(self):
        return self.email
 
    def get_full_name(self):
        return self.email
 
    def __unicode__(self):
        return self.email




