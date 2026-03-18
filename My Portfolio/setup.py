"""
Bu skriptni bir marta ishga tushiring:
  python setup.py

Nima qiladi:
  1. Migratsiyalarni qo'llaydi
  2. Superuser yaratadi (admin / admin123)
  3. Boshlang'ich ma'lumotlarni kiritadi
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User
from portfolio.models import Profile, Stat, Skill, Experience, Education, Project

# 1. Migrate
print("⏳ Migratsiyalar qo'llanmoqda...")
call_command('migrate', verbosity=0)
print("✅ Migrate — bajarildi")

# 2. Superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'drasuljonov345@gmail.com', 'admin123')
    print("✅ Superuser yaratildi → login: admin | parol: admin123")
else:
    print("ℹ️  Superuser allaqachon mavjud")

# 3. Seed data
if not Profile.objects.exists():
    Profile.objects.create(
        name="Rasuljonov Dostonbek",
        role="Backend Developer",
        bio="Backend dasturlash sohasida ixtisoslashgan dasturciman. Python va Django yordamida ishonchli, tezkor va kengaytiriladigan veb-ilovalar va API'lar yarataman. Telegram botlar va ma'lumotlar bazasi optimizatsiyasiga qiziqaman.",
        location="Toshkent, O'zbekiston",
        email="drasuljonov345@gmail.com",
        github="https://github.com/drasuljonov345-wq",
        telegram="https://t.me/Rasuljonov_009",
        experience="1+ yil",
    )
    print("✅ Profil yaratildi")

if not Stat.objects.exists():
    stats = [
        ("1+",   "Yil tajriba",    "fa-briefcase",   0),
        ("10+",  "Loyihalar",      "fa-code",        1),
        ("4",    "Texnologiyalar", "fa-layer-group", 2),
        ("100%", "Mas'uliyat",     "fa-fire",        3),
    ]
    for num, label, icon, order in stats:
        Stat.objects.create(num=num, label=label, icon=icon, order=order)
    print("✅ Statistikalar yaratildi")

if not Skill.objects.exists():
    skills = [
        ("fa-brands fa-python",   "Python",       85, "Python 3,OOP,Asyncio,Scripting",          0),
        ("fa-solid fa-globe",     "Django & DRF", 80, "Django,REST API,ORM,Admin Panel",          1),
        ("fa-solid fa-database",  "PostgreSQL",   70, "PostgreSQL,SQL,Migrations,Indexing",       2),
        ("fa-brands fa-telegram", "Telegram Bot", 75, "PyTelegramBotAPI,Webhooks,FSM,Inline KB",  3),
    ]
    for icon, name, level, tags, order in skills:
        Skill.objects.create(icon=icon, name=name, level=level, tags=tags, order=order)
    print("✅ Ko'nikmalar yaratildi")

if not Experience.objects.exists():
    Experience.objects.create(
        company="Freelance / Mustaqil",
        role="Backend Developer",
        period="2024 — hozir",
        type="Full-time",
        desc="Python va Django asosida veb-ilovalar, REST API'lar va Telegram botlar ishlab chiqish. PostgreSQL bilan ishlash va loyihalarni deploy qilish.",
        tags="Python,Django,PostgreSQL,PyTelegramBotAPI",
        order=0,
    )
    print("✅ Tajriba yaratildi")

if not Education.objects.exists():
    Education.objects.create(
        school="Najot Ta'lim",
        field="Backend Python Django (Standard)",
        period="2023 — 2024",
        icon="fa-graduation-cap",
        desc="Python, Django, PostgreSQL va backend dasturlash asoslari bo'yicha intensiv kurs. Real loyihalar ustida amaliy mashqlar.",
        order=0,
    )
    print("✅ Ta'lim yaratildi")

if not Project.objects.exists():
    projects = [
        ("01", "Veb-ilova",    "Tez Yetkazish",
         "Django asosida qurilgan yetkazib berish xizmati backend tizimi. Buyurtmalarni boshqarish, autentifikatsiya va admin panel.",
         "Django,PostgreSQL,DRF,JWT", "", "Tugallangan", "green", 0),
        ("02", "Telegram Bot", "Info Bot",
         "Foydalanuvchilarga ma'lumot beruvchi va savollar qabul qiluvchi Telegram bot. Django backend bilan to'liq integratsiya.",
         "Python,PyTelegramBotAPI,Django,PostgreSQL", "", "Tugallangan", "green", 1),
        ("03", "Tez kunda",    "Yangi loyiha...",
         "Keyingi loyiha ustida ishlayapman. Admin panelda yangi loyiha qo'shishingiz mumkin.",
         "", "", "Jarayonda", "orange", 2),
    ]
    for num, cat, name, desc, stack, github, badge, badge_color, order in projects:
        Project.objects.create(
            num=num, category=cat, name=name, desc=desc,
            stack=stack, github=github, badge=badge,
            badge_color=badge_color, order=order,
        )
    print("✅ Loyihalar yaratildi")

print()
print("🚀 Tayyor! Serverni ishga tushiring:")
print("   python manage.py runserver")
print()
print("🔑 Admin panel: http://127.0.0.1:8000/admin/")
print("   Login: admin")
print("   Parol: admin123")
print()
print("⚠️  Parolni o'zgartiring: python manage.py changepassword admin")
