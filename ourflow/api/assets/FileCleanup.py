import os

def file_cleanup_delete(sender, instance, **kwargs):
	if instance.media_item:
		delete_file(instance.media_item.path)

def file_cleanup_upload(sender, instance, **kwargs):
	if not instance.pk:
		return False
	try:
		old_file = sender.objects.get(pk=instance.pk).media_item
	except sender.DoesNotExist:
		return False
	new_file = instance.media_item
	if not old_file == new_file:
		delete_file(old_file.path)	

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)
