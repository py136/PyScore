from django.contrib import admin
from .models import ScoreEntries,Scores

# Register your models here.

admin.site.register(ScoreEntries)
admin.site.register(Scores)