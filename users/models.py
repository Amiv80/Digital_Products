import random

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, send_mail


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('username'), max_length=25, unique=True, 
                                help_text=_('Username must be at least 4 and at most 25 characters. It does not start with numbers or symbols'),
                                validators=[validators.RegexValidator(r'^[a-zA-Z][a-zA-Z0-9-\.]+$')],
                                error_messages={'unique':_('A user already exists.'),}
                                )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email'), unique=True, null=True, blank=True, max_length=254)
    phone_number = models.BigIntegerField(_('mobile number'), unique=True, null=True, blank=True,
                                          validators=[validators.RegexValidator(r'^989[0-3,9]\d{8}$')],
                                          error_messages={'unique':_('A phone number already exists.'),}
                                          )
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    date_join = models.DateTimeField(_('date joined'), default=timezone.now)
    last_seen = models.DateTimeField(_('last seen date'), null=True)

    objects = UserManager()

    USERNAME_FILED = 'username'
    REQUIRED_FIELDS = ['email', 'phone number']

    class Meta:
        db_table = 'users'
        verbose_name= _('user')
        verbose_name_plural= _('users')

    def get_full_name(self,):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip
    

    def get_short_name(self):
        return self.first_name
    

    def email_user(self, subject, message, from_email=None, **kwargs):
        return send_mail(subject, message, from_email, [self.email], **kwargs)
    

    @property
    def is_loggedin_user(self):
        return self.phone_number is not None or self.email is not None
    

    def save(self, *args, **kwargs):
        if self.email is not None and self.email.strip() == '':
            self.email = None
        super().save(*args, **kwargs)