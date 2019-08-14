import unittest

from main import Deque


class TestDeque(unittest.TestCase):
    # ------------- TEST ADD_FRONT -----------------------
    def test_add_in_front_with_empty_deque(self):
        deque = Deque()

        deque.addFront(4)
        deque.addFront(5)

        test_result = deque.data
        check_result = [5, 4]
        self.assertEqual(test_result, check_result,
                         "Test 'addFront'. Add elements in front with empty queue. Result arrays not equal")

    def test_add_in_front_with_filled_deque(self):
        deque = Deque()
        deque.data = [1, 2, 3]

        deque.addFront(4)
        deque.addFront(5)

        test_result = deque.data
        check_result = [5, 4, 1, 2, 3]
        self.assertEqual(test_result, check_result,
                         "Test 'addFront'. Add elements in front with filled queue. Result arrays not equal")

    # -------------- TEST ADD_TAIL -------------------------
    def test_add_in_tail_with_empty_deque(self):
        deque = Deque()

        deque.addTail(4)
        deque.addTail(5)

        test_result = deque.data
        check_result = [4, 5]
        self.assertEqual(test_result, check_result,
                         "Test 'addTail'. Add elements in tail with empty queue. Result arrays not equal")

    def test_add_in_tail_with_filled_deque(self):
        deque = Deque()
        deque.data = [1, 2, 3]

        deque.addTail(4)
        deque.addTail(5)

        test_result = deque.data
        check_result = [1, 2, 3, 4, 5]
        self.assertEqual(test_result, check_result,
                         "Test 'addTail'. Add elements in tail with filled queue. Result arrays not equal")

    # -------------- TEST REMOVE_FRONT -----------------------
    def test_remove_front_with_filled_deque(self):
        deque = Deque()
        deque.data = [1, 2, 3, 4, 5]

        test_value = list()
        test_value.append(deque.removeFront())
        test_value.append(deque.removeFront())
        check_value = [1, 2]

        test_result = deque.data
        check_result = [3, 4, 5]

        self.assertEqual(test_value, check_value,
                         "Test 'removeFront'. Remove elements at front with filled queue. Returned data incorrect")
        self.assertEqual(test_result, check_result,
                         "Test 'removeFront'. Remove elements at front with filled queue. Result arrays incorrect")

    def test_remove_front_with_empty_deque(self):
        deque = Deque()

        v1 = deque.removeFront()
        v2 = deque.removeFront()

        test_result = deque.data
        check_result = list()

        self.assertIsNone(v1, "Test 'removeFront'. Remove elements at front with empty queue. Returned data incorrect")
        self.assertIsNone(v2, "Test 'removeFront'. Remove elements at front with empty queue. Returned data incorrect")
        self.assertEqual(test_result, check_result,
                         "Test 'removeFront'. Remove elements at front with empty queue. Result arrays incorrect")

    def test_remove_tail_with_filled_deque(self):
        deque = Deque()
        deque.data = [1, 2, 3, 4, 5]

        test_value = list()
        test_value.append(deque.removeTail())
        test_value.append(deque.removeTail())
        check_value = [5, 4]

        test_result = deque.data
        check_result = [1, 2, 3]

        self.assertEqual(test_value, check_value,
                         "Test 'removeTail'. Remove elements in tail with filled queue. Returned data incorrect")
        self.assertEqual(test_result, check_result,
                         "Test 'removeTail'. Remove elements in tail with filled queue. Result arrays incorrect")

    def test_remove_tail_with_empty_deque(self):
        deque = Deque()

        v1 = deque.removeTail()
        v2 = deque.removeTail()

        test_result = deque.data
        check_result = list()

        self.assertIsNone(v1, "Test 'removeTail'. Remove elements in tail with empty queue. Returned data incorrect")
        self.assertIsNone(v2, "Test 'removeTail'. Remove elements in tail with empty queue. Returned data incorrect")
        self.assertEqual(test_result, check_result,
                         "Test 'removeTail'. Remove elements in tail with empty queue. Result arrays incorrect")


if __name__ == '__main__':
    unittest.main()
