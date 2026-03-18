from django.contrib import admin
from django.utils.html import format_html
from .models import Profile, Stat, Skill, Experience, Education, Project

admin.site.site_header  = "Dostonbek Portfolio — Admin"
admin.site.site_title   = "Portfolio Admin"
admin.site.index_title  = "Boshqaruv paneli"


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Shaxsiy ma'lumotlar", {
            'fields': ('name', 'role', 'location', 'experience')
        }),
        ("Bio", {
            'fields': ('bio',)
        }),
        ("Aloqa va ijtimoiy tarmoqlar", {
            'fields': ('email', 'github', 'telegram', 'linkedin')
        }),
    )

    def has_add_permission(self, request):
        return not Profile.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display  = ('num', 'label', 'order')
    list_editable = ('order',)
    ordering      = ('order',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('name', 'level_bar', 'order')
    list_editable = ('order',)
    ordering      = ('order',)

    def level_bar(self, obj):
        color = '#f97316' if obj.level >= 70 else '#60a5fa'
        return format_html(
            '<div style="background:#1e293b;border-radius:4px;width:120px;height:10px;display:inline-block;vertical-align:middle;">'
            '<div style="background:{};width:{}%;height:100%;border-radius:4px;"></div>'
            '</div> <small style="margin-left:6px;">{}%</small>',
            color, obj.level, obj.level
        )
    level_bar.short_description = "Daraja"


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ('company', 'role', 'order')
    list_editable = ('order',)
    ordering      = ('order',)
    fields        = ('company', 'role', 'period', 'type', 'desc', 'tags', 'order')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ('school', 'field', 'order')
    list_editable = ('order',)
    ordering      = ('order',)
    fields        = ('school', 'field', 'period', 'icon', 'desc', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display  = ('num', 'name', 'category', 'badge_colored', 'order')
    list_editable = ('order',)
    ordering      = ('order',)
    fields        = ('num', 'category', 'name', 'desc', 'stack', 'github', 'badge', 'badge_color', 'order')

    def badge_colored(self, obj):
        colors = {'green': '#22c55e', 'orange': '#f97316', 'blue': '#60a5fa'}
        c = colors.get(obj.badge_color, '#888')
        return format_html(
            '<span style="background:{}22;color:{};border:1px solid {}55;'
            'padding:2px 10px;border-radius:20px;font-size:11px;">{}</span>',
            c, c, c, obj.badge
        )
    badge_colored.short_description = "Holat"
