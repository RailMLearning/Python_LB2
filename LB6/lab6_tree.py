"""
Лабораторная работа 6
Сравнение рекурсивной и итеративной реализации построения бинарного дерева.
Выполнил: Rail
Вариант: 9
"""

from typing import Callable, Dict, List
from collections import deque
import timeit
import matplotlib.pyplot as plt

# --- Формулы для левой и правой ветви ---
def left_leaf(root: int) -> int:
    """Вычисляет левый потомок по варианту 9."""
    return root * 2 + 1

def right_leaf(root: int) -> int:
    """Вычисляет правый потомок по варианту 9."""
    return 2 * root - 1

# --- Рекурсивное построение дерева ---
def build_tree_recursive(root: int, height: int,
                         l_b: Callable[[int], int] = left_leaf,
                         r_b: Callable[[int], int] = right_leaf) -> Dict[str, List]:
    """
    Рекурсивная функция построения бинарного дерева.

    :param root: значение корня
    :param height: высота дерева
    :param l_b: функция вычисления левого потомка
    :param r_b: функция вычисления правого потомка
    :return: дерево в виде словаря
    """
    if height < 0:
        raise ValueError("Height cannot be negative")
    if height == 0:
        return {str(root): []}

    left_subtree = build_tree_recursive(l_b(root), height - 1, l_b, r_b)
    right_subtree = build_tree_recursive(r_b(root), height - 1, l_b, r_b)
    return {str(root): [left_subtree, right_subtree]}

# --- Итеративное построение дерева ---
def build_tree_iterative(root: int, height: int,
                         l_b: Callable[[int], int] = left_leaf,
                         r_b: Callable[[int], int] = right_leaf) -> Dict[str, List]:
    """
    Итеративная функция построения бинарного дерева с использованием очереди.

    :param root: значение корня
    :param height: высота дерева
    :param l_b: функция вычисления левого потомка
    :param r_b: функция вычисления правого потомка
    :return: дерево в виде словаря
    """
    if height < 0:
        raise ValueError("Height cannot be negative")

    TreeNode = Dict[str, List]
    root_node: TreeNode = {str(root): []}
    queue = deque([(root_node, root, height)])

    while queue:
        node, value, h = queue.popleft()
        if h > 0:
            l_val = l_b(value)
            r_val = r_b(value)
            left_subtree: TreeNode = {str(l_val): []}
            right_subtree: TreeNode = {str(r_val): []}
            node[str(value)] = [left_subtree, right_subtree]
            queue.append((left_subtree, l_val, h - 1))
            queue.append((right_subtree, r_val, h - 1))
    return root_node

# --- Функция для замера времени и построения графика ---
def benchmark(max_height: int = 6, root: int = 9, repeats: int = 3):
    """
    Сравнивает рекурсивную и итеративную реализацию построения дерева.
    Строит график времени работы.

    :param max_height: максимальная высота дерева для тестирования
    :param root: значение корня дерева
    :param repeats: количество повторов для усреднения времени
    :return: кортеж списков (время рекурсивной реализации, время итеративной)
    """
    heights = list(range(max_height + 1))
    recursive_times = []
    iterative_times = []

    for h in heights:
        r_time = timeit.timeit(lambda: build_tree_recursive(root, h), number=repeats) / repeats
        i_time = timeit.timeit(lambda: build_tree_iterative(root, h), number=repeats) / repeats
        recursive_times.append(r_time)
        iterative_times.append(i_time)

    # --- Построение графика ---
    plt.plot(heights, recursive_times, marker='o', label='Recursive')
    plt.plot(heights, iterative_times, marker='x', label='Iterative')
    plt.xlabel('Height of tree')
    plt.ylabel('Average build time (s)')
    plt.title('Comparison of Recursive and Iterative Tree Building')
    plt.legend()
    plt.grid(True)
    plt.show()

    return recursive_times, iterative_times


if __name__ == "__main__":
    benchmark(max_height=6, root=9, repeats=5)
