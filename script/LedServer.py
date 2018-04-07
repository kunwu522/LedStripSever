from SocketServer import BaseRequestHandler, TCPServer
from LedController import LedController


class LedRequestHandler(BaseRequestHandler):
    def __init__(self, request, client_address, server):
        print('Init Request Handler')
        BaseRequestHandler.__init__(self, request, client_address, server)
        return

    def setup(self):
        print('Setup Request Handler')
        self.controller = LedController()
        self.controller.begin()
        return BaseRequestHandler.setup(self)

    def handle(self):
        print('Got connection from ', self.client_address)
        while True:
            data = self.request.recv(9182)
            if not data:
                break
            # print(msg.decode())
            self.controller.update(data.decode())

    def finish(self):
        print('Finish')
        return BaseRequestHandler.finish(self)

if __name__ == '__main__':
    serv = TCPServer(('', 20000), LedRequestHandler)
    serv.serve_forever()
