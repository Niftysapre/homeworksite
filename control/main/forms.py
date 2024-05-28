from django import forms
from .models import *

class checking(forms.Form):
    date = forms.DateField(widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}), label="Дата")
    lessons = forms.ModelChoiceField(queryset=lesson.objects.all(), label="Урок")
    groups = forms.ModelChoiceField(queryset=group.objects.all(), label="Класс")
    students = forms.ModelMultipleChoiceField(
                        queryset= student.objects.values_list('second_name', flat=True),
                        label="Ученики",
                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'filterDiv'}))

class marks(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lesson'].empty_label = 'Урок не выбран'
        self.fields['group'].empty_label = 'Класс не выбран'

    class Meta:
        model = mark
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'class': 'form-control lessonday', 'type':'date'}), 
            'student': forms.CheckboxSelectMultiple(attrs={'class': 'filterDiv'}),

        }
class markss(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = marking
        fields = '__all__'
    widgets = {
        'student': forms.CheckboxSelectMultiple()}