__author__ = 'Fridge'
from  rest_framework import serializers
from models import *

class  LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        field = ('apkName',  'methodName', 'args')