# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import Service_pb2 as Service__pb2


class ClientServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/ClientService/ListFiles',
                request_serializer=Service__pb2.Empty.SerializeToString,
                response_deserializer=Service__pb2.FileList.FromString,
                )
        self.CreateFile = channel.unary_unary(
                '/ClientService/CreateFile',
                request_serializer=Service__pb2.FileData.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.Open = channel.unary_unary(
                '/ClientService/Open',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.Close = channel.unary_unary(
                '/ClientService/Close',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.Read = channel.unary_unary(
                '/ClientService/Read',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.FileData.FromString,
                )
        self.Write = channel.unary_unary(
                '/ClientService/Write',
                request_serializer=Service__pb2.FileData.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.FilePartition = channel.unary_unary(
                '/ClientService/FilePartition',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.PartitionedFile.FromString,
                )
        self.JoinPartitionedFiles = channel.unary_unary(
                '/ClientService/JoinPartitionedFiles',
                request_serializer=Service__pb2.PartitionedFile.SerializeToString,
                response_deserializer=Service__pb2.FileData.FromString,
                )


class ClientServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Open(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FilePartition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def JoinPartitionedFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ClientServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=Service__pb2.Empty.FromString,
                    response_serializer=Service__pb2.FileList.SerializeToString,
            ),
            'CreateFile': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFile,
                    request_deserializer=Service__pb2.FileData.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'Open': grpc.unary_unary_rpc_method_handler(
                    servicer.Open,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.FileData.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=Service__pb2.FileData.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'FilePartition': grpc.unary_unary_rpc_method_handler(
                    servicer.FilePartition,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.PartitionedFile.SerializeToString,
            ),
            'JoinPartitionedFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.JoinPartitionedFiles,
                    request_deserializer=Service__pb2.PartitionedFile.FromString,
                    response_serializer=Service__pb2.FileData.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ClientService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ClientService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/ListFiles',
            Service__pb2.Empty.SerializeToString,
            Service__pb2.FileList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/CreateFile',
            Service__pb2.FileData.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Open(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/Open',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/Close',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/Read',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.FileData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/Write',
            Service__pb2.FileData.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FilePartition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/FilePartition',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.PartitionedFile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def JoinPartitionedFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ClientService/JoinPartitionedFiles',
            Service__pb2.PartitionedFile.SerializeToString,
            Service__pb2.FileData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class NameNodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/NameNodeService/Create',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.AllocateBlocks = channel.unary_unary(
                '/NameNodeService/AllocateBlocks',
                request_serializer=Service__pb2.FileData.SerializeToString,
                response_deserializer=Service__pb2.BlockAllocation.FromString,
                )
        self.Append = channel.unary_unary(
                '/NameNodeService/Append',
                request_serializer=Service__pb2.FileData.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.GetBlockLocations = channel.unary_unary(
                '/NameNodeService/GetBlockLocations',
                request_serializer=Service__pb2.FilePath.SerializeToString,
                response_deserializer=Service__pb2.BlockLocations.FromString,
                )
        self.RegisterDataNode = channel.unary_unary(
                '/NameNodeService/RegisterDataNode',
                request_serializer=Service__pb2.DataNodeInfo.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.DataNodeHeartbeat = channel.unary_unary(
                '/NameNodeService/DataNodeHeartbeat',
                request_serializer=Service__pb2.DataNodeStatus.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.RelocateBlocks = channel.unary_unary(
                '/NameNodeService/RelocateBlocks',
                request_serializer=Service__pb2.BlockRelocation.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )


class NameNodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocateBlocks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Append(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockLocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterDataNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DataNodeHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RelocateBlocks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameNodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'AllocateBlocks': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateBlocks,
                    request_deserializer=Service__pb2.FileData.FromString,
                    response_serializer=Service__pb2.BlockAllocation.SerializeToString,
            ),
            'Append': grpc.unary_unary_rpc_method_handler(
                    servicer.Append,
                    request_deserializer=Service__pb2.FileData.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'GetBlockLocations': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockLocations,
                    request_deserializer=Service__pb2.FilePath.FromString,
                    response_serializer=Service__pb2.BlockLocations.SerializeToString,
            ),
            'RegisterDataNode': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterDataNode,
                    request_deserializer=Service__pb2.DataNodeInfo.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'DataNodeHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.DataNodeHeartbeat,
                    request_deserializer=Service__pb2.DataNodeStatus.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'RelocateBlocks': grpc.unary_unary_rpc_method_handler(
                    servicer.RelocateBlocks,
                    request_deserializer=Service__pb2.BlockRelocation.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameNodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameNodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/Create',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocateBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/AllocateBlocks',
            Service__pb2.FileData.SerializeToString,
            Service__pb2.BlockAllocation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Append(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/Append',
            Service__pb2.FileData.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockLocations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/GetBlockLocations',
            Service__pb2.FilePath.SerializeToString,
            Service__pb2.BlockLocations.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterDataNode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/RegisterDataNode',
            Service__pb2.DataNodeInfo.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DataNodeHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/DataNodeHeartbeat',
            Service__pb2.DataNodeStatus.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RelocateBlocks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNodeService/RelocateBlocks',
            Service__pb2.BlockRelocation.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class DataNodeServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendHeartbeat = channel.unary_unary(
                '/DataNodeService/SendHeartbeat',
                request_serializer=Service__pb2.Empty.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.StoreBlock = channel.unary_unary(
                '/DataNodeService/StoreBlock',
                request_serializer=Service__pb2.BlockData.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.DeleteBlock = channel.unary_unary(
                '/DataNodeService/DeleteBlock',
                request_serializer=Service__pb2.BlockId.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.SendBlock = channel.unary_unary(
                '/DataNodeService/SendBlock',
                request_serializer=Service__pb2.BlockId.SerializeToString,
                response_deserializer=Service__pb2.BlockData.FromString,
                )
        self.CleanStart = channel.unary_unary(
                '/DataNodeService/CleanStart',
                request_serializer=Service__pb2.Empty.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )
        self.ChangeOfLeader = channel.unary_unary(
                '/DataNodeService/ChangeOfLeader',
                request_serializer=Service__pb2.LeaderInfo.SerializeToString,
                response_deserializer=Service__pb2.Status.FromString,
                )


class DataNodeServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendHeartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendBlock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CleanStart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangeOfLeader(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataNodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendHeartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.SendHeartbeat,
                    request_deserializer=Service__pb2.Empty.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'StoreBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreBlock,
                    request_deserializer=Service__pb2.BlockData.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'DeleteBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteBlock,
                    request_deserializer=Service__pb2.BlockId.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'SendBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.SendBlock,
                    request_deserializer=Service__pb2.BlockId.FromString,
                    response_serializer=Service__pb2.BlockData.SerializeToString,
            ),
            'CleanStart': grpc.unary_unary_rpc_method_handler(
                    servicer.CleanStart,
                    request_deserializer=Service__pb2.Empty.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
            'ChangeOfLeader': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangeOfLeader,
                    request_deserializer=Service__pb2.LeaderInfo.FromString,
                    response_serializer=Service__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataNodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataNodeService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendHeartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/SendHeartbeat',
            Service__pb2.Empty.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StoreBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/StoreBlock',
            Service__pb2.BlockData.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/DeleteBlock',
            Service__pb2.BlockId.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/SendBlock',
            Service__pb2.BlockId.SerializeToString,
            Service__pb2.BlockData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CleanStart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/CleanStart',
            Service__pb2.Empty.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChangeOfLeader(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNodeService/ChangeOfLeader',
            Service__pb2.LeaderInfo.SerializeToString,
            Service__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
