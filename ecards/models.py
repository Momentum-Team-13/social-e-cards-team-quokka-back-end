from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    def __str__(self):
        return self.username

class Card(models.Model):
    COMARANT_UNICASE = f"font-family: 'Cormorant Unicase', serif;"
    KAUSHAN_SCRIPT = f"font-family: 'Kaushan Script', cursive;"
    AMANTIC_SC = f"font-family: 'Amatic SC', cursive;"
    BUNGEE_SHADE = f"font-family: 'Bungee Shade', cursive;"
    RIGHTEOUS = f"font-family: 'Righteous', cursive;"
    JULIUS_SANS_ONE = f"font-family: 'Julius Sans One', sans-serif;"
    ROBOTO = f"font-family: 'Roboto', sans-serif;"
    SPECTRAL = f"font-family: 'Spectral', serif;"
    DANCING_SCRIPT = f"font-family: 'Dancing Script', cursive;"
    
    FONT_CHOICES = [
        (COMARANT_UNICASE, 'Cormorant Unicase'),
        (KAUSHAN_SCRIPT, 'Kaushan Script'),
        (AMANTIC_SC, 'Amatic SC'),
        (BUNGEE_SHADE, 'Bungee Shade'),
        (RIGHTEOUS, 'Righteous'),
        (JULIUS_SANS_ONE, 'Julius Sans One'),
        (ROBOTO, 'Roboto'),
        (SPECTRAL, 'Spectral'),
        (DANCING_SCRIPT, 'Dancing Script'),
    ]

    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name='cards')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255)
    font = models.TextField(choices=FONT_CHOICES, default=ROBOTO)
    font_color = models.TextField(null=True, blank=True)
    bg_color = models.TextField()
    border_color = models.TextField()
    border_style = models.TextField(null=True, blank=True)
    img_src = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_id} created a post at {self.created_at}"

class Follow(models.Model):
    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name='follows')
    follow_user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name='follows')

    def __str__(self):
        return f"{self.user_id} followed {self.follow_user_id}"