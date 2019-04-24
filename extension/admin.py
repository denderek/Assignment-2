from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
        (None, {'fields': ['question_text']}),
        (None, {'fields': ['correctAnswer'],'classes': ['collapse']}),]
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
