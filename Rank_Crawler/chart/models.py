# from django.db import models
#
#
# class rank_search(models.Model):
#     id = models.AutoField(db_column='id', primary_key=True)
#     product_name = models.CharField(db_column='product_name', max_length=20)
#     total_rank = models.IntegerField(db_column='total_rank')
#     date = models.CharField(db_column='date', max_length=20)
#     keyword = models.CharField(db_column='keyword', max_length=20)
#     keyword22 = models.CharField(db_column='keyword22', max_length=20)
#     keyword33 = models.CharField(db_column='keyword33', max_length=20)
#     keyword44 = models.CharField(db_column='keyword44', max_length=20)
#
#     class Meta:
#         managed = False
#         db_table = 'rank_search'
#
#     def __str__(self):
#         return str(self.product_name) + "," + self.total_rank + "," + str(self.date) + "," + str(self.keyword)
