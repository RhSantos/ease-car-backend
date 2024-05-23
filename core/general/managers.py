from django.contrib.auth.models import BaseUserManager


class ProfileUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        profile_user = self.model(email=email, **extra_fields)
        profile_user.set_password(password)
        profile_user.profile_pic = extra_fields.get("profile_pic")
        profile_user.address = extra_fields.get("address")
        profile_user.save(using=self._db)
        return profile_user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)
