

class Counter:
    def __init__(self):
        self.value: int = 0

    def increment(self):
        self.increase(
            1
        )

    def decrement(self):
        self.decrease(
            1
        )

    def reset(self):
        self.set_value(
            0
        )

    def increase(
            self,
            by_value: int
    ):
        self.set_value(
            self.get_value() + by_value
        )

    def decrease(
            self,
            by_value: int
    ):
        self.set_value(
            self.get_value() - by_value
        )

    def get_value_as_string(self) -> str:
        return str(
            self.get_value()
        )

    def get_value(self) -> int:
        return self.value

    def set_value(
            self,
            value: int
    ) -> None:
        self.value = value
