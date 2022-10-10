from rest_framework import serializers
from .models import Bus,User,Book

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'bus_name','source','dest','nos','rem','price','date','time') 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id','email','name','password')

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('email','name','userid','busid','bus_name','source','dest','nos','price','date','time','status')