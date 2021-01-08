

from stark.service.sites import  site
from app02.models import Food

site.register(Food)
print("------>",site._registry)