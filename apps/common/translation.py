from modeltranslation.translator import TranslationOptions, register

from .models import *


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(ProductSize)
class ProductSizeTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', )