from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    following = models.ManyToManyField("User", related_name='followers')
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

    WHITE = f"#FFFFFF"
    RED = f"#FF0000"
    BLACK = f"#000000"
    BLUE = f"#0086FF"
    GREEN = f"#04D61F"
    YELLOW = f"#FFFD00"
    ORANGE = f"#FF7F00"
    PURPLE = f"#D100FF"
    BROWN = f"#845A0F"

    COLOR_CHOICES = [
        (WHITE, 'White'),
        (RED, 'Red'),
        (BLACK, 'Black'),
        (BLUE, 'Blue'),
        (GREEN, 'Green'),
        (YELLOW, 'Yellow'),
        (ORANGE, 'Orange'),
        (PURPLE, 'Purple'),
        (BROWN, 'Brown'),
    ]

    user_id = models.ForeignKey("User", on_delete=models.CASCADE, related_name='cards')
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    message = models.CharField(max_length=255)
    font = models.TextField(choices=FONT_CHOICES, default=ROBOTO)
    font_color = models.TextField(choices=COLOR_CHOICES, default=BLACK)
    bg_color = models.TextField(choices=COLOR_CHOICES, default=WHITE)
    border_color = models.TextField(choices=COLOR_CHOICES, default=BLACK)
    border_style = models.TextField(null=True, blank=True)
    img_src = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user_id} created a post at {self.created_at}"
