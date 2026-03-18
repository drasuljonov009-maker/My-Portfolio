from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',       models.CharField(max_length=100, verbose_name="Ism-familiya")),
                ('role',       models.CharField(max_length=100, verbose_name="Kasb/Rol")),
                ('bio',        models.TextField(verbose_name="Bio")),
                ('location',   models.CharField(max_length=100, verbose_name="Joylashuv")),
                ('email',      models.EmailField(verbose_name="Email")),
                ('github',     models.URLField(blank=True, verbose_name="GitHub URL")),
                ('telegram',   models.URLField(blank=True, verbose_name="Telegram URL")),
                ('linkedin',   models.URLField(blank=True, verbose_name="LinkedIn URL")),
                ('experience', models.CharField(default='1+ yil', max_length=50, verbose_name="Tajriba")),
            ],
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profil'},
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id',    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num',   models.CharField(max_length=20, verbose_name="Raqam")),
                ('label', models.CharField(max_length=50, verbose_name="Izoh")),
                ('icon',  models.CharField(default='fa-star', max_length=60, verbose_name="FA icon class")),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")),
            ],
            options={'verbose_name': 'Statistika', 'verbose_name_plural': 'Statistikalar', 'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id',    models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon',  models.CharField(default='fa-solid fa-code', max_length=80, verbose_name="FA icon class")),
                ('name',  models.CharField(max_length=100, verbose_name="Nomi")),
                ('level', models.PositiveSmallIntegerField(default=70, verbose_name="Daraja (0-100)")),
                ('tags',  models.CharField(blank=True, max_length=255, verbose_name="Teglar (vergul bilan)")),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")),
            ],
            options={'verbose_name': "Ko'nikma", 'verbose_name_plural': "Ko'nikmalar", 'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id',      models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150, verbose_name="Kompaniya")),
                ('role',    models.CharField(max_length=100, verbose_name="Lavozim")),
                ('period',  models.CharField(max_length=60, verbose_name="Davr")),
                ('type',    models.CharField(default='Full-time', max_length=60, verbose_name="Ish turi")),
                ('desc',    models.TextField(verbose_name="Tavsif")),
                ('tags',    models.CharField(blank=True, max_length=255, verbose_name="Teglar")),
                ('order',   models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")),
            ],
            options={'verbose_name': 'Tajriba', 'verbose_name_plural': 'Tajribalar', 'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id',     models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150, verbose_name="O'quv muassasasi")),
                ('field',  models.CharField(max_length=150, verbose_name="Yo'nalish")),
                ('period', models.CharField(max_length=60, verbose_name="Davr")),
                ('icon',   models.CharField(default='fa-graduation-cap', max_length=60, verbose_name="FA icon class")),
                ('desc',   models.TextField(verbose_name="Tavsif")),
                ('order',  models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")),
            ],
            options={'verbose_name': "Ta'lim", 'verbose_name_plural': "Ta'lim", 'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id',          models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num',         models.CharField(max_length=5, verbose_name="Raqam")),
                ('category',    models.CharField(max_length=80, verbose_name="Kategoriya")),
                ('name',        models.CharField(max_length=150, verbose_name="Nomi")),
                ('desc',        models.TextField(verbose_name="Tavsif")),
                ('stack',       models.CharField(blank=True, max_length=255, verbose_name="Texnologiyalar")),
                ('github',      models.URLField(blank=True, verbose_name="GitHub havolasi")),
                ('badge',       models.CharField(blank=True, max_length=50, verbose_name="Holat")),
                ('badge_color', models.CharField(choices=[('green', 'Yashil'), ('orange', "To'q sariq"), ('blue', "Ko'k")], default='green', max_length=20, verbose_name="Badge rangi")),
                ('order',       models.PositiveSmallIntegerField(default=0, verbose_name="Tartib")),
            ],
            options={'verbose_name': 'Loyiha', 'verbose_name_plural': 'Loyihalar', 'ordering': ['order']},
        ),
    ]
