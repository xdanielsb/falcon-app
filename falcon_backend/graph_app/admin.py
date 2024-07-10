# Register your models here.
from django.contrib import admin

from graph_app.models import Node, Edge, GraphMetadata, Empire, BountyHunter

admin.site.site_title = 'Milleniun Falcon'
admin.site.site_header = 'Milleniun falcon'
admin.site.index_title = 'Milleniun control'

admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(Empire)
