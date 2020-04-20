from django.db import models
from django.contrib.auth.models import User, Group 
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.


class Table(models.Model):
    name = models.TextField(_("Table"))
    capacity = models.IntegerField(_("Capacity"))    
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("Table")
        verbose_name_plural = _("Tables")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class MenuDetail(models.Model):
    type_name = models.TextField(_("Menu Type"))
    category = models.TextField(_("Category"))
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("MenuType")
        verbose_name_plural = _("MenuTypes")

    def __str__(self):
        return self.type_name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class Menu (models.Model):
    name = models.TextField(_("Menu name"))
    type =  models.ForeignKey(MenuDetail, verbose_name=_("Type"), on_delete=models.CASCADE)
    quantity = models.TextField(_("Quanitity"))
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2) 
    description = models.TextField(_("Description"))
    taste = models.TextField(_("Taste"))
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)
    is_new = models.NullBooleanField(_("Newly Added"))

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menu")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class OrderedMenu (models.Model):
    menu = models.ForeignKey(Menu, verbose_name=_("Menu"), on_delete=models.CASCADE)
    quantity = models.IntegerField(_("quantity"))
    taste = models.TextField(_("taste"), default="Regular")
    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("OrderedMenu")
        verbose_name_plural = _("OrderedMenues")

    def __str__(self):
        return self.menu.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Order(models.Model):
    name = models.TextField(_("Order"))
    menu = models.ManyToManyField(OrderedMenu, verbose_name=_("Ordered Menu"))
    table = models.ForeignKey(Table, verbose_name=_("Table"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("Orders")
        verbose_name_plural = _("Orders")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

class Billing(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), on_delete=models.CASCADE)    
    final_total = models.DecimalField(_("Total"), max_digits=7, decimal_places=2)
    paid = models.BooleanField(_("Paid"))
    discount = models.DecimalField(_("discount"), max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = _("Billing")
        verbose_name_plural = _("Billings")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
