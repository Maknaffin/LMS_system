from django.conf import settings
from django.db import models


NULLABLE = {"blank": True, "null": True}

PAY_CASH = "Наличные"
PAY_CARD = "Карта"

PAYMENT_CHOICES = (
    ("PAY_CASH", "Наличные"),
    ("PAY_CARD", "Карта"),
)


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="название урока")
    image = models.ImageField(verbose_name="картинка урока", **NULLABLE)
    description = models.TextField(verbose_name="описание урока", **NULLABLE)
    link_to_video = models.URLField(verbose_name="ссылка на видео", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )
    course = models.ForeignKey(
        "Course", on_delete=models.CASCADE, related_name="lesson", verbose_name="курс", **NULLABLE
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="название курса")
    image = models.ImageField(verbose_name="картинка курса", **NULLABLE)
    description = models.TextField(verbose_name="описание курса", **NULLABLE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="пользователь", **NULLABLE
    )

    def __str__(self):
        return f"{self.title} {self.description}"

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Payment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name="пользователь", **NULLABLE,
        related_name="payment",
    )
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name="дата оплаты")
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="оплаченный урок", **NULLABLE
    )
    payment_amount = models.PositiveIntegerField(verbose_name="сумма оплаты")
    payment_method = models.CharField(
        choices=PAYMENT_CHOICES, default=PAY_CARD, max_length=10, verbose_name="способ оплаты"
    )

    def __str__(self):
        return (f"{self.user}: {self.paid_course if self.paid_course else self.paid_lesson} - "
                f"{self.payment_amount}")

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
