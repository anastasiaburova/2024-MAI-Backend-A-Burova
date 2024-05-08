from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название продукта")
    description = models.TextField(verbose_name="Описание продукта", blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    available = models.BooleanField(default=True, verbose_name="В наличии")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    address = models.CharField(max_length=200, verbose_name="Адрес", blank=True)

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders", verbose_name="Покупатель")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ #{self.pk}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name="Заказ")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items", verbose_name="Продукт")
    quantity = models.PositiveIntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

