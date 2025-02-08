from django.contrib import admin
from check.models import Score_all,Score_Topics,Scores_Histories

# Register your models here.
admin.site.register(Score_all)
admin.site.register(Score_Topics)
admin.site.register(Scores_Histories)