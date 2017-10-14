class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.num.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.empty():
            self.num = self.num[1:]
        

    def peek(self):
        """
        :rtype: int
        """
        if empty():
            return self.num[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.num)>0:
            return True
        return False
        
