# from django.shortcuts import render
# from chart.models import rank_search
# import pymysql
#
#
# def chart_bar(request):
#
#     return render(request, "chart_bar.html")
#
# def chart_line(request):
#
#     return render(request, "chart_line.html")
#
# def chart_bar2(request):
#     dbCon = pymysql.connect('127.0.0.1', 'root', 'root', 'rank_test')
#     cursor = dbCon.cursor()
#
#     with dbCon:
#         cursor.execute('SELECT product_name, total_rank, date, keyword FROM rank_search')
#         graph = cursor.fetchall()
#
#     return render(request,"chart",{
#         'title': '상품 순위',
#         'dititle': '몰라',
#         'dititle': '몰라2',
#         'graph': graph
#     })
#
#
