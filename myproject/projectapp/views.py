from django.shortcuts import render  # 템플릿을 렌더링하고, 컨텍스트 데이터를 포함해 HTML 응답을 생성하는 함수
from django.db import connection     # 렌더링 = 데이터와 템플릿(HTML 등)을 결합해 최종 웹 페이지를 생성하는 과정


def safe_search(request):
    query = request.POST.get('q', '')

    # 파라미터화된 쿼리로 SQL Injection 방지
    raw_query = "SELECT * FROM myapp_py5test WHERE name = %s"

    with connection.cursor() as cursor:    # 데이터베이스에 대한 커서를 열어 sql쿼리 실행 준비
        cursor.execute(raw_query, [query]) # 작성한 쿼리를 실행
        rows = cursor.fetchall()           # 쿼리 결과를 가져와서 rows 변수에 저장, fetchall()은 데이터베이스에서 모든 조회 결과를 가져올 때 사용하는 메서드

    # 템플릿에 결과 전달
    context = {             # 데이터를 저장하는 딕셔너리
        'rows': rows,
        'query': query,
    }
    return render(request, 'index.html', context)