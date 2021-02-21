import grpc
from lastpage_pb2_grpc import PS4StoreLastPageStub
from lastpage_pb2 import LastPageRequest

channel = grpc.insecure_channel("localhost:50051")
client = PS4StoreLastPageStub(channel)
request = LastPageRequest()

print(client.GetLastPage(request))
