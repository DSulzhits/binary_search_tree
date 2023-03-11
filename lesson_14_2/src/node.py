"""Заказчик хочет оптимизировать работу бэкэнда веб-блога.
Надо построить хранение коротких постов блога в оперативной памяти, чтобы скорость поиска
и выдачи данных конкретного поста по id была очень высокой.
При этом новые посты также будут добавляться к существующим"""


class Node:
    """Класс для представления узла с данными."""

    def __init__(self, data: dict) -> None:
        """Узел инициализируется словарем с данными."""
        self.data = data
        self.left = None
        self.right = None

