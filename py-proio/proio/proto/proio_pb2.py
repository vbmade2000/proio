# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proio/proto/proio.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proio/proto/proio.proto',
  package='proio.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x17proio/proto/proio.proto\x12\x0bproio.proto\"\"\n\x04Meta\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xaf\x02\n\x0c\x42ucketHeader\x12\x0f\n\x07nEvents\x18\x01 \x01(\x04\x12\x12\n\nbucketSize\x18\x02 \x01(\x04\x12\x37\n\x0b\x63ompression\x18\x03 \x01(\x0e\x32\".proio.proto.BucketHeader.CompType\x12\x33\n\x04type\x18\x04 \x01(\x0e\x32%.proio.proto.BucketHeader.PayloadType\x12\x17\n\x0f\x66ileDescriptors\x18\x05 \x03(\x0c\x12#\n\x08metaData\x18\x06 \x03(\x0b\x32\x11.proio.proto.Meta\"\'\n\x08\x43ompType\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04GZIP\x10\x01\x12\x07\n\x03LZ4\x10\x02\"%\n\x0bPayloadType\x12\n\n\x06\x45VENTS\x10\x00\x12\n\n\x06\x46OOTER\x10\x01\"\x16\n\x03Tag\x12\x0f\n\x07\x65ntries\x18\x01 \x03(\x04\"&\n\x05\x45ntry\x12\x0c\n\x04type\x18\x01 \x01(\x04\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"\xf9\x02\n\x05\x45vent\x12*\n\x04tags\x18\x01 \x03(\x0b\x32\x1c.proio.proto.Event.TagsEntry\x12\x10\n\x08nEntries\x18\x02 \x01(\x04\x12\x30\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x1f.proio.proto.Event.EntriesEntry\x12\x0e\n\x06nTypes\x18\x04 \x01(\x04\x12,\n\x05types\x18\x05 \x03(\x0b\x32\x1d.proio.proto.Event.TypesEntry\x12\x11\n\ttimestamp\x18\x06 \x01(\x04\x1a=\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.proio.proto.Tag:\x02\x38\x01\x1a\x42\n\x0c\x45ntriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.proio.proto.Entry:\x02\x38\x01\x1a,\n\nTypesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42=\n\x05proioB\x05ProtoZ-github.com/decibelcooper/proio/go-proio/protob\x06proto3')
)



_BUCKETHEADER_COMPTYPE = _descriptor.EnumDescriptor(
  name='CompType',
  full_name='proio.proto.BucketHeader.CompType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GZIP', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LZ4', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=302,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_BUCKETHEADER_COMPTYPE)

_BUCKETHEADER_PAYLOADTYPE = _descriptor.EnumDescriptor(
  name='PayloadType',
  full_name='proio.proto.BucketHeader.PayloadType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EVENTS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOOTER', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=343,
  serialized_end=380,
)
_sym_db.RegisterEnumDescriptor(_BUCKETHEADER_PAYLOADTYPE)


_META = _descriptor.Descriptor(
  name='Meta',
  full_name='proio.proto.Meta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='proio.proto.Meta.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='proio.proto.Meta.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=74,
)


_BUCKETHEADER = _descriptor.Descriptor(
  name='BucketHeader',
  full_name='proio.proto.BucketHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nEvents', full_name='proio.proto.BucketHeader.nEvents', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bucketSize', full_name='proio.proto.BucketHeader.bucketSize', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compression', full_name='proio.proto.BucketHeader.compression', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='proio.proto.BucketHeader.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fileDescriptors', full_name='proio.proto.BucketHeader.fileDescriptors', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metaData', full_name='proio.proto.BucketHeader.metaData', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BUCKETHEADER_COMPTYPE,
    _BUCKETHEADER_PAYLOADTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=380,
)


_TAG = _descriptor.Descriptor(
  name='Tag',
  full_name='proio.proto.Tag',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entries', full_name='proio.proto.Tag.entries', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=404,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='proio.proto.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='proio.proto.Entry.type', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='proio.proto.Entry.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=406,
  serialized_end=444,
)


_EVENT_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='proio.proto.Event.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proio.proto.Event.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proio.proto.Event.TagsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=649,
  serialized_end=710,
)

_EVENT_ENTRIESENTRY = _descriptor.Descriptor(
  name='EntriesEntry',
  full_name='proio.proto.Event.EntriesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proio.proto.Event.EntriesEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proio.proto.Event.EntriesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=712,
  serialized_end=778,
)

