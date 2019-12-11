from django.db import models

# Create your models here.
class dbtest(models.Model):                    # dbtest는 클레스명
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    content=models.TextField()
    url=models.URLField()
    email=models.EmailField()
    cdate=models.DateTimeField(auto_now_add=True)

    def __str__(self):           ##외부에서 dbtest라는 클레스에 접근할 때 테이블의
        return self.name       ##이름을 반환해서 어떤 테이블인지 쉽게 알아 볼 수 있다.