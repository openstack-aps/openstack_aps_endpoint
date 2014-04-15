from rest_framework.decorators import api_view
from rest_framework.response import Response

from openstack_aps_app.rest import openstack_aps_client


@api_view(['GET'])
def index(request):
    return Response({'status': 'ok'})


@api_view(['GET'])
def instance_create(request):
    return Response(openstack_aps_client.instance_create())


@api_view(['GET'])
def instance_list(request):
    return Response(openstack_aps_client.instance_list())


@api_view(['GET'])
def tenant_create(request):
    return Response(openstack_aps_client.tenant_create())


@api_view(['GET'])
def tenant_list(request):
    return Response(openstack_aps_client.tenant_list())


@api_view(['GET'])
def quota_list(request, tenant_id):
    return Response(openstack_aps_client.quota_list(tenant_id))
