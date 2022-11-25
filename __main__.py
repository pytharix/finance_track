from finance_track import apps
import socket

host = socket.gethostbyname(socket.gethostname())

if __name__ == "__main__":
    apps.run(host=host, port=5000, debug=True)
