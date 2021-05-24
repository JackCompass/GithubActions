from django.contrib import admin
from pipeline.models import RegisteredUsers

@admin.register(RegisteredUsers)
class AdminRegisteredUsers(admin.ModelAdmin):
	exclude = ('country',)
	list_display = ('username', 'age', 'country')

	def __str__(self):
		return f"{self.username}"

