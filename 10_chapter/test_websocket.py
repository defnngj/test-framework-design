import time
import unittest

from tools.webcocket_client import WebSocketClient


class WebSocketTest(unittest.TestCase):

    def setUp(self):
        """
        创建WebSocket客户端线程
        """
        self.client = WebSocketClient("ws://127.0.0.1:8080/echo")
        self.client.start()
        # 等待客户端连接建立
        time.sleep(1)

    def tearDown(self):
        """
        发送关闭消息
        """
        self.client.send_message("close")
        # 停止WebSocket客户端线程
        self.client.stop()
        self.client.join()

    def test_send_and_receive_message(self):
        """
        测试发送消息
        """
        self.client.send_message("WebSocket!")
        time.sleep(1)
        print(self.client.received_messages)
        self.assertEqual(len(self.client.received_messages), 1)
        self.assertIn("Hello, WebSocket!", self.client.received_messages[0])


if __name__ == '__main__':
    unittest.main()
