
from curd.service import sites
from . import models


class UserInfoConfig(sites.CurdConfig):
    list_display = ['job_number', 'name']


sites.site.register(models.UserInfo, UserInfoConfig)
