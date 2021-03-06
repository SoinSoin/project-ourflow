import os
import time
from django.conf import settings
def definer_root(instance, filename,*args, **kwargs):
    try:
        name, ext = os.path.splitext(filename)
        list_ext = ['.jpg', '.jpeg', '.svg', '.png', '.pdf','.JPG','.gif']
        if ext in list_ext:
            if ext == '.pdf':
                upload_dir = os.path.join('public/uploads',time.strftime("%Y"),'pdf')
                media_dir = os.path.join(getattr(settings, "BASE_DIR", None), upload_dir)
            else: 
                upload_dir = os.path.join('public/uploads',time.strftime("%Y"),'images')
                media_dir = os.path.join(getattr(settings, "BASE_DIR", None), upload_dir)
        else:
            return None
        if not os.path.exists(media_dir):
            os.makedirs(media_dir)
        return os.path.join(media_dir, filename)
    except:
        return None