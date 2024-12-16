from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField() 

  def to_representation(self, instance):
    ret = super().to_representation(instance)
    ret.pop('password', None) 
    return ret

class AmilSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = amil
        fields = ('id', 'nama_amil', 'no_telp_amil')  # Atau tentukan fields yang diinginkan

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'password', 'id_role')
    extra_kwargs = {'password': {'write_only':True}}

  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user
  
class DistribusiPenerima(serializers.ModelSerializer):
  class Meta:
    model = penerima
    fields = ('nama_penerima', 'id_kategori', 'id_rekap', 'jml_penerima', 'nominal_total', 'tgl_penyaluran')

class BayarZakat(serializers.ModelSerializer):
  class Meta:
    model = zakat
    fields = '__all__'