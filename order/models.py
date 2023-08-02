from django.db import models

# Create your models here.
class Shop(models.Model) :
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)


# 음식점 메뉴 관련
class Menu(models.Model) :
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)

# 특정 사용자가 주문한 내역
class Order(models.Model) :
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateField('date ordered')
    address = models.CharField(max_length=40)
    estimated_time = models.IntegerField(default=-1) # 예상 시간 사장님이 입력해야 됨.
    deliver_finish = models.BooleanField(default=0)

# 주문 음식
class Orderfood(models.Model) :
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)