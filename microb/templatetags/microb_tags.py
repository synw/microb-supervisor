# -*- coding: utf-8 -*-
import json
from django import template
from django.utils.html import mark_safe
from instant.init import get_role_channels, clean_chanpath

register = template.Library()


@register.simple_tag
def convert_instances(instances):
    jsi = {}
    for instance in instances:
        jsi[instance.slug] = {
            "domain": instance.domain,
            "ip": instance.ip,
            "port": instance.port,
            "url": instance.url,
            "status": "unknown",
        }

    return mark_safe(json.dumps(jsi))


"""
@register.assignment_tag
def _get_ping_channels(path):
    chans = get_role_channels(path, "superuser")
    res = []
    for chan in chans:
        if chan.endswith("_in") and chan.startswith("cmd:"):
            res.append(clean_chanpath(chan))
    return res
"""


@register.assignment_tag
def get_ping_channels(path):
    chans = get_role_channels(path, "superuser")
    res = []
    for chan in chans:
        if chan.endswith("_in") and chan.startswith("cmd:"):
            res.append(clean_chanpath(chan))
    return res
