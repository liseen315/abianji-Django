from django.contrib.admin import AdminSite
from blog.admin import *
class AbianjiAdminSite(AdminSite):
    site_header = 'Abianji 管理后台'
    site_title = '阿比安吉 admin'
    def __init__(self,name='admin'):
        super().__init__(name)
    def has_permission(self, request):
        return request.user.is_superuser

admin_site = AbianjiAdminSite(name='admin')
admin_site.register(Setting,BlogSettingAdmin)