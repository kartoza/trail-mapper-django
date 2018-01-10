# import hashlib
# import random
#
# from django.contrib.gis.db import models
# from django.utils.translation import ugettext_lazy as _
#
# class GUIDModel(models.Model):
#
#     guid = models.CharField(
#         _('GUID'),
#         null=True,
#         blank=True,
#         max_length=40
#     )
#
#     def save(self, *args, **kwargs):
#
#       if not self.guid:
#         self.guid = hashlib.sha1(str(random.random())).hexdigest()
#
#       super(GUIDModel, self).save(*args, **kwargs)