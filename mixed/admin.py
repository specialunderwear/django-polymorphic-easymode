from django.contrib import admin
from mixed.models import PageWithBodyText, PageWithLink,PageBase, Owner
from easymode.i18n.admin.decorators import L10n
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe

class PageInline(admin.StackedInline):
    model = PageBase
    exclude = ('order',)
    readonly_fields = ('real_link',)

    def real_link(self, model):
        """
        Render a link to the real model.
        """
        options = model._meta
        url = reverse('admin:%s_%s_change' % (options.app_label, options.object_name.lower()), args=[model.pk])
        return mark_safe('<a href="%s">Edit all fields</a>' % url)


class OwnerAdmin(admin.ModelAdmin):
    inlines  = [PageInline]

class OrderAdmin(admin.ModelAdmin):
    ordering = ('order',)
    list_display = ('__unicode__', 'id', 'order')
    
    list_editable = ('order',)
    
    class Media:
        js = (
            'jquery-1.4.2.min.js',
            'jquery-ui-1.8.16.custom.min.js',
            'menu-sort.js',            
        )
    
    def real_link(self, model):
        """
        Render a link to the real model.
        """
        options = model._meta
        url = reverse('admin:%s_%s_change' % (options.app_label, options.object_name.lower()), args=[model.pk])
        return mark_safe('<a href="%s">Edit all fields</a>' % url)
    
admin.site.register(PageBase, OrderAdmin)
admin.site.register(PageWithBodyText, L10n(PageWithBodyText, admin.ModelAdmin))
admin.site.register(PageWithLink)
admin.site.register(Owner, OwnerAdmin)
