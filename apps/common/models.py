from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False, verbose_name=_("Model id"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    class Meta:
        abstract = True


class VersionHistory(BaseModel):
    version = models.CharField(_("Version"), max_length=64)
    required = models.BooleanField(_("Required"), default=True)

    class Meta:
        verbose_name = _("Version history")
        verbose_name_plural = _("Version histories")

    def __str__(self):
        return self.version
    
class Category(BaseModel):
    class CategoryTypeChoices(models.TextChoices):
        FOOD = ('food', _('Food'))
        FAST_FOOD = ('fast_food', _('Fast food'))

    name = models.CharField(max_length=128, verbose_name=_('Name'))
    category_type = models.CharField(max_length=28, choices=CategoryTypeChoices.choices, verbose_name=_('Category type'))

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Product(BaseModel):
    name = models.CharField(max_length=128, verbose_name=_('Product name'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='product_image', verbose_name=_('Image'))
    category = models.ForeignKey(Category, models.PROTECT, related_name='products', verbose_name=_('Category'), null=True, blank=True)
    rating = models.FloatField(default=0.0)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-rating', '-created_at']
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    

class ProductSize(BaseModel):
    class ProductSizeChoices(models.TextChoices):
        LITRE = 'l', 'Liter'
        CUBIC_METER = 'mcub', 'Kub metr'
        SQUARE_METER  = 'mkv', 'Kvadrat metr'
        TON = 't', 'Tonna'
        CENTIMETER  = 'cm', 'Santimetr'
        GRAM = 'g', 'Gramm'
        KILOGRAM = 'kg', 'Kilogramm'
        PORTION = 'port', 'Porsiya'
        METER = 'm', 'Metr'
        PIECE = 'pcs', 'Dona'
    product = models.ForeignKey(Product, models.PROTECT, verbose_name=_('Product'), related_name='product_sizes')
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    size = models.CharField(max_length=28, choices=ProductSizeChoices.choices, verbose_name=_('Size'))
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_('Price'))
    description = models.TextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='product/', blank=True, null=True)


    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = _("Product size")
        verbose_name_plural = _("Product sizes")
    

class Cart(BaseModel):
    user = models.OneToOneField('user.User', models.CASCADE, related_name='cart', verbose_name=_('User'))

    def __str__(self) -> str:
        return self.user.phone_number
    
    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        ordering = ('-quantity', '-created_at')
        verbose_name = _("Cart item")
        verbose_name_plural = _("Cart items")



class Order(BaseModel):
    class OrderStatusChoices(models.TextChoices):
        PENDING = ('pending', _('Pending'))
        CONFIRMED = ('confirmed', _('Confirmed'))
        OUT_FOR_DELIVERY = ('out_for_delivery', _('Out for delivery'))
        COMPLETED = ('completed', _('Completed'))
        CANCELLED = ('cancelled', _('Cancelled'))

    user = models.OneToOneField('user.User', models.CASCADE, related_name='order', verbose_name=_('User'))
    status = models.CharField(max_length=64, choices=OrderStatusChoices.choices, default=OrderStatusChoices.PENDING, verbose_name=_('Status'))
    delivery_time = models.DateTimeField(default=timezone.now, verbose_name=_('Delivery time'))
    is_discount =models.BooleanField(default=False, verbose_name=_('Discount'))
    address = models.CharField(max_length=256, verbose_name=_('Address'))

    @property
    def total_price(self):
        tl_pr = sum(order_item for order_item in self.order_items.all())
        if self.is_discount:
            tl_pr -= self.user.coins
            if self.user.coins != 0:
                self.user.coins = 0
                self.user.save()
        return tl_pr


    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self) -> str:
        return self.user.phone_number    


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, models.CASCADE, related_name='order_items')
    product = models.ForeignKey(ProductSize, models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)
    
    @property
    def total_price(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = _("Order item")
        verbose_name_plural = _("Order items")


class Banner(BaseModel):
    title = models.CharField(max_length=256, verbose_name=_('Title'))
    image = models.ImageField(upload_to='banner_image/', verbose_name=_('Image'))
    phone_image = models.ImageField(upload_to='banner_image/', verbose_name=_('Image for phone'), blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name=_('Ordering'))

    class Meta:
        ordering = ('order', '-created_at')
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')
    

class Rating(BaseModel):
    product = models.ForeignKey(Product, models.CASCADE, related_name='ratings')
    user = models.ForeignKey('user.User', models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.rating)