import settings
# from django.db import models
from os import path
import os
new_path =  '\\'.join([settings.MEDIA_ROOT,'profiles'])
# os.rename('raman/views.png',new_path)
print(new_path)
# # class UploadModel(models.Model):
print(os.listdir('raman/'))
#     image = models.ImageField(upload_to='uploads')

#     def save(self, *args, **kwargs):

#         # Call standard save
#         super(UploadModel, self).save(*args, **kwargs)

#         if 'uploads' in self.image.path:

#             initial_path = self.image.path

#             # New path in the form eg '/images/uploadmodel/1/image.jpg'
#             new_name = '/'.join(['images', self._meta.model_name, str(self.id), 
#                 path.basename(initial_path)])
#             new_path = os.path.join(settings.MEDIA_ROOT, 'images', 
#             self._meta.model_name, self.pk, os.path.basename(initial_path))

#             # Create dir if necessary and move file
#             if not os.path.exists(os.path.dirname(new_path)):
#                 os.makedirs(os.path.dirname(new_path))

#             os.rename(initial_path, new_path)

#             # Update the image_file field
#             self.image_file.name = new_name

#             # Save changes
#             super(UploadModel, self).save(*args, **kwargs)