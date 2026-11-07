"""Обратная связь от покупателей."""


class FeedbackForm:
    """Форма для отправки сообщения от покупателя."""

    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.sent = False

    def send(self):
        """Отправляет сообщение и меняет его состояние."""
        if not self.message.strip():
            raise ValueError("Message cannot be empty")
        self.sent = True
        return f"Сообщение от пользователя {self.user.name} отправлено"
