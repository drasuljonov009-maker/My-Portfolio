from django.db import models


class Profile(models.Model):
    """Shaxsiy ma'lumotlar — faqat 1 ta yozuv bo'ladi"""
    name        = models.CharField(max_length=100, verbose_name="Ism-familiya")
    role        = models.CharField(max_length=100, verbose_name="Kasb/Rol")
    bio         = models.TextField(verbose_name="Bio (o'zingiz haqingizda)")
    location    = models.CharField(max_length=100, verbose_name="Joylashuv")
    email       = models.EmailField(verbose_name="Email")
    github      = models.URLField(blank=True, verbose_name="GitHub URL")
    telegram    = models.URLField(blank=True, verbose_name="Telegram URL")
    linkedin    = models.URLField(blank=True, verbose_name="LinkedIn URL")
    experience  = models.CharField(max_length=50, default="1+ yil", verbose_name="Tajriba (masalan: 1+ yil)")

    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profil"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Faqat 1 ta profil bo'lishi uchun
        self.pk = 1
        super().save(*args, **kwargs)


class Stat(models.Model):
    """Statistika raqamlari (Hero bo'limidagi)"""
    num     = models.CharField(max_length=20, verbose_name="Raqam (masalan: 10+)")
    label   = models.CharField(max_length=50, verbose_name="Izoh (masalan: Loyihalar)")
    icon    = models.CharField(max_length=60, default="fa-star", verbose_name="Font Awesome icon class")
    order   = models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistikalar"
        ordering = ['order']

    def __str__(self):
        return f"{self.num} — {self.label}"


class Skill(models.Model):
    """Ko'nikmalar / Texnologiyalar"""
    icon    = models.CharField(max_length=80, default="fa-solid fa-code", verbose_name="Font Awesome icon class")
    name    = models.CharField(max_length=100, verbose_name="Texnologiya nomi")
    level   = models.PositiveSmallIntegerField(default=70, verbose_name="Daraja (0–100%)")
    tags    = models.CharField(max_length=255, blank=True, verbose_name="Teglar (vergul bilan, masalan: Django,DRF,ORM)")
    order   = models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Ko'nikma"
        verbose_name_plural = "Ko'nikmalar"
        ordering = ['order']

    def __str__(self):
        return self.name

    def tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Experience(models.Model):
    """Ish tajribasi"""
    company = models.CharField(max_length=150, verbose_name="Kompaniya / Ish joyi")
    role    = models.CharField(max_length=100, verbose_name="Lavozim")
    period  = models.CharField(max_length=60, verbose_name="Davr (masalan: 2024 — hozir)")
    type    = models.CharField(max_length=60, default="Full-time", verbose_name="Ish turi")
    desc    = models.TextField(verbose_name="Tavsif")
    tags    = models.CharField(max_length=255, blank=True, verbose_name="Teglar (vergul bilan)")
    order   = models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Tajriba"
        verbose_name_plural = "Tajribalar"
        ordering = ['order']

    def __str__(self):
        return f"{self.company} — {self.role}"

    def tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Education(models.Model):
    """Ta'lim"""
    school  = models.CharField(max_length=150, verbose_name="O'quv muassasasi")
    field   = models.CharField(max_length=150, verbose_name="Yo'nalish / Mutaxassislik")
    period  = models.CharField(max_length=60, verbose_name="Davr (masalan: 2023 — 2024)")
    icon    = models.CharField(max_length=60, default="fa-graduation-cap", verbose_name="Font Awesome icon class")
    desc    = models.TextField(verbose_name="Tavsif")
    order   = models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Ta'lim"
        verbose_name_plural = "Ta'lim"
        ordering = ['order']

    def __str__(self):
        return f"{self.school} — {self.field}"


BADGE_COLORS = [
    ('green',  'Yashil (Tugallangan)'),
    ('orange', 'To\'q sariq (Jarayonda)'),
    ('blue',   'Ko\'k (Yangi)'),
]

class Project(models.Model):
    """Loyihalar"""
    num          = models.CharField(max_length=5, verbose_name="Raqam (masalan: 01)")
    category     = models.CharField(max_length=80, verbose_name="Kategoriya (masalan: Veb-ilova)")
    name         = models.CharField(max_length=150, verbose_name="Loyiha nomi")
    desc         = models.TextField(verbose_name="Tavsif")
    stack        = models.CharField(max_length=255, blank=True, verbose_name="Texnologiyalar (vergul bilan)")
    github       = models.URLField(blank=True, verbose_name="GitHub havolasi")
    badge        = models.CharField(max_length=50, blank=True, verbose_name="Holat (masalan: Tugallangan)")
    badge_color  = models.CharField(max_length=20, choices=BADGE_COLORS, default='green', verbose_name="Badge rangi")
    order        = models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['order']

    def __str__(self):
        return self.name

    def stack_list(self):
        return [t.strip() for t in self.stack.split(',') if t.strip()]
