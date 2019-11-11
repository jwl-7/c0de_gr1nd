from test_framework import generic_test
from test_framework.test_failure import TestFailure
from sortedcontainers import SortedDict


class ClientsCreditsInfo:

    def __init__(self):
        self.offset = 0
        self.clients = {}
        self.credits = SortedDict()

    def insert(self, client_id, c):
        self.remove(client_id)
        self.clients[client_id] = c - self.offset
        self.credits[c - self.offset] = client_id

    def remove(self, client_id):
        if client_id not in self.clients:
            return False
        credit = self.clients[client_id]
        if not self.credits[credit]:
            del self.credits[credit]
        del self.clients[client_id]
        return True

    def lookup(self, client_id):
        if client_id not in self.clients:
            return -1
        credit = self.clients[client_id]
        return credit + self.offset

    def add_all(self, C):
        self.offset += C

    def max(self):
        if not self.credits:
            return ''
        return self.credits.peekitem(-1)[1]


def client_credits_info_tester(ops):
    cr = ClientsCreditsInfo()

    for x in ops:
        op = x[0]
        s_arg = x[1]
        i_arg = x[2]
        if op == 'ClientsCreditsInfo':
            pass
        if op == 'max':
            result = cr.max()
            if result != s_arg:
                raise TestFailure('Max: return value mismatch')
        elif op == 'remove':
            result = cr.remove(s_arg)
            if result != i_arg:
                raise TestFailure('Remove: return value mismatch')
        elif op == 'insert':
            cr.insert(s_arg, i_arg)
        elif op == "add_all":
            cr.add_all(i_arg)
        elif op == "lookup":
            result = cr.lookup(s_arg)
            if result != i_arg:
                raise TestFailure('Lookup: return value mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("adding_credits.py",
                                       'adding_credits.tsv',
                                       client_credits_info_tester))
