from keystoneclient.v2_0 import client as keystone_client
from novaclient.v1_1 import client as nova_client

from openstack_aps_endpoint.settings import ADMIN_KEYSTONE_URL, KEYSTONE_URL, KEYSTONE_LOGIN, KEYSTONE_PASSWORD, \
    DEFAULT_TENANT, DEFAULT_IMAGE
from openstack_aps_app.common.utils import data_utils


nova_client = nova_client.Client(KEYSTONE_LOGIN, KEYSTONE_PASSWORD, DEFAULT_TENANT, KEYSTONE_URL)

keystone_client = keystone_client.Client(username=KEYSTONE_LOGIN, password=KEYSTONE_PASSWORD,
                                         tenant_name=DEFAULT_TENANT,
                                         auth_url=ADMIN_KEYSTONE_URL)


def get_image_by_name(name):
    return nova_client.images.find(name=name)


def instance_create():
    return nova_client.servers.create(name=data_utils.rand_name('temporary-instance'),
                                      image=get_image_by_name(DEFAULT_IMAGE).id, flavor=1)


def instance_list():
    return nova_client.servers.list()


def tenant_create():
    return keystone_client.tenants.create(tenant_name=data_utils.rand_name('temporary-tenant'),
                                          description=data_utils.rand_name('temporary-description'))


def tenant_list():
    return keystone_client.tenants.list()


def quota_list(tenant_id):
    return nova_client.quotas.get(tenant_id)
