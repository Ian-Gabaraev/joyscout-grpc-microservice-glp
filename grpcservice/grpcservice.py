# grpcservice/grpcservice.py

from concurrent import futures

import utils

import grpc


from lastpage_pb2 import (
    LastPage,
    LastPageRequest,
    LastPageResponse
)

import lastpage_pb2_grpc


class PSStoreLastPageService(

    lastpage_pb2_grpc.PS4StoreLastPageServicer

):

    def GetLastPage(self, request, context):
        last_page = utils.find_final_page()
        return LastPageResponse(last_page=last_page)


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    lastpage_pb2_grpc.add_PS4StoreLastPageServicer_to_server(

        PSStoreLastPageService(), server

    )

    server.add_insecure_port("[::]:50051")

    server.start()

    server.wait_for_termination()


if __name__ == "__main__":

    serve()
