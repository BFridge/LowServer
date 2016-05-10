from django.db import models

APK_NAME_MAX_LENGTH = 100
METHOD_NAME_MAX_LENGTH = 100
ARGS_MAX_LENGTH = 300

class Log(models.Model):
    apkName = models.CharField(max_length = APK_NAME_MAX_LENGTH)
    methodName = models.CharField(max_length = METHOD_NAME_MAX_LENGTH)
    args = models.CharField(max_length = ARGS_MAX_LENGTH)



