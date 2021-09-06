from django.contrib import admin
from django.urls import path, include # 모듈 임포트
from livepolls import views

'''
path() 함수 : route, view 2개의 필수인자와, kwargs, name 2개의 선택인자를 받음.
    route : URL 패턴을 표현하는 문자열. URL스트링이라고 함.
    view : URL스트링이 매칭되면 호출되는 뷰 함수. HttpReuqest객체와 URL 
        스트링에서 추출된 항목이 뷰 함수의 인자로 전달됨
    kwargs : URL스트링에서 추출된 항목 외에 추가적인 인자를 뷰 함수에 전달할때,
        파이썬 사전 타입으로 인자를 정의함. 
    name : 각 URL 패턴별로 이름을 붙여준다. 여기서 정한 이름은 주로 템플릿
        에서 사용한다. 
'''
urlpatterns = [
    path('', views.main, name='main'), # http://localhost:8000/ 첫화면
    path('admin/', admin.site.urls), # 관리자모드

    #livepolls앱 : 1개의 urls파일로 만드는 경우
    #path('livepolls/', views.index, name='index'), # /livepolls/
    #path('livepolls/<int:question_id>/', views.detail, name='detail'), #/livepolls/5/
    #path('livepolls/<int:question_id>/results/', views.results, name='results'), #/livepolls/5/result/
    #path('livepolls/<int:question_id>/vote/', views.vote, name='vote'), #/livepolls/5/vote/

    #livepolls앱 : 2개의 urls파일로 만드는 경우
    path('livepolls/', include('livepolls.urls')), # 투표 애플리케이션 기본

    path('template.filter/', views.templateFilter), #템플릿 필터
    path('template.tag/', views.templateTag), #템플릿 태그
    path('form.create/', views.formCreate, name='formCreate'),  
    path('thanks/', views.thanks),  

    path('books/', include('books.urls')), # 도서관리 애플리케이션
]
