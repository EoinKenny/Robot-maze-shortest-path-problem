class Node(object):

    __next = None
    __element = None
    
    def __init__(self, element=None):
        self.__next = None
        self.__element = element
    
    def get_next(self):
        return self.__next

    def get_element(self):
        return self.__element

    def set_next(self, next):
        self.__next = next

    def set_element(self, element):
        self.__element = element

    def __repr__(self):
        return "node: " + str(self.get_element())
    
    
    
    
class LinkedList(object):

    def __init__(self, node=None):
        self.__first = node

    # def __init__(self, node):
    #     self.__first = node

    def head(self):
        return self.__first

    def add_tail(self, node):
        current = self.head()
        while not current.get_next() == None:
#             if current.get_next() == None:
#                 current.set_next(node)
            current = current.get_next()
        current.set_next(node)

    def add_head(self, node):
        node.set_next(self.head())
        self.__first = node
        
    def remove_head(self):
        self.__first = self.__first.get_next()
        
    def __repr__(self):

        result = ""
        current = self.__my_list.head()
        while not (current is None):
            result += " -> "  + str(current)
            current = current.get_next()
        return result
  
  
class StackLinkedList(object):
    
    __my_list = LinkedList()
    
    def push(self, elem):
    
        node = Node(elem)
        p = self.__my_list.head()
        while p is not None:
            if p.get_element() == node.get_element():
                return False
            p = p.get_next()
        self.__my_list.add_head(node)
        return True

    def pop(self):
        
        p = self.__my_list.head()
        if p is not None:
            self.__my_list.remove_head()
            p = p.get_next()
            
        return 0

    def head(self):
        return self.__my_list.head()
        
    def __str__(self):
        result = "-> "
        p = self.__my_list.head()
        if p is not None:
            while p is not None:
                result += "%s " % str(p.get_element()) + ": "
                p = p.get_next()
        return result
     

current_path = StackLinkedList()
