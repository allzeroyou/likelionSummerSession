from django.db import models

# Create your models here.
class Blog(models.Model): #상속받음: 상속받을 부모 클래스에 있는 모든 메소드, 속성 쓸 수 있음 따라서 따로 id 작성하지 않아도
  title=models.CharField(max_length=200)
  writer=models.CharField(max_length=100)
  pub_date =models.DateTimeField()
  body=models.TextField() #제한없음
  image=models.ImageField(upload_to="blog/", blank=True, null=True)
  #비어 있다고 blank,null=True 라고 코드를 꼭 적어줘야! 안하면 안했다고 화를 냄=오류발생/실제 사진 저장x, 사진이 있는 경로 저장(url)
  def __str__(self):
    return self.title

  def summary(self):
    return self.body[:100]
    
