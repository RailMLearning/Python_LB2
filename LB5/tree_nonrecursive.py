from typing import Callable, Dict, List
from collections import deque

Tree = Dict[str, List["Tree"]]


def gen_bin_tree(
        height: int = 6,
        root: int = 9,
        left_branch: Callable[[int], int] = lambda r: r * 2 + 1,
        right_branch: Callable[[int], int] = lambda r: 2 * r - 1
) -> Tree:
    """
    Генерация бинарного дерева **нерекурсивным способом**.

    :param height: высота дерева (0 = только корень)
    :param root: значение корня
    :param left_branch: функция вычисления левого потомка
    :param right_branch: функция вычисления правого потомка
    :return: дерево в виде словаря {root: [left_subtree, right_subtree]}
    """
    if height < 0:
        raise ValueError("Height must be >= 0")

    # Очередь для построения дерева уровнями
    Node = Dict[str, List]
    tree: Node = {str(root): []}
    queue = deque([(tree[str(root)], root, 1)])  # (ссылка на список поддеревьев, значение, текущая высота)

    while queue:
        children_list, node_value, level = queue.popleft()
        if level > height:
            continue
        # Вычисляем потомков
        l_val = left_branch(node_value)
        r_val = right_branch(node_value)
        # Добавляем словари для потомков
        l_dict = {str(l_val): []}
        r_dict = {str(r_val): []}
        children_list.extend([l_dict, r_dict])
        # Добавляем в очередь
        queue.append((l_dict[str(l_val)], l_val, level + 1))
        queue.append((r_dict[str(r_val)], r_val, level + 1))

    return {str(root): tree[str(root)]}
