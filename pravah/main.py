import os
import importlib
import grpc
from google.protobuf.json_format import ParseDict
from mesh_rpc.mesh import MeshRPC
from mesh_rpc.exp import MeshRPCException
from dlake import Datalake

parent_module = 'pravah_protocols'
feed_message_string = 'FeedMessage'


class Pravah(MeshRPC):
    def __init__(self, channel, endpoint='127.0.0.1:5555'):
        super().__init__(endpoint)

        self.channel = channel

        if channel[0] != '/':
            raise Exception('Not a valid channel name. Channel name starts with a \'/\'')
        
        self.proto_module = importlib.import_module(parent_module + '.' + self.get_module_name(channel))
        self.parent_module = importlib.import_module(parent_module)
        self.FeedMessage = getattr(self.proto_module, feed_message_string)

        self.datalake = Datalake(os.getenv('PRAVAH_DB_USERNAME'), os.getenv('PRAVAH_DB_PASSWORD'), channel)

    def subscribe(self, geospace):
        s = super().subscribe(self.channel, geospace)

        feed = self.FeedMessage()

        channelLen = len(self.channel)

        try:
            for msg in s:
                feed.ParseFromString(msg.raw)
                yield feed, msg.topic.pop()[channelLen:]
        except grpc.RpcError as e:
            raise MeshRPCException(e.details())
    
    def unsubscribe(self, geospaces):
        return super().unsubscribe(self.channel, geospaces)
    
    def registerToPublish(self, geospace):
        try:
            super().registerToPublish(self.channel, geospace)
        except MeshRPCException as e:
            raise 

    def publish(self, geospace, d):
        d['header']['version'] = self.parent_module.pravah_protocol_version.get(self.channel, "0.0.1")
        
        feed = self.FeedMessage()
        ParseDict(d, feed, True)
        raw = feed.SerializeToString()

        try:
            res = super().publish(self.channel, geospace, raw)
        except MeshRPCException as e:
            raise 
    
    def get_channel(self):
        return self.channel
    
    def get_module_name(self, module):
        return module[1:] + '_pb2'
    
    def get_historical_data(self, query={}, **kwargs):
        return self.datalake.get(query, **kwargs)

    def get_static_data(self):
        pass
    
