from django.db import models

"""
장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은
클래스의 변수로 매핑한다. 
django.db.models.Model클래스를 상속받아 정의하고, 각 클래스 변수의
타입도 장고에서 미리 정의된 필드 클래스를 사용한다. 
"""

#Question 테이블 생성
class Question(models.Model):
    '''
    PK는 별도로 지정하지 않아도 자동으로 생성된다. 컬럼명은 id로 
    not null과 Autoincrement 제약조건이 지정된다. 
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') #일종의 설명문

    '''
    객체를 문자열로 표현할 때 사용한다. 해당 메소드를 정의하지 않으면
    테이블명이 제대로 표시되지 않는다. 
    '''
    def __str__(self):
        return self.question_text

#Choice 테이블 생성
class Choice(models.Model):
    '''
    FK는 항상 부모 테이블의 PK와 연결되므로 Question 클래스만 지정하면된다. 
    FK로 지정된 컬럼은 자동으로 _id 접미사가 붙게된다. 
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
