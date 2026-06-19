class MyQueue(object):

    def __init__(self):
        self.istack = []
        self.ostack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.istack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.ostack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.ostack:
            while self.istack:
                self.ostack.append(self.istack.pop())
        return self.ostack[-1] if self.ostack else None

    def empty(self):
        """
        :rtype: bool
        """
        return not self.ostack and not self.istack