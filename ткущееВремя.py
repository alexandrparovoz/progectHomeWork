# узнать текущее время в удобоваримом варианте
import datetime

now = datetime.datetime.now()
print(now.strftime('%y-%m-%d     %H:%M:%S'))