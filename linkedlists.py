from collections.abc import MutableSequence
from nodes import Node, DoubleLinkedNode
from typing import Iterable, Any, Optional, Iterator


class LinkedList(MutableSequence):
    """Класс, который реализует односвязный список"""
    def __init__(self, data: Iterable):
        """Конструктор связанного списка"""
        self._len = 0
        self._head = None
        self._tail = self._head

        self.extend(data)

    def validate_index(self, index: int) -> None:
        """Метод, который проверяет, индекс на правильность значения"""
        if not isinstance(index, int):
            raise TypeError("Указан неверный тип индекса, нужен int")
        if not 0 <= index < self._len:
            raise IndexError("Указан неверный индекс")

    def step_by_step_on_nodes(self, index: int) -> [Node, DoubleLinkedNode]:
        """
        Метод, который осуществляет перемещение по узлам до указанного индекса
        и возвращает значение
        """
        self.validate_index(index)

        current_node = self._head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def linked_nodes(self, left_node: Node, right_node: Optional["Node"] = None) -> None:
        """Метод, который связывает между собой два узла ноды в однсвязном списке"""
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """Метод, который возвращает значение узла по оуказанному индексу"""

        self.validate_index(index)
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """Метод, который устанавливает значение узла по указанному индексу"""

        self.validate_index(index)
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        """Метод, который удаляет элемент по указанному индексу"""

        self.validate_index(index)

        if index == 0:
            self._head = self._head.next
        elif index == self._len - 1:
            self._tail = self.step_by_step_on_nodes(index - 1)
            self._tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            current_node_del = prev_node.next
            next_node = current_node_del.next
            self.linked_nodes(prev_node, next_node)

        self._len -= 1

    def __len__(self) -> int:
        """Метод, который возвращает длину связанного списка"""
        return self._len

    def append(self, value: Any) -> None:
        """Метод, который добавляет значение в конец списка"""  # рассматриваю, как частный случай insert
        self.insert(self._len, value)

    def insert(self, index: int, value: Any) -> None:
        """Метод, который добавляет значение по указанному индексу"""
        if not isinstance(index, int):
            raise TypeError("Указан неверный тип индекса, нужен int")
        if not 0 <= index <= self._len:
            raise IndexError("Указан неверный индекс")

        insert_node = self.create_node(value)

        if self._head is None:
            self._head = self._tail = insert_node

        elif index == 0:
            self.linked_nodes(insert_node, self._head)
            self._head = insert_node

        elif index == self._len:
            self.linked_nodes(self._tail, insert_node)
            self._tail = insert_node
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

        self._len += 1

    def create_node(self, value: Any) -> Node:
        """Метод, который создает ноду"""  # использую данный метод для того, чтобы не перегружать методы append, insert в DoubleLinkedList
        return  Node(value)

    def to_list(self) -> list:
        """Метод, который формирует список значений нод"""
        return [value for value in self]

    def __str__(self) -> str:
        """Метод, который возвращает представление списка нод для пользователя"""
        return f"{self.to_list()}"

    def __repr__(self) -> str:
        """Метод, который возвращает представление списка нод"""
        return f"{self.__class__.__name__}({self.to_list()})"

    def node_iterator(self) -> Iterator:
        """Метод, который проходит по всем узлам нод"""
        current_node = self._head
        for _ in range(self._len):
            yield current_node
            current_node = current_node.next

    def __iter__(self) -> Iterator:
        """Метод, который итерируется по узлам нод и возвращает значение"""
        for node in self.node_iterator():
            yield node.value

    def __contains__(self, item: Any) -> bool:
        """Метод, который проверяед вхождение элемента в список"""
        for node in self.node_iterator():
            if node.value == item:
                return True
        return False

    def reversed_iter_nodes(self) -> Iterator:
        """Метод, который проходит по всем узлам нод"""
        for index in range(self._len - 1, -1, -1):
            current_node = self.step_by_step_on_nodes(index)
            yield current_node

    def __reversed__(self) -> Iterator:
        """Метод, котрый возвращает значение списка в обратном порядке"""
        for node in self.reversed_iter_nodes():
            yield node.value

    def count(self, item: Any) -> int:
        """Метод, который подсчитывает количество вхождений указанного значения в список"""
        count = 0
        for node in self.node_iterator():
            if node.value == item:
                count += 1
        return count

    def extend(self, values: Iterable) -> None:
        """Метод, который добавляет в конец списка несколько элементов"""
        if values is not None:
            for value in values:
                self.append(value)

    def remove(self, item: Any) -> None:
        """Метод, который удаляет первое вхождение указанного значения"""
        index = self.index(item)
        self.__delitem__(index)

    def pop(self, index: int) -> Any:
        """Метод, который удаляет элемент по указаному индексу и возвращает значение этого элемента"""
        pop_value = self.__getitem__(index)
        self.__delitem__(index)
        return pop_value

    def index(self, value: Any) -> int:
        """Метод, который возвращает значение индекса в списке указанного значения"""
        if self._head is None:
            raise ValueError("Список пуст")

        current_node = self._head
        for index in range(self._len):
            if current_node.value == value:
                return index
            current_node = current_node.next

        raise ValueError("Данного значения нет в списке")


