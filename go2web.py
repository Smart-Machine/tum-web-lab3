#!/bin/python3

import sys
import socket
import subprocess 

#TODO: Add error handling likewise in Golang.
#TODO: Substitute the whole printing to a logger.
#TODO: Implement redirects.

class WebHandler:

    def __init__(self):
        self.port = 80
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def request(self, url):
        self.socket.connect((url, self.port))
        self.socket.send(f"GET / HTTP/1.1\r\nHost:{url}\r\n\r\n".encode("ascii"))

        response = self.socket.recv(4096)

        self.socket.close()
        return response

if __name__=="__main__":
    web_handler = WebHandler()

    if "-u" in sys.argv:
        response = web_handler.request(sys.argv[-1])
        print(subprocess.run(['lynx', '-stdin', '-dump'], input=response.decode(), capture_output=True, text=True).stdout)
    elif "-s" in sys.argv:
        print("-s")
    else:
        print("go2web -u <URL>         # make an HTTP request to the specified URL and print the response")
        print("go2web -s <search-term> # make an HTTP request to search the term using your favorite search engine and print top 10 results")
        print("go2web -h               # show this help")

