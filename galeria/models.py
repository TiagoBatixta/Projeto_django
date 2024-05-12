from django.db import models

class fotografia(models.Model):
    
    OPECOES_CATEGORIA = [
        ("Nebulosa", "Nebulosa" ),
        ("Estrela", "Estrela" ),
        ("Galáxia", "Galáxia" ),
        ("Plaenta", "Plaenta"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=200 , null=False, blank=False)
    categoria = models.CharField(max_length=100, choices= OPECOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"