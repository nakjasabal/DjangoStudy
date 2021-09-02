from django.shortcuts import render, get_object_or_404
from livepolls.models import Question, Choice
from django.urls import reverse
from django.http import HttpResponseRedirect #리다이렉트 기능을 위해 임포트

def main(request):
    num1 = 1
    num2 = 100
    hanStr = "안녕 하세요\r\n여기는 코스모 입니다"
    engStr = "Good 'morning' <strong>everyone</strong>"    
    # JSON 형식으로 템플릿으로 넘긴 데이터 저장
    context = {'num1':num1, 'num2':num2, 'hanStr':hanStr, 'engStr':engStr}
    return render(request, 'livepolls/main.html', context)

# index 화면 처리용 함수
# http://localhost:8000/livepolls 요청했을때 매핑되어 호출됨
def index(request): # request 객체는 뷰 함수의 필수 매개변수
    #Question 테이블에서 pub_date를 내림차순으로 최근 5개의 게시물을 가져온다.
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    #템플릿으로 데이터를 전달하기 위해 딕셔너리로 생성한다. 
    context = {'latest_question_list': latest_question_list}
    #render 함수를 통해 템플릿으로 context를 전달한다. 
    return render(request, 'livepolls/index.html', context)


'''
get_object_or_404(모델클래스, 검색조건1) 
    : 모델클래스에서 검색조건에 맞는 객체를 조회한다. 만약 조건에 
    맞는 객체가 없다면 Http404 예외를 발생시킨다. 
'''
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'livepolls/detail.html', {'question':question})



'''
Question 객체의 choice_set 속성
외래키 제약조건이 있는경우 부모테이블과 자식테이블 간에 서로 연결된 항목이라는 의미.

'''
def vote(request, question_id):
    #선택한 질문의 일련번호를 통해 레코드 가져옴
    question = get_object_or_404(Question, pk=question_id)
    try:
        #detail 페이지에서 선택한 항목을 통해 choices테이블에서 레코드 가져온다. 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #예외 발생시 설문 투표 폼을 다시 보여준다. 
        return render(request, 'livepolls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        #try절에서 가져온 레코드를 통해 votes항목을 업데이트 한후 저장한다. 
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데 이 터 를  정 상 적 으 로  처 리 하 였 으 면 ,
        # 항상 HttpResponseRedirect를  반환하여   리다이렉션  처 리함
        return HttpResponseRedirect(reverse('livepolls:results', args=(question.id,)))



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'livepolls/results.html', {'question':question})


