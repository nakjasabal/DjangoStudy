import django
from django.shortcuts import render
# 클래스형 제네릭뷰를 사용하기 위해 3가지 뷰를 임포트
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
# 레코드 조회를 위한 모델 클래스 임포트
from books.models import Book, Author, Publisher


# TemplateView 사용 : books 애플리케이션의 첫화면을 출력
class BooksModelView(TemplateView):
    # TemplateView를 사용하는 경우 template_name 클래스변수를 오버라이딩 해야한다.
    template_name = 'books/index.html' # 템플릿 파일 지정

    # 아우~자동완성 되네..
    # 템플릿으로 전달할 데이터가 있는경우 get_context_data() 메서드를 오버라이딩 한다.
    def get_context_data(self, **kwargs):
        # 오버라이딩 하는 경우 반드시 super()를 첫줄에 선언
        context = super().get_context_data(**kwargs)
        # 템플릿으로 전달한 데이터 저장
        context['model_list'] = ['Book', 'Author', 'Publisher']
        # return도 필수적
        return context

# ListView 제네릭 뷰를 사용. 
'''
ListView를 상속받는 경우 해당 모델 클래스를 템플릿으로 전달하는것만으로
리스트구성, 컨텍스트변수 저장 및 전달이 자동으로 처리된다. 
또한 디폴트로 지정되는 2가지가 있는데 
첫째 컨텍스트 변수로 object_list를 사용함
둘째 템플릿 파일명은 모델명소문자_list.html로 지정된다. 
'''
class BookList(ListView):
    # 1.Book 테이블로 부터 모든 레코드를 가져와서 컨텍스트변수 object_list를 생성
    # 2.템플릿 파일은 'books/book_list.html' 이와같이 지정되어 컨텍스트 변수가 전달됨
    model = Book

class AuthorList(ListView):
    # BookList와 동일한 패턴
    model = Author

class PublisherList(ListView):
    # BookList와 동일한 패턴
    model = Publisher

# DetailView 제네릭 뷰를 사용
'''
DetailView를 상속하는 경우 특정 레코드 하나를 조회한후 컨텍스트 변수에 저장한다.
URLconf에서 지정한 파라미터를 통해 특정 레코드 하나를 조회한 후 템플릿으로 전달한다.
'''
class BookDetail(DetailView):
    '''
    URLconf => path('book/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    /book/100/ 과 같이 요청되었다면 100 레코드를 조회한다. 
    컨텍스트 변수 object에 저장한 후 템플릿 파일 '모델명소문자_detail.html'로 전달한다.
    템플릿 경로는 'books/book_detail.html'와 같다. 
    '''
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher

