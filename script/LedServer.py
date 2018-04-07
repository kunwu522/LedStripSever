from socketserver import BaseRequestHandler, TCPServer
from LedController import LedController


class LedRequestHandler(BaseRequestHandler):
    controller = LedController()

    def __init__(self, request, client_address, server):
        BaseRequestHandler.__init__(self, request, client_address, server)
        self.controller.begin()

    def handle(self):
        print('Got connection from ', self.client_address)
        while True:
            data = self.request.recv(9182)
            if not data:
                break
            # print(msg.decode())
            self.controller.update(data.decode())


if __name__ == '__main__':
    serv = TCPServer(('', 20000), LedRequestHandler)
    serv.serve_forever()
