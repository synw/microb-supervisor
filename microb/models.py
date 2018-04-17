# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from instant.models import Channel


class Instance(models.Model):
    domain = models.CharField(
        max_length=120,
        verbose_name=_(u'Domain'),
        unique=True,)
    #slug = models.SlugField(max_length=25, unique=True)
    ip = models.GenericIPAddressField(
        verbose_name=_(u'Ip adress'),
        unique=True,
        blank=True,
        null=True)
    port = models.PositiveIntegerField(
        verbose_name=_(u'Port'), blank=True, null=True)
    url = models.URLField(blank=True)
    channel_in = models.CharField(max_length=120, blank=True)
    channel_out = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = _(u'Instance')
        verbose_name_plural = _(u'Instances')
        ordering = ('domain', 'ip')
        unique_together = ('domain', 'ip')

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
        """
        Build the server adress and command channels before saving
        """
        # get url and channels
        self.url = self.get_url()
        self.channel_in = "cmd:$" + self.domain + "_in"
        self.channel_out = "cmd:$" + self.domain + "_out"
        # ensure that the command channels exist in the database
        Channel.objects.get_or_create(
            slug=self.channel_in,
            role="superuser",
            paths="/microb")
        Channel.objects.get_or_create(
            slug=self.channel_out,
            role="superuser",
            paths="/microb")
        super(Instance, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Remove the database channels
        """
        try:
            chans = [self.channel_in, self.channel_out]
            Channel.objects.filter(slug__in=chans).delete()
        except Channel.DoesNotExist:
            pass
        super(Instance, self).delete(*args, **kwargs)

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
