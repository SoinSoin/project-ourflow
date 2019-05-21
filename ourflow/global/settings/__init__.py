from .base import *

DEBUG = False

if DEBUG:                          
   from .dev import *  
   pass
else:
   from .prod import * 
   pass