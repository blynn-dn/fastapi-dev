from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Union, Optional

from pydantic import BaseModel, Field, RootModel


# region nautobot webhook Event model
class Manufacturer(BaseModel):
    display: str
    id: str
    url: str
    name: str
    slug: str


class DeviceType(BaseModel):
    display: str
    id: str
    url: str
    manufacturer: Manufacturer
    model: str
    slug: str


class DeviceRole(BaseModel):
    display: str
    id: str
    url: str
    name: str
    slug: str


class Site(BaseModel):
    display: str
    id: str
    url: str
    name: str
    slug: str


class Status(BaseModel):
    value: str
    label: str


class Device(BaseModel):
    id: str
    display: str
    url: str
    name: str
    device_type: DeviceType
    device_role: DeviceRole
    tenant: Any
    platform: Any
    serial: str
    asset_tag: Any
    site: Site
    location: Any
    rack: Any
    position: Any
    face: Any
    parent_device: Any
    status: Status
    primary_ip: Any
    primary_ip4: Any
    primary_ip6: Any
    secrets_group: Any
    cluster: Any
    virtual_chassis: Any
    vc_position: Any
    vc_priority: Any
    device_redundancy_group: Any
    device_redundancy_group_priority: Any
    comments: str
    local_context_schema: Any
    local_context_data: Any
    created: str
    last_updated: str
    tags: List
    notes_url: str
    custom_fields: Dict[str, Any]


class Change(BaseModel):
    id: str
    url: str
    face: Any
    name: str
    rack: Any
    site: Site
    tags: List
    serial: str
    status: Status
    tenant: Any
    cluster: Any
    created: str
    display: str
    comments: str
    location: Any
    platform: Any
    position: Any
    asset_tag: Any
    notes_url: str
    primary_ip: Any
    device_role: DeviceRole
    device_type: DeviceType
    primary_ip4: Any
    primary_ip6: Any
    vc_position: Any
    vc_priority: Any
    last_updated: str
    custom_fields: Dict[str, Any]
    parent_device: Any
    secrets_group: Any
    virtual_chassis: Any
    local_context_data: Any
    local_context_schema: Any
    device_redundancy_group: Any
    device_redundancy_group_priority: Any


class Difference(BaseModel):
    status: Status


class Differences(BaseModel):
    # note that an event of type `created` has a `removed` of None
    removed: Union[Dict[Any, Any], None]

    # note that an event of type `deleted` has a `added` of None
    added: Union[Dict[Any, Any], None]


class Snapshots(BaseModel):
    # note that an event of type `created` has a `prechange` of None
    pre_change: Union[Change, None] = Field(alias='prechange')

    # note that an event of type `deleted` has a `postchange` of None
    post_change: Union[Change, None] = Field(alias='postchange')
    differences: Differences


class EventEnum(str, Enum):
    updated = 'updated'
    created = 'created'
    deleted = 'deleted'


class ModelEnum(str, Enum):
    device = 'device'


class Event(BaseModel):
    event: EventEnum
    timestamp: str
    model: ModelEnum
    username: str
    request_id: str
    data: Device
    snapshots: Snapshots


class EventRoot(RootModel):
    root: Event

'''
class EventRootModel(BaseModel):
    __root__: Event
'''


# endregion nautobot webhook Event model
