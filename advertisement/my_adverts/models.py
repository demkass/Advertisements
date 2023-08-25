from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("Создано",auto_now_add=True)
    updated_at = models.DateTimeField("Обновлено",auto_now_add=True)
    category = models.SmallIntegerField("Категория")
    author = models.CharField("Автор", max_length=20)
    location = models.CharField("Локация товара", max_length=255)
    auction = models.BooleanField("Торг", help_text="Отметьте, если торг уместен.")
    user = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)
    photo = models.ImageField("Фото", upload_to="my_adverts",  blank=True, null=True)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f"<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price:.2f})>"
    
    @admin.display(description="Дата создания")
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.strftime ("%H:%M:%S")
            return format_html("""
            <span>Сегодня в {}</span>
            """, create_time)
        return self.created_at.strftime('%d.%m.%y в %H:%M:%S')
    
    @admin.display(description="Дата изменения")
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.strftime ("%H:%M:%S")
            return format_html("""
            <span>Сегодня в {}</span>
            """, update_time)
        return self.updated_at.strftime('%d.%m.%y в %H:%M:%S')
    


