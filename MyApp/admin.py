from django.contrib import admin
from models import Users, UserScore

# Register your models here.
class MemeMoryGameAdminPage(admin.AdminSite):
    # Changing the title and the header title of the admin page
    site_header = "Meme-mory Admin Page"


admin_site = MemeMoryGameAdminPage(name = "AdminPage")

admin_site.register(Users)
admin_site.register(UserScore)