class DoubleLinkedList(LinkedList):
    """Класс, который реализует двусвязный список"""
    def linked_nodes(self, left_node: DoubleLinkedNode,
                     right_node: Optional["DoubleLinkedNode"] = None) -> None:
        """Метод, который связывает между собой два узла ноды в двунаправленом списке"""
        left_node.next = right_node
        right_node.prev = left_node

    def create_node(self, value: Any) -> DoubleLinkedNode:
        """Метод, который создает ноду"""
        return DoubleLinkedNode(value)

    def reversed_iter_nodes(self) -> Iterator:
        """Метод, который проходит по всем узлам нод"""
        current_node = self._tail   # переопределяю этот метод, так как в данном списке удобнее реализовать с использованием ссылки prev
        for _ in range(self._len):
            yield current_node
            current_node = current_node.prev

    def __delitem__(self, index: int) -> None:   # переопределила этот метод для того, чтобы при удалении не было ссылок prev
        """Метод, который удаляет элемент по указанному индексу"""

        self.validate_index(index)

        if index == 0:
            current_node_del = self._head
            if current_node_del.next is not None:
                current_node_del.next.prev = None
            self._head = self._head.next
            current_node_del.next = None
            if self._head is None:
                self._tail = None
        elif index == self._len - 1:
            current_node_del = self._tail
            self._tail = self._tail.prev
            self._tail.next = None
            current_node_del.prev = None
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            current_node_del = prev_node.next
            next_node = current_node_del.next
            self.linked_nodes(prev_node, next_node)
            current_node_del.next = None
            current_node_del.prev = None

        self._len -= 1


if __name__ == '__main__':
    list_ = [1, 2, 3]                   # задаем последовательно для linked_list
    linked_list = LinkedList(list_)
    print(linked_list)

    print("Метод append LL")
    linked_list.append(9)
    print(linked_list)

    print("Метод insert LL")
    linked_list.insert(0, 0)
    print(linked_list)
    linked_list.insert(2, 0)
    print(linked_list)
    linked_list.insert(len(linked_list), len(linked_list))
    print(linked_list)
    # linked_list.insert(100, 100)
    # print(linked_list)
    linked_list.insert(2, "abc")
    print(linked_list)
    print(linked_list[2] == "abc")

    print("Метод __len__ LL")
    print(len(linked_list))

    print("Метод __delitem__ LL")
    del linked_list[2]
    print(linked_list)
    print(len(linked_list))

    print("Метод __repr__ LL")
    print(repr(linked_list))

    # print(linked_list.index("a"))

    print("Метод pop LL")
    print(linked_list.pop(0))

    print("Метод __iter__ LL")
    iterator = iter(linked_list)
    for i in iterator:
        print(i)

    print("Метод __contains__ LL")
    print(3 in linked_list)

    print("Метод __reversed__ LL")
    revers_iterator = reversed(linked_list)
    for i in revers_iterator:
        print(i)

    print("Метод count LL")
    print(linked_list.count(3))

    print("Метод extend LL")
    linked_list.extend("abc")
    print(linked_list)

    print("Метод remove LL")
    linked_list.append(2)
    linked_list.remove(2)
    print(linked_list)

    print("Append и Extend 'abc'")
    linked_list.append("abc")
    linked_list.extend("abc")
    print(linked_list)

    print('----------------------------------------------')

    list_ = [5, 6, 7, 8]                   # задаем последовательно для double_linked_list
    double_linked_list = DoubleLinkedList(list_)
    print(double_linked_list)

    print("Метод append DLL")
    double_linked_list.append(9)
    print(double_linked_list)
    double_linked_list.append(5)
    print(double_linked_list)

    print("Метод insert DLL")
    double_linked_list.insert(0, 0)
    print(double_linked_list)
    double_linked_list.insert(2, 0)
    print(double_linked_list)
    double_linked_list.insert(len(double_linked_list), len(double_linked_list))
    print(double_linked_list)
    # double_linked_list.insert(100, 100)
    # print(double_linked_list)
    double_linked_list.insert(2, "abc")
    print(double_linked_list)
    print(double_linked_list[2] == "abc")

    print("Метод __len__ DLL")
    print(len(double_linked_list))

    print("Метод __delitem__ DLL")
    del double_linked_list[3]
    print(double_linked_list)
    print(len(double_linked_list))

    print("Метод __repr__ DLL")
    print(repr(double_linked_list))

    print("Метод __iter__ DLL")
    iterator = iter(double_linked_list)
    for i in iterator:
        print(i)

    print("Метод __contains__ DLL")
    print(8 in double_linked_list)

    print("Метод __reversed__ DLL")
    revers_iterator = reversed(double_linked_list)
    for i in revers_iterator:
        print(i)

    print("Метод count DLL")
    print(double_linked_list.count(8))

    print("Метод remove DLL")
    double_linked_list.remove(9)
    print(double_linked_list)

    print("Метод extend DLL")
    double_linked_list.extend([2, 5, 8])
    print(double_linked_list)

    print("Метод pop DLL")
    list_new = [1, 2, 3, 4]
    double_linked_list = DoubleLinkedList(list_new)
    print(double_linked_list)
    print(double_linked_list.pop(2)) # mid
    print(double_linked_list)
    print(double_linked_list.pop(2)) #tail
    print(double_linked_list)
    #print(double_linked_list.pop(0)) #head
    print(double_linked_list.pop(1))  # tail
    print(double_linked_list)
    print(double_linked_list.pop(0))  # last
    print(double_linked_list)
    print('done')

