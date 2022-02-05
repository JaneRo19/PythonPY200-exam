from typing import Any, Optional


class Node:

    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        self.value = value
        self._next = next_

    def validate_next(self, next_: Optional["Node"] = None) -> None:
        """Метод, который проверяет валидность next"""
        if not isinstance(next_, (type(None), Node)):
            raise TypeError("Следующее значение ноды имеет неверный тип.")

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_):
        self.validate_next(next_)
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

    def validate_next(self, next_: Optional["DoubleLinkedNode"] = None) -> None:
        """Метод, который определяет валидность в DoubleLinkedNode"""
        if not isinstance(next_, (type(None), DoubleLinkedNode)):
            raise TypeError("Следующее значение ноды имеет неверный тип.")

    @staticmethod
    def validate_prev(prev: Optional["DoubleLinkedNode"] = None) -> None:
        """Метод, который проверяет валидность prev"""
        if not isinstance(prev, (type(None), DoubleLinkedNode)):
            raise TypeError("Предыдущее значение ноды имеет неверный тип.")

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev):
        self.validate_prev(prev)
        self._prev = prev

    def __repr__(self) -> str:
        next_ = "None" if self.next is None else f"DoubleLinkedNode({self.next})"
        prev_ = "None" if self.prev is None else f"DoubleLinkedNode({self.prev})"
        return f"DoubleLinkedNode({prev_}, {self.value}, {next_})"
