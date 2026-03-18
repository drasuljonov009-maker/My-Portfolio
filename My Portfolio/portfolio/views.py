from django.shortcuts import render
from .models import Profile, Stat, Skill, Experience, Education, Project

NAV_ITEMS = [
    {"href": "#about",      "label": "Haqimda"},
    {"href": "#skills",     "label": "Ko'nikmalar"},
    {"href": "#experience", "label": "Tajriba"},
    {"href": "#education",  "label": "Ta'lim"},
    {"href": "#projects",   "label": "Loyihalar"},
    {"href": "#contact",    "label": "Aloqa"},
]

def index(request):
    profile     = Profile.objects.first()
    stats       = Stat.objects.all()
    skills      = Skill.objects.all()
    experiences = Experience.objects.all()
    education   = Education.objects.all()
    projects    = Project.objects.all()

    context = {
        "profile":     profile,
        "stats":       stats,
        "skills":      skills,
        "experiences": experiences,
        "education":   education,
        "projects":    projects,
        "nav_items":   NAV_ITEMS,
    }
    return render(request, 'portfolio/index.html', context)
