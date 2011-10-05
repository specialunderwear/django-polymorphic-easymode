from django.db import models
from polymorphic import PolymorphicModel
from easymode.i18n.decorators import I18n
# Create your models here.

class Owner(models.Model):
    title = models.CharField(max_length=255)

class RealPageBase(models.Model):
    title = models.CharField(max_length=255)
    meta_description = models.TextField()
    
    class Meta:
        abstract = True

class PageBase(PolymorphicModel):
    """The baseclass for all pages"""
    owner = models.ForeignKey(Owner, related_name='pages')
    
    order = models.PositiveIntegerField('Order', default=99999999)
    
    slug = models.SlugField()
    
    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return "%s - %s" % (self.__class__.__doc__, self.slug)

@I18n('body', 'title')
class PageWithBodyText(PageBase, RealPageBase):
    "A page with an extra text"
    body = models.TextField()

@I18n('image')
class PageWithLink(PageBase, RealPageBase):
    "A page with an extra link"
    link = models.URLField()
    image = models.ImageField(upload_to='images')

