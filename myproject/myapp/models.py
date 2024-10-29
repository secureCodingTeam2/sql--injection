from django.db import models # models: 데이터베이스 테이블을 Python 코드로 정의하는 곳


class py5test(models.Model):
    name = models.CharField(max_length=100)   # name은 최대100자까지 문자열 저장 필드
    score = models.IntegerField()             # score은 정수값 저장 필드

    # 객체를 문자열로 표현
    def __str__(self):    # self : 현재 객체를 참조.
        return self.name  # 객체가 문자열로 변환될 때, 이 객체의 name 필드 값이 반환

'''
   (9, 10)예시
   객체 생성
   student1 = py5test(name="Alice", score=95)
   student2 = py5test(name="Bob", score=85)

   객체를 문자열로 출력
    print(student1)  # 출력 결과: "Alice"
    print(student2)  # 출력 결과: "Bob
'''