from typing import Any, Optional


class Node:

    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self._next = next_

    @classmethod
    def is_node_valid(cls, node):
        if not isinstance(node, (type(None), cls)):
            raise TypeError("Значение ноды имеет неверный тип.")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_):
        self.is_node_valid(next_)
        self._next = next_

    def __repr__(self) -> str:
        if self.next is None:
            return f"Node({self.value}, None)"
        else:
            return f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return f"{self.value}"

    def __del__(self) -> None:
        print(f"Node({self.value}) удалена")


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional["DoubleLinkedNode"] = None,
                 prev: Optional["DoubleLinkedNode"] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.is_node_valid(prev)
        self._prev = prev

    def __repr__(self) -> str:
        next_ = "None" if self.next is None else f"DoubleLinkedNode({self.next})"
        prev_ = "None" if self.prev is None else f"DoubleLinkedNode({self.prev})"
        return f"DoubleLinkedNode({prev_}, {self.value}, {next_})"
