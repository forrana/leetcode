import unittest

class MyCircularQueue:

    def __init__(self, k: int):
        self.lst: list[int] = [None] * k
        self.size: int = k
        self.front_index: int = 0
        self.rear_index: int = 0
        self.elements: int = 0

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            index: int = self.rear_index
            if self.rear_index >= self.size:
                index %= self.size
            self.lst[index] = value
            self.elements += 1
            self.rear_index += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.elements == 0:
            return False
        self.front_index += 1
        if self.front_index > self.size:
            self.front_index = 0
        self.elements -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.lst[self.front_index]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            index: int = self.rear_index
            if self.rear_index >= self.size:
                index %= self.size
            return self.lst[index-1]

    def isEmpty(self) -> bool:
        if self.front_index == self.rear_index:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if (self.rear_index - self.front_index) == self.size:
            return True
        else:
            return False


class TestStringMethods(unittest.TestCase):
    # ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "deQueue", "deQueue", "enQueue", "enQueue", "deQueue", "deQueue", "deQueue", "deQueue"]
    # [ [3],                [1],        [2],        [3],     [],        [],       [3],          [5],    [],         [],         [],         []]
    # [ null,               true,       true,       true,     true,     true,       true,       true,   true,       true,       true,      false]
    def test_leet_code_57(self):
        q = MyCircularQueue(3)
        q.enQueue(1)
        q.enQueue(2)
        q.enQueue(3)
        q.deQueue()
        q.deQueue()
        q.enQueue(3)
        q.enQueue(5)
        q.deQueue()
        q.deQueue()
        q.deQueue()
        print(q.rear_index)
        print(q.front_index)
        self.assertFalse(q.deQueue())

    # ["MyCircularQueue", "enQueue", "enQueue", "deQueue", "enQueue", "deQueue", "enQueue", "deQueue", "enQueue", "deQueue", "Front"]
    # [[2],                 [1],        [2],        [],         [3],    [],         [3],        [],         [3],    [],         []]
    # [null,                true,       true,       true,       true,   true,       true,       true,       true,   true,       3]
    def test_leet_code_56(self):
        q = MyCircularQueue(2)
        q.enQueue(1)
        q.enQueue(2)
        q.deQueue()
        q.enQueue(3)
        q.deQueue()
        q.enQueue(3)
        q.deQueue()
        self.assertTrue(q.enQueue(3))
        q.deQueue()
        self.assertEqual(q.Front(), 3)

    # ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    # [[3],                 [1],        [2],        [3],        [4],    [],     [],         [],     [4],        []]
    # [null,                true,       true,       true,     false,    3,       true,     true,      true,     4]
    def test_leet_code_1(self):
        q = MyCircularQueue(3)
        q.enQueue(1)
        q.enQueue(2)
        q.enQueue(3)
        self.assertFalse(q.enQueue(4))
        self.assertEqual(q.Rear(), 3)
        self.assertEqual(q.isFull(), True)
        self.assertEqual(q.deQueue(), True)
        q.enQueue(4)
        self.assertEqual(q.Rear(), 4)

    def test_dequeue_empty_list_return_false(self):
        q = MyCircularQueue(5)
        self.assertFalse(q.deQueue())

    def test_add_k_elements_remove_first_and_add_new_one_possible_to_add(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k+1):
            q.enQueue(x)
        q.deQueue()
        self.assertTrue(q.enQueue(1))

    def test_add_k_elements_remove_first_and_add_new_one_dequeue_all_empty(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k):
            q.enQueue(x)
        q.deQueue()
        q.enQueue(1)

        for x in range(k+1):
            q.deQueue()

        self.assertFalse(q.isEmpty())

    def test_add_k_elements_remove_first_and_add_new_one_full(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k+1):
            q.enQueue(x)
        q.deQueue()
        q.enQueue(1)
        self.assertTrue(q.isFull())

    def test_add_k_elements_and_remove_first_not_full(self):
        k = 5
        q = MyCircularQueue(k)
        for x in range(k+1):
            q.enQueue(x)
        q.deQueue()
        self.assertFalse(q.isFull())

    def test_add_1_element_return_true(self):
        q = MyCircularQueue(5)
        self.assertTrue(q.enQueue(value=1))

    def test_add_and_remove_1_element_return_true(self):
        q = MyCircularQueue(5)
        q.enQueue(1)
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
        self.assertEqual(q.Rear(), 1)

    def test_add_and_remove_1_element_move_front_to_1(self):
        q = MyCircularQueue(5)
        q.enQueue(1)
        q.deQueue()
        self.assertTrue(q.Front(), None)

    def test_add_k_and_1_element_move_rear_to_k(self):
        k = 5
        q = MyCircularQueue(k)
        q.enQueue(1)
        q.enQueue(2)
        q.enQueue(3)
        q.enQueue(4)
        q.enQueue(5)
        self.assertEqual(q.Rear(), k)

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
        for x in range(k):
            q.enQueue(x)
        self.assertTrue(q.isFull())

if __name__ == '__main__':
    unittest.main()