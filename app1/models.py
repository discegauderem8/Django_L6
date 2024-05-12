from django.db import models

# Create your models here.

class Games (models.Model):

    side = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Монетка со стороной {self.side} выпала в {self.created_at}"

    @staticmethod
    def get_stats(n):
        games = Games.objects.all().order_by("-id")[:n]

        result = {"орёл": 0, "решка": 0}

        for i in games:
            if str(i.side) == "орёл":
                result["орёл"] += 1
            else:
                result["решка"] += 1

        return result


