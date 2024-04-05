# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rService.proto\"\x07\n\x05\x45mpty\"\x19\n\x08\x46ileList\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"\x18\n\x08\x46ileName\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x08\x46ileData\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\",\n\x08\x46ileInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nnum_blocks\x18\x02 \x01(\x05\"3\n\x0fPartitionedFile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\npartitions\x18\x02 \x03(\x0c\"*\n\x06Status\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"1\n\x0f\x42lockAllocation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x62lockIds\x18\x02 \x03(\t\"6\n\rBlockLocation\x12\x10\n\x08\x62lock_id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61taNode_id\x18\x02 \x01(\t\"\x83\x01\n\x0e\x42lockLocations\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x31\n\tlocations\x18\x02 \x03(\x0b\x32\x1e.BlockLocations.LocationsEntry\x1a\x30\n\x0eLocationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"+\n\x0c\x44\x61taNodeInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"-\n\x0e\x44\x61taNodeStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07isAlive\x18\x02 \x01(\x08\"V\n\x0f\x42lockRelocation\x12\x0f\n\x07\x62lockId\x18\x01 \x01(\t\x12\x18\n\x10sourceDataNodeId\x18\x02 \x01(\t\x12\x18\n\x10targetDataNodeId\x18\x03 \x01(\t\"\x15\n\x07\x42lockId\x12\n\n\x02id\x18\x01 \x01(\t\"\x18\n\nDataNodeID\x12\n\n\x02id\x18\x01 \x01(\t\"%\n\tBlockData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\")\n\nLeaderInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t2\xef\x02\n\rClientService\x12 \n\tListFiles\x12\x06.Empty\x1a\t.FileList\"\x00\x12&\n\nCreateFile\x12\t.FileInfo\x1a\x0b.DataNodeID\"\x00\x12\x31\n\x11GetBlockLocations\x12\t.FileName\x1a\x0f.BlockLocations\"\x00\x12\x1c\n\x04Open\x12\t.FileName\x1a\x07.Status\"\x00\x12\x1d\n\x05\x43lose\x12\t.FileName\x1a\x07.Status\"\x00\x12\x1e\n\x04Read\x12\t.FileName\x1a\t.FileData\"\x00\x12\x1d\n\x05Write\x12\t.FileData\x1a\x07.Status\"\x00\x12.\n\rFilePartition\x12\t.FileName\x1a\x10.PartitionedFile\"\x00\x12\x35\n\x14JoinPartitionedFiles\x12\x10.PartitionedFile\x1a\t.FileData\"\x00\x32\xf0\x01\n\x0fNameNodeService\x12/\n\x0e\x41llocateBlocks\x12\t.FileData\x1a\x10.BlockAllocation\"\x00\x12\x1e\n\x06\x41ppend\x12\t.FileData\x1a\x07.Status\"\x00\x12,\n\x10RegisterDataNode\x12\r.DataNodeInfo\x1a\x07.Status\"\x00\x12/\n\x11\x44\x61taNodeHeartbeat\x12\x0f.DataNodeStatus\x1a\x07.Status\"\x00\x12-\n\x0eRelocateBlocks\x12\x10.BlockRelocation\x1a\x07.Status\"\x00\x32\xf3\x01\n\x0f\x44\x61taNodeService\x12\'\n\rSendHeartbeat\x12\x0b.DataNodeID\x1a\x07.Status\"\x00\x12#\n\nStoreBlock\x12\n.BlockData\x1a\x07.Status\"\x00\x12\"\n\x0b\x44\x65leteBlock\x12\x08.BlockId\x1a\x07.Status\"\x00\x12#\n\tSendBlock\x12\x08.BlockId\x1a\n.BlockData\"\x00\x12\x1f\n\nCleanStart\x12\x06.Empty\x1a\x07.Status\"\x00\x12(\n\x0e\x43hangeOfLeader\x12\x0b.LeaderInfo\x1a\x07.Status\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BLOCKLOCATIONS_LOCATIONSENTRY']._options = None
  _globals['_BLOCKLOCATIONS_LOCATIONSENTRY']._serialized_options = b'8\001'
  _globals['_EMPTY']._serialized_start=17
  _globals['_EMPTY']._serialized_end=24
  _globals['_FILELIST']._serialized_start=26
  _globals['_FILELIST']._serialized_end=51
  _globals['_FILENAME']._serialized_start=53
  _globals['_FILENAME']._serialized_end=77
  _globals['_FILEDATA']._serialized_start=79
  _globals['_FILEDATA']._serialized_end=117
  _globals['_FILEINFO']._serialized_start=119
  _globals['_FILEINFO']._serialized_end=163
  _globals['_PARTITIONEDFILE']._serialized_start=165
  _globals['_PARTITIONEDFILE']._serialized_end=216
  _globals['_STATUS']._serialized_start=218
  _globals['_STATUS']._serialized_end=260
  _globals['_BLOCKALLOCATION']._serialized_start=262
  _globals['_BLOCKALLOCATION']._serialized_end=311
  _globals['_BLOCKLOCATION']._serialized_start=313
  _globals['_BLOCKLOCATION']._serialized_end=367
  _globals['_BLOCKLOCATIONS']._serialized_start=370
  _globals['_BLOCKLOCATIONS']._serialized_end=501
  _globals['_BLOCKLOCATIONS_LOCATIONSENTRY']._serialized_start=453
  _globals['_BLOCKLOCATIONS_LOCATIONSENTRY']._serialized_end=501
  _globals['_DATANODEINFO']._serialized_start=503
  _globals['_DATANODEINFO']._serialized_end=546
  _globals['_DATANODESTATUS']._serialized_start=548
  _globals['_DATANODESTATUS']._serialized_end=593
  _globals['_BLOCKRELOCATION']._serialized_start=595
  _globals['_BLOCKRELOCATION']._serialized_end=681
  _globals['_BLOCKID']._serialized_start=683
  _globals['_BLOCKID']._serialized_end=704
  _globals['_DATANODEID']._serialized_start=706
  _globals['_DATANODEID']._serialized_end=730
  _globals['_BLOCKDATA']._serialized_start=732
  _globals['_BLOCKDATA']._serialized_end=769
  _globals['_LEADERINFO']._serialized_start=771
  _globals['_LEADERINFO']._serialized_end=812
  _globals['_CLIENTSERVICE']._serialized_start=815
  _globals['_CLIENTSERVICE']._serialized_end=1182
  _globals['_NAMENODESERVICE']._serialized_start=1185
  _globals['_NAMENODESERVICE']._serialized_end=1425
  _globals['_DATANODESERVICE']._serialized_start=1428
  _globals['_DATANODESERVICE']._serialized_end=1671
# @@protoc_insertion_point(module_scope)
