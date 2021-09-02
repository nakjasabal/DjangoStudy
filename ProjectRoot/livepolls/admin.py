from django.contrib import admin
from livepolls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
