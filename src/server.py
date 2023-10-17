from __future__ import annotations

from argparse import ArgumentParser
# from email.mime.text import MIMEText
from queue import Queue
import socket
from socketserver import ThreadingTCPServer, BaseRequestHandler
from threading import Thread

import tomli


def student_id() -> int:
    return 12210000  # TODO: replace with your SID


parser = ArgumentParser()
parser.add_argument('--name', '-n', type=str, required=True)
parser.add_argument('--smtp', '-s', type=int)
parser.add_argument('--pop', '-p', type=int)

args = parser.parse_args()

with open('data/config.toml', 'rb') as f:
    _config = tomli.load(f)
    SMTP_PORT = args.smtp or int(_config['server'][args.name]['smtp'])
    POP_PORT = args.pop or int(_config['server'][args.name]['pop'])
    ACCOUNTS = _config['accounts'][args.name]
    MAILBOXES = {account: [] for account in ACCOUNTS.keys()}

with open('data/fdns.toml', 'rb') as f:
    FDNS = tomli.load(f)

ThreadingTCPServer.allow_reuse_address = True


def fdns_query(domain: str, type_: str) -> str | None:
    domain = domain.rstrip('.') + '.'
    return FDNS[type_][domain]


class POP3Server(BaseRequestHandler):
    def handle(self):
        conn = self.request
        ...


class SMTPServer(BaseRequestHandler):
    def handle(self):
        conn = self.request
        ...


def run_server():
    smtp_server = ThreadingTCPServer(('', SMTP_PORT), SMTPServer)
    pop_server = ThreadingTCPServer(('', POP_PORT), POP3Server)

    smtp_thread = Thread(target=smtp_server.serve_forever)
    pop_thread = Thread(target=pop_server.serve_forever)

    smtp_thread.daemon = True
    pop_thread.daemon = True

    smtp_thread.start()
    pop_thread.start()

    while True:
        pass

if __name__ == '__main__':
    if student_id() % 10000 == 0:
        raise ValueError('Invalid student ID')
    
    try:
        run_server()
    except KeyboardInterrupt:
        print('Shutting down...')

