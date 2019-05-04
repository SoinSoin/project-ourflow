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
            else: 
                upload_dir = os.path.join('public/uploads',time.strftime("%Y"),'images')
        else:
            return None
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        return os.path.join(upload_dir, filename)
    except:
        return None