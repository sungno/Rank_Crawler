from django.shortcuts import render
from chart_graph.models import rank_search



def chart_bar(request):
    return render(request, "chart_bar.html")


def chart_line(request):
    return render(request, "chart_line.html")


def chart(request):
    import pymysql
    dbCon = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='rank_test', charset='utf8')
    cursor = dbCon.cursor()

    # cursor = dbCon.cursor(pymysql.cursors.DictCursor)

    input_product = request.GET.get('input_product')
    input_keyword = request.GET.get('input_keyword')


    dic = {}
    for i in range(1, 6):
        dic[i] = request.GET.get(f'ext{i}')

    product = request.GET.get('product')



    with dbCon:
        # 제품명 인풋으로 받아 제품명에 있는 date값중 중복값 제외하고 가져오기
        cursor.execute("select distinct(date) from rank_search where product_name='{}' order by date".format(product))
        date_distinct = cursor.fetchall()

        # 제품명 인풋으로 받아 제품명에 있는 keyword 값중 중복값 제외하고 가져오기
        cursor.execute("select distinct(keyword) from rank_search where product_name='{}' order by keyword".format(product))
        keyword_distinct = cursor.fetchall()

        # 제품명 인풋으로 받아 제품명에 있는 product_name 값중 중복값 제외하고 가져오기
        cursor.execute("select distinct(product_name) from rank_search where product_name='{}'".format(product))
        product_distinct = cursor.fetchall()


        # 키워드를 인풋으로 입력받아 모든데이터 가져오기
        for n in range(1,6):
            cursor.execute("select total_rank,keyword from rank_search where keyword='{}'".format(dic[n]))
            dic[n] = cursor.fetchall()

        cursor.execute("select distinct keyword from rank_search where product_name='{}' order by keyword".format(product))
        keyword_data = cursor.fetchall()

        cursor.execute("select distinct keyword,date,total_rank from rank_search where product_name='{}' order by keyword;".format(input_product))
        product_data = cursor.fetchall()


        cursor.execute("select distinct(date) from rank_search where product_name='녹차카테킨' order by date")
        date_distinct2 = cursor.fetchall()
        cursor.execute("select distinct(keyword) from rank_search")


        cursor.execute("SELECT product_name, total_rank, date, keyword FROM rank_search order by date")
        graph = cursor.fetchall()






        # cursor.execute("select * from rank_search where keyword='장뇌삼가격' order by date")
        # graph_keyword3 = cursor.fetchall()
        cursor.execute("select * from rank_search where keyword='녹차다이어트' order by date")
        graph_keyword4 = cursor.fetchall()
        cursor.execute("select * from rank_search where keyword='다이어트' order by date")
        graph_keyword5 = cursor.fetchall()
        cursor.execute("select * from rank_search where keyword='카테킨' order by date")
        graph_keyword6 = cursor.fetchall()





    return render(request, "chart.html", {

        # for e in range(1,6):
        #     f'ext1{e}': dic[e]
        'ext1': dic[1],
        'ext2': dic[2],
        'ext3': dic[3],
        'ext4': dic[4],
        'ext5': dic[5],
        'ext_all': [dic[1], dic[2], dic[3], dic[4], dic[4]],

        'product': product,



        'date_distinct': date_distinct,
        'keyword_distinct': keyword_distinct,
        'product_distinct': product_distinct,



        'input_product': input_product,
        'input_keyword': input_keyword,


        'product_data': product_data,

        'graph': graph,



        'graph_keyword4': graph_keyword4,
        'graph_keyword5': graph_keyword5,
        'graph_keyword6': graph_keyword6,


        'date_distinct2': date_distinct2,

        'keyword_data': keyword_data,



    },)


