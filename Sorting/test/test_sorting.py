
import unittest

# 각 정렬 알고리즘을 개별 파일에서 가져옴
from ..src.bubble_sort import bubble_sort
from ..src.selection_sort import selection_sort
from ..src.heap_sort import heap_sort
from ..src.merge_sort import merge_sort
from ..src.quick_sort import quick_sort
from ..src.insertion_sort import insertion_sort

class TestSortingAlgorithms(unittest.TestCase):

    # 테스트에 사용할 배열들
    def setUp(self):
        self.test_cases = [
            [64, 25, 12, 22, 11],
            [5, 2, 9, 1, 5, 6],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [1],
            [],
        ]
        self.expected_results = [
            [11, 12, 22, 25, 64],
            [1, 2, 5, 5, 6, 9],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1],
            [],
        ]

    # 버블 정렬 테스트
    def test_bubble_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            bubble_sort(arr_copy)
            self.assertEqual(arr_copy, self.expected_results[i])

    # 삽입 정렬 테스트
    def test_insertion_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            insertion_sort(arr_copy)
            self.assertEqual(arr_copy, self.expected_results[i])

    # 선택 정렬 테스트
    def test_selection_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            selection_sort(arr_copy)
            self.assertEqual(arr_copy, self.expected_results[i])

    # 힙 정렬 테스트
    def test_heap_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            heap_sort(arr_copy)
            self.assertEqual(arr_copy, self.expected_results[i])

    # 병합 정렬 테스트
    def test_merge_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            merge_sort(arr_copy)
            self.assertEqual(arr_copy, self.expected_results[i])

    # 퀵 정렬 테스트
    def test_quick_sort(self):
        for i, arr in enumerate(self.test_cases):
            arr_copy = arr.copy()
            sorted_arr = quick_sort(arr_copy)  # 퀵 정렬은 새로운 리스트를 반환함
            self.assertEqual(sorted_arr, self.expected_results[i])

if __name__ == '__main__':
    unittest.main()
