from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.core.exceptions import ValidationError

class Event(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)  # 一旦nullを許可
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Request(models.Model):
    LOCATION_CHOICES = [
        ('onsite', '出張'),
        ('moca', '下津カフェMOCA'),
    ]

    name = models.CharField(max_length=255, verbose_name="名前")
    start_time = models.DateTimeField(verbose_name="開始時間")
    end_time = models.DateTimeField(verbose_name="終了時間")
    treatment_location = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name="施術場所")

    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="電話番号")
    email = models.EmailField(blank=True, null=True,  verbose_name="メールアドレス")
    email_confirm = models.EmailField(blank=True, null=True, verbose_name="メールアドレス(確認)")
    
    comment = models.TextField(blank=True, null=True, verbose_name="コメント")  # コメントフィールドを追加

    def clean(self):
        # 電話番号かメールアドレスのどちらか一方が必須
        if not self.phone_number and not self.email:
            raise ValidationError('電話番号かメールアドレスのどちらか一方を入力してください。')

        # メールアドレスの一致を確認
        if self.email and self.email_confirm and self.email != self.email_confirm:
            raise ValidationError("メールアドレスが一致しません。再度確認してください。")

    def __str__(self):
        return self.name
    

class Notice(models.Model):
    title = models.CharField(max_length=200)  # お知らせのタイトル
    content = models.TextField()  # お知らせの内容
    date = models.DateField()  # お知らせの日付、自動的に現在の日付が保存される

    def __str__(self):
        return self.title