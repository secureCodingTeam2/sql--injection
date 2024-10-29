from django.shortcuts import render # 템플릿을 렌더링하고, 컨텍스트 데이터를 포함해 HTML 응답을 생성하는 함수
from django.db import connection    # 렌더링 = 데이터와 템플릿(HTML 등)을 결합해 최종 웹 페이지를 생성하는 과정

# urls.py 에서
def vulnerable_search(request):
    query = request.POST.get('q', '')
    raw_query = f"SELECT * FROM myapp_py5test WHERE name = '{query}'" #query 변수의 값을 직접 SQL 쿼리 문자열에 삽입

    with connection.cursor() as cursor:  # connection.cursor()를 통해 데이터베이스 연결을 설정, 상호작용할 수 있는 cursor 객체를 만듦
        cursor.execute(raw_query)        # raw_query에 저장된 SQL 쿼리를 데이터베이스에 전달하여 실행
        rows = cursor.fetchall()         # execute()로 조회된 쿼리 결과의 모든 행을 리스트 형태로 반환

    # 템플릿에 결과 전달
    context = {
        'rows': rows,      #조회된 결과를 rows 키에 저장
        'query': query,
    }

    # render 함수를 사용하여 요청을 처리하고, 'index.html' 템플릿과 함께 context 데이터를 기반으로 응답을 반환
    return render(request, 'index.html', context)