from uuid import uuid4, UUID

import attr


@attr.s(auto_attribs=True)
class Entity(object):
    """ Int ID Entity """
    id: int = None


@attr.s(auto_attribs=True)
class UuidEntity(object):
    """ UUID Entity """
    id: UUID = uuid4()


@attr.s(auto_attribs=True)
class ValueObject(object):
    """ Value Object """
