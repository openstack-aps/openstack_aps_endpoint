from rest_framework.utils.encoders import JSONEncoder
from novaclient.v1_1.servers import Server
from novaclient.v1_1.quotas import QuotaSet
from keystoneclient.v2_0.tenants import Tenant


class JSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (Server, Tenant, QuotaSet)):
            return obj.to_dict()
        return JSONEncoder.default(self, obj)