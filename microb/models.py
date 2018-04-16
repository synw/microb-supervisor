# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from instant.init import get_role_channels, clean_chanpath


class Instance(models.Model):
    domain = models.CharField(
        max_length=120,
        verbose_name=_(u'Domain'),
        unique=True,)
    slug = models.SlugField(max_length=25, unique=True)
    ip = models.GenericIPAddressField(
        verbose_name=_(u'Ip adress'),
        unique=True,
        blank=True,
        null=True)
    port = models.PositiveIntegerField(
        verbose_name=_(u'Port'), blank=True, null=True)
    url = models.URLField(blank=True)
    ping_channel = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = _(u'Instance')
        verbose_name_plural = _(u'Instances')
        ordering = ('domain', 'ip')
        unique_together = ('domain', 'ip', 'slug')

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
        """
        Build the server adress before saving
        """
        self.url = self.get_url()
        self.ping_channel = "cmd:$" + self.domain + "_in"
        super(Instance, self).save(*args, **kwargs)

    def get_url(self):
        """
        Get the adress of the server from
        either ip or domain
        """
        if self.ip:
            addr = str(self.ip)
            if self.port is not None:
                addr += ":" + str(self.port)
        else:
            addr = self.domain
        return addr
