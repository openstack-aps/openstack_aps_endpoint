from rest_framework.renderers import JSONRenderer

from openstack_aps_app import encoders


class JSONRenderer(JSONRenderer):
    encoder_class = encoders.JSONEncoder