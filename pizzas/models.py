from django.db import models

class Pizza(models.Model):
    """pizza를 정의한다."""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        "모델에 관한 정보를 문자열 형태로 변환한다."
        return self.name

class Topping(models.Model):
    """피자의 토핑에 대해 정의했다."""
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    name = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 변환한다."""
        if self.name[:] > self.name[:50]:
            return self.name[:50] + "..."
        else:
            return self.name[:]
