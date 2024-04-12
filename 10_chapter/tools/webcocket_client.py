from threading import Thread

import websocket


class WebSocketClient(Thread):
    """
    WebSocket Client
    """

    def __init__(self, url):
        Thread.__init__(self)
        self.ws = websocket.create_connection(url)
        self.running = True
        self.received_messages = []

    def run(self):
        """
        实现运行方法
        :return:
        """
        while self.running:
            try:
                message = self.ws.recv()
                self.received_messages.append(message)
            except websocket.WebSocketConnectionClosedException:
                break
            except Exception as e:
                print(f"WebSocket error: {e}")
                break
        self.ws.close()

    def send_message(self, message):
        """
        发送消息
        :param message:
        :return:
        """
        self.ws.send(message)

    def stop(self):
        """
        停止运行
        :return:
        """
        self.running = False
