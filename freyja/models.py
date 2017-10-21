from django.db import models
from django.contrib.auth.models import User


class Log(models.Model):
    user = models.ForeignKey(User)
    refer = models.CharField('请求路径', max_length=256)
    operation = models.SmallIntegerField('操作类型 0:create 1:update 2:delete')
    resource_id = models.IntegerField('资源名称')
    resource_type = models.SmallIntegerField('资源类型 0:图片')
    pre_val = models.TextField('操作前记录')
    aft_val = models.TextField('操作后记录')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    OPER_CREATE = 0
    OPER_UPDATE = 1
    OPER_DELETE = 2

    class Meta:
        db_table = 'log'