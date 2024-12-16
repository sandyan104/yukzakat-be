from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, id_role=None, **extra_fields ):
        if not email:
            raise ValueError('Email harus diisi!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.id_role = id_role
        user.save(using=self._db)
        return user
        
    
    def create_superuser(self, email, password=None, id_role=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, id_role, **extra_fields)

# Create your models here.

class role(models.Model):
    id_role = models.CharField(max_length=2, primary_key=True)
    nama_role = models.CharField(max_length=50)
    def __str__(self):
        return self.nama_role
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    id_role = models.ForeignKey(role, on_delete=models.CASCADE)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class amil(models.Model):
    id_amil = models.AutoField(primary_key=True)
    id = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    nama_amil = models.CharField(max_length=50)
    no_telp_amil = models.CharField(max_length=15)
    
    def __str__(self):
        return str(self.id_amil)
    
class artikel(models.Model):
    id_artikel = models.CharField(max_length=10, primary_key=True)
    judul = models.CharField(max_length=50)
    hero_image = models.ImageField(upload_to='artikel', null=True, blank=True)
    no_telp_amil = models.CharField(max_length=15)
    id_amil = models.ForeignKey(amil, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id_artikel)
    
class kategori_penerima(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id_kategori)
    
class rekap(models.Model):
    id_rekap = models.AutoField(primary_key=True)
    nama_rekap = models.CharField(max_length=50)
    id_amil = models.ForeignKey(amil, on_delete=models.CASCADE)
    total = models.IntegerField()
    tgl_awal = models.DateField()
    tgl_akhir = models.DateField()

    def __str__(self):
        return str(self.id_rekap)
    
class penerima(models.Model):
    id_penerima = models.AutoField(primary_key=True)
    nama_penerima = models.CharField(max_length=50)
    id_kategori = models.ForeignKey(kategori_penerima, on_delete=models.CASCADE)
    id_rekap = models.ForeignKey(rekap, on_delete=models.CASCADE)
    jml_penerima = models.IntegerField()
    nominal_total = models.IntegerField()
    tgl_penyaluran = models.DateField()
    def __str__(self):
        return str(self.id_penerima)
    
class tipe_zakat(models.Model):
    id_tipe = models.AutoField(primary_key=True)
    nama_zakat = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id_tipe)
    
class zakat(models.Model):
    choices = (
        ('P', 'Pria'),
        ('W', 'Wanita'),
    )

    id_zakat = models.AutoField(primary_key=True)
    nama_mz = models.CharField(max_length=50)
    jk_mz = models.CharField(choices=choices, max_length=1)
    no_telp_mz = models.CharField(max_length=15)
    email_mz = models.EmailField(max_length=50)
    tgl_Zakat = models.DateField()
    id_rekap = models.ForeignKey(rekap, on_delete=models.CASCADE)
    id_tipe = models.ForeignKey(tipe_zakat, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_zakat