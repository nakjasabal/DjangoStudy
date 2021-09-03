from django import forms

'''
QuestionForm은 모델 폼(forms.ModelForm)을 상속했다. 
장고의 폼은 일반 폼(forms.Form)과 모델 폼(forms.ModelForm)이 있는데 
모델 폼은 모델(Model)과 연결된 폼으로 폼을 저장하면 연결된 모델의 데이터를 저장할수 있는 폼이다. 
모델 폼은 이너 클래스인 Meta 클래스가 반드시 필요하다. Meta 클래스에는 사용할 모델과 모델의 속성을 적어야 한다.
'''
class QuestionForm(forms.Form):
    user_id = forms.CharField(label='아이디', max_length=10) # 아이디 <input type=text max_length=10
    title = forms.CharField() # title <input type=text
    content = forms.CharField(widget=forms.Textarea) # content <textarea
    email = forms.EmailField() # email <input type=text
    my_check = forms.BooleanField(required=False) # my_check <input type=checkbox 
    
