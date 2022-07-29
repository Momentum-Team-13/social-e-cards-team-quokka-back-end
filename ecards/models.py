from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    following = models.ManyToManyField("User", related_name='followers', null=True, blank=True)
    def __str__(self):
        return self.username


class Card(models.Model):
    COMARANT_UNICASE = f"cormorant"
    KAUSHAN_SCRIPT = f"kaushan"
    AMANTIC_SC = f"amatic"
    BUNGEE_SHADE = f"bungee"
    RIGHTEOUS = f"righteous"
    JULIUS_SANS_ONE = f"julius"
    ROBOTO = f"roboto"
    SPECTRAL = f"spectral"
    DANCING_SCRIPT = f"dancing"

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

    WHITE = f"White"
    RED = f"Red"
    BLACK = f"Black"
    BLUE = f"Blue"
    GREEN = f"Green"
    YELLOW = f"Yellow"
    ORANGE = f"Orange"
    PURPLE = f"Purple"
    BROWN = f"Brown"

    COLOR_CHOICES = [
        (WHITE, 'white'),
        (RED, 'red'),
        (BLACK, 'black'),
        (BLUE, 'blue'),
        (GREEN, 'green'),
        (YELLOW, 'yellow'),
        (ORANGE, 'orange'),
        (PURPLE, 'purple'),
        (BROWN, 'brown'),
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
