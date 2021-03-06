
from django.contrib import admin
# Register your models here.


from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    list_display = ['choice_text', 'question']
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date', 'ccc']
    #fields = ['pub_date', 'question_text'] #控制顺序
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('日期信息', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline] # 如果这个inlines不写 那修改question的时候不会显示choice列表
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)