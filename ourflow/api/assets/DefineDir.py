import os
import time
def definer_root(instance, filename,*args, **kwargs):
    name, ext = os.path.splitext(filename)
    list_ext = ['.jpg', '.jpeg', '.svg', '.png', '.pdf','.JPG']
    if ext in list_ext:
        if ext == '.pdf':
            upload_dir = os.path.join('uploads',time.strftime("%Y"),'pdf')
        else: 
            upload_dir = os.path.join('uploads',time.strftime("%Y"),'images')
    else:
        return "<p>votre fichier n'est pas au format image ou pdf</p>"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return os.path.join(upload_dir, filename)