_EVENT_TYPESENTRY = _descriptor.Descriptor(
  name='TypesEntry',
  full_name='proio.proto.Event.TypesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='proio.proto.Event.TypesEntry.key', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='proio.proto.Event.TypesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=824,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='proio.proto.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tags', full_name='proio.proto.Event.tags', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nEntries', full_name='proio.proto.Event.nEntries', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='proio.proto.Event.entries', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nTypes', full_name='proio.proto.Event.nTypes', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='types', full_name='proio.proto.Event.types', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='proio.proto.Event.timestamp', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_TAGSENTRY, _EVENT_ENTRIESENTRY, _EVENT_TYPESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=447,
  serialized_end=824,
)

_BUCKETHEADER.fields_by_name['compression'].enum_type = _BUCKETHEADER_COMPTYPE
_BUCKETHEADER.fields_by_name['type'].enum_type = _BUCKETHEADER_PAYLOADTYPE
_BUCKETHEADER.fields_by_name['metaData'].message_type = _META
_BUCKETHEADER_COMPTYPE.containing_type = _BUCKETHEADER
_BUCKETHEADER_PAYLOADTYPE.containing_type = _BUCKETHEADER
_EVENT_TAGSENTRY.fields_by_name['value'].message_type = _TAG
_EVENT_TAGSENTRY.containing_type = _EVENT
_EVENT_ENTRIESENTRY.fields_by_name['value'].message_type = _ENTRY
_EVENT_ENTRIESENTRY.containing_type = _EVENT
_EVENT_TYPESENTRY.containing_type = _EVENT
_EVENT.fields_by_name['tags'].message_type = _EVENT_TAGSENTRY
_EVENT.fields_by_name['entries'].message_type = _EVENT_ENTRIESENTRY
_EVENT.fields_by_name['types'].message_type = _EVENT_TYPESENTRY
DESCRIPTOR.message_types_by_name['Meta'] = _META
DESCRIPTOR.message_types_by_name['BucketHeader'] = _BUCKETHEADER
DESCRIPTOR.message_types_by_name['Tag'] = _TAG
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Meta = _reflection.GeneratedProtocolMessageType('Meta', (_message.Message,), dict(
  DESCRIPTOR = _META,
  __module__ = 'proio.proto.proio_pb2'
  # @@protoc_insertion_point(class_scope:proio.proto.Meta)
  ))
_sym_db.RegisterMessage(Meta)

BucketHeader = _reflection.GeneratedProtocolMessageType('BucketHeader', (_message.Message,), dict(
  DESCRIPTOR = _BUCKETHEADER,
  __module__ = 'proio.proto.proio_pb2'
  # @@protoc_insertion_point(class_scope:proio.proto.BucketHeader)
  ))
_sym_db.RegisterMessage(BucketHeader)

Tag = _reflection.GeneratedProtocolMessageType('Tag', (_message.Message,), dict(
  DESCRIPTOR = _TAG,
  __module__ = 'proio.proto.proio_pb2'
  # @@protoc_insertion_point(class_scope:proio.proto.Tag)
  ))
_sym_db.RegisterMessage(Tag)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
  DESCRIPTOR = _ENTRY,
  __module__ = 'proio.proto.proio_pb2'
  # @@protoc_insertion_point(class_scope:proio.proto.Entry)
  ))
_sym_db.RegisterMessage(Entry)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _EVENT_TAGSENTRY,
    __module__ = 'proio.proto.proio_pb2'
    # @@protoc_insertion_point(class_scope:proio.proto.Event.TagsEntry)
    ))
  ,

  EntriesEntry = _reflection.GeneratedProtocolMessageType('EntriesEntry', (_message.Message,), dict(
    DESCRIPTOR = _EVENT_ENTRIESENTRY,
    __module__ = 'proio.proto.proio_pb2'
    # @@protoc_insertion_point(class_scope:proio.proto.Event.EntriesEntry)
    ))
  ,

  TypesEntry = _reflection.GeneratedProtocolMessageType('TypesEntry', (_message.Message,), dict(
    DESCRIPTOR = _EVENT_TYPESENTRY,
    __module__ = 'proio.proto.proio_pb2'
    # @@protoc_insertion_point(class_scope:proio.proto.Event.TypesEntry)
    ))
  ,
  DESCRIPTOR = _EVENT,
  __module__ = 'proio.proto.proio_pb2'
  # @@protoc_insertion_point(class_scope:proio.proto.Event)
  ))
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.TagsEntry)
_sym_db.RegisterMessage(Event.EntriesEntry)
_sym_db.RegisterMessage(Event.TypesEntry)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\005proioB\005ProtoZ-github.com/decibelcooper/proio/go-proio/proto'))
_EVENT_TAGSENTRY.has_options = True
_EVENT_TAGSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_EVENT_ENTRIESENTRY.has_options = True
_EVENT_ENTRIESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_EVENT_TYPESENTRY.has_options = True
_EVENT_TYPESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)