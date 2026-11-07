"""Отзывы покупателей о товарах."""


class Review:
    """Отзыв покупателя с оценкой и комментарием."""

    def __init__(self, author, product, rating, comment):
        self.author = author
        self.product = product
        self.rating = rating
        self.comment = comment

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or not 1 <= value <= 5:
            raise ValueError("Rating must be between 1 and 5")
        self._rating = value

    def is_positive(self):
        """Проверяет, является ли оценка положительной."""
        return self.rating >= 4
