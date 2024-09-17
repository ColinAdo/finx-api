# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from accounts.models import CustomUser
# from profiles.models import Profile

# # Create profile signal
# @receiver(post_save, sender=CustomUser)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(owner=instance)
