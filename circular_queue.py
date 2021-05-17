import unittest

class MyCircularQueue:

    def __init__(self, k: int):
        self.lst: list[int] = [None] * k
        self.size: int = k
        self.front_index: int = 0
        self.rear_index: int = 0

    def enQueue(self, value: int) -> bool:
        if self.Front() < self.size - 1:
            self.lst[self.Front()] = value
            self.front_index += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        self.rear_index += 1
        return True

    def Front(self) -> int:
        return self.front_index

    def Rear(self) -> int:
        return self.rear_index

    def isEmpty(self) -> bool:
        if self.front_index == self.rear_index:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.Front() == self.size - 1:
            return True
        else:
            return False


class TestStringMethods(unittest.TestCase):

    def test_add_1_element_return_true(self):
        q = MyCircularQueue(5)
        self.assertTrue(q.enQueue(value=1))

    def test_add_and_remove_1_element_return_true(self):
        q = MyCircularQueue(5)
        self.assertTrue(q.deQueue())

    def test_add_k_and_1_element_return_false(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k):
            q.enQueue(x)
        self.assertFalse(q.enQueue(1))

    def test_add_1_element_move_tail_to_1(self):
        q = MyCircularQueue(5)
        q.enQueue(value=1)
        self.assertEqual(q.Front(), 1)

    def test_add_and_remove_1_element_move_front_to_1(self):
        q = MyCircularQueue(5)
        q.deQueue()
        self.assertTrue(q.Rear(), 1)

    def test_add_k_and_1_element_move_rear_to_k(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k+1):
            q.enQueue(x)
        self.assertEqual(q.Front(), k - 1)

    def test_empty_queue_is_empty_true(self):
        q = MyCircularQueue(5)
        self.assertTrue(q.isEmpty())

    def test_add_1_element_is_empty_false(self):
        q = MyCircularQueue(5)
        q.enQueue(1)
        self.assertFalse(q.isEmpty())

    def test_add_k_and_1_element_is_full_true(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k + 1):
            q.enQueue(x)
        self.assertEqual(q.size - 1, q.Front())
        self.assertTrue(q.isFull())

if __name__ == '__main__':
    unittest.main()