from django.contrib import admin
from livepolls.models import Question, Choice

#admin 페이지에 보이도록 등록
admin.site.register(Question)
admin.site.register(Choice)
