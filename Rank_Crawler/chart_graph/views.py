from django.shortcuts import render
from chart_graph.models import rank_search



def chart_bar(request):
    return render(request, "chart_bar.html")


def chart_line(request):
    return render(request, "chart_line.html")


def chart_bar2(request):
    import pymysql
    dbCon = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='rank_test', charset='utf8')
    cursor = dbCon.cursor()

    with dbCon:
        cursor.execute('SELECT product_name, total_rank, date, keyword FROM rank_search')
        graph = cursor.fetchall()
        cursor.execute("select * from rank_search where keyword='산삼'")
        graph_keyword = cursor.fetchall()

    return render(request, "chart_bar2.html", {
        'title': '상품 순위',
        'dititle': '몰라',
        'dititle': '몰라2',
        'graph': graph,
        'graph_keyword': graph_keyword
    })


