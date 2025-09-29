# 2 Лабораторная. 3 Задание Комбинированное задание: Система обработки заказов
# с динамическими скидками (Декоратор + Стратегия)
import abc
from typing import Type


# 1. Компонент (Component): Базовый интерфейс
class Order(abc.ABC):
    @abc.abstractmethod
    def get_total_cost(self) -> float:
        """Возвращает итоговую стоимость заказа."""

        pass

    @abc.abstractmethod
    def get_description(self) -> str:
        """Возвращает описание заказа."""

        pass


# 2. Конкретный Компонент (Concrete Component)
class BasicOrder(Order):
    def __init__(self, total_amount: float):
        """Создаёт базовый заказ."""

        self.total_amount = total_amount

    def get_total_cost(self) -> float:
        """Возвращает сумму заказа без скидок."""

        return self.total_amount

    def get_description(self) -> str:
        """Описание базового заказа."""

        return f"Базовая стоимость заказа: {self.total_amount:.2f}$"


# 3. Декоратор (Decorator): Базовый класс
class OrderDiscountDecorator(Order, abc.ABC):
    def __init__(self, decorated_order: Order):
        """Инициализирует декоратор скидки."""

        self._decorated_order = decorated_order

    @abc.abstractmethod
    def get_total_cost(self) -> float:
        """Возвращает стоимость заказа с применённой скидкой."""

        pass

    @abc.abstractmethod
    def get_description(self) -> str:
        """Возвращает описание заказа с учётом скидки."""

        pass


# 4. Конкретные Декораторы (Concrete Decorators)
class PercentageDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        return self._decorated_order.get_total_cost() * 0.9

    def get_description(self) -> str:
        return (
            self._decorated_order.get_description()
            + f". Сумма с учётом скидки 10%: {self.get_total_cost():.2f}$"
        )


class FixedAmountDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        total = self._decorated_order.get_total_cost()
        if total >= 15:
            return total - 5
        return total

    def get_description(self) -> str:
        return (
            self._decorated_order.get_description()
            + f". Сумма с учётом скидки 5$: {self.get_total_cost():.2f}$"
        )


class LoyaltyDiscount(OrderDiscountDecorator):
    def get_total_cost(self) -> float:
        return self._decorated_order.get_total_cost() * 0.5

    def get_description(self) -> str:
        return (
            self._decorated_order.get_description()
            + f". Сумма с учётом скидки 50% для лояльных клиентов: {self.get_total_cost():.2f}$"
        )


# 1. Интерфейс Стратегии (Strategy Interface)
class DeliveryCostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self, distance: float, weight: float) -> float:
        """Рассчитывает стоимость доставки."""

        pass


# 2. Конкретные Стратегии (Concrete Strategies)
class StandardDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 0.2 + weight * 1


class ExpressDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return distance * 0.4 + weight * 3


class FreeDeliveryThreshold(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float) -> float:
        return 0


# 3. Контекст (Context): Класс, который использует стратегию и декоратор
class OrderProcessor:
    def __init__(self, distance: float):
        """Инициализирует обработчик заказа."""

        if not isinstance(distance, (int, float)):
            raise TypeError(f"Расстояние должно быть числовым, а не {type(distance).__name__}")
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным")

        self.distance = distance
        self.items = []
        self.total_amount = 0.0
        self.total_weight = 0.0
        self._delivery_strategy = None
        self._discount_decorator = None

    def add_item(self, item_name: str, price: float, weight: float):
        """Добавляет товар в корзину."""

        if not isinstance(price, (int, float)):
            raise TypeError(f"price должна быть числом, а не {type(price).__name__}")
        if not isinstance(weight, (int, float)):
            raise TypeError(f"weight должна быть числом, а не {type(weight).__name__}")

        self.items.append((item_name, price, weight))
        self.total_amount += price
        self.total_weight += weight
        print(f"Добавлен товар: {item_name}, Цена: {price:.2f}$, Вес: {weight} кг")

    def set_discount_decorator(self, decorator: Type[OrderDiscountDecorator]):
        """Устанавливает класс декоратора скидки."""

        self._discount_decorator = decorator
        print(f"Выбрана скидка: {decorator.__name__}")

    def set_delivery_strategy(self, strategy: DeliveryCostStrategy):
        """Устанавливает стратегию расчёта доставки."""

        self._delivery_strategy = strategy
        print(
            f"Установлен способ доставки: "
            f"{strategy.__class__.__name__} на расстояние {self.distance:.2f} км"
        )

    def checkout(self):
        """Оформляет заказ, рассчитывает скидку и доставку, выводит результат."""

        if not self.items:
            raise ValueError("Для оформления заказа добавьте товар в корзину")
        base_order = BasicOrder(self.total_amount)

        if self._discount_decorator:
            decorated_order = self._discount_decorator(base_order)
        else:
            decorated_order = base_order

        if self._delivery_strategy is None:
            raise ValueError("Для оформления заказа выберите способ доставки")

        delivery_cost = self._delivery_strategy.calculate_cost(
            self.distance, self.total_weight
        )
        if delivery_cost >= 50:
            delivery_cost = 50

        final_cost = decorated_order.get_total_cost() + delivery_cost

        print(decorated_order.get_description())
        print(f"Стоимость доставки: {delivery_cost:.2f}$")
        print(f"Итоговая стоимость заказа: {final_cost:.2f}$")

processor1 = OrderProcessor(distance=15.55)
processor1.add_item("Ноутбук", 1000.00, 2.5)
processor1.set_delivery_strategy(FreeDeliveryThreshold())
processor1.set_discount_decorator(PercentageDiscount)
processor1.checkout()

print('---------------------------------------------------------------------')

processor2 = OrderProcessor(distance=50)
processor2.add_item("Наушники", 350.50, 0.5)
processor2.add_item("Беспроводная мышка", 14.99, 0.2)
processor2.add_item("Коврик для пк мышки", 5.00, 0.1)
processor2.set_delivery_strategy(StandardDelivery())
processor2.set_discount_decorator(FixedAmountDiscount)
processor2.checkout()

print('---------------------------------------------------------------------')

processor3 = OrderProcessor(distance=75)
processor3.add_item("ПК", 1999.99, 10)
processor3.set_delivery_strategy(ExpressDelivery())
processor3.set_discount_decorator(LoyaltyDiscount)
processor3.checkout()

print('---------------------------------------------------------------------')

# Processor4: ошибка при создании из-за отрицательного distance
try:
    processor4 = OrderProcessor(distance=-5)
except Exception as e:
    print(f"Ошибка при создании processor4: {e}")
else:
    try:
        processor4.checkout()
    except Exception as e:
        print(f"Ошибка: {e}")


# Processor5: ошибка при добавлении товара с неверным типом price
try:
    processor5 = OrderProcessor(distance=34)
    processor5.add_item('ПК', 'сто', 10)
except Exception as e:
    print(f"Ошибка: {e}")
else:
    try:
        processor5.checkout()
    except Exception as e:
        print(f"Ошибка: {e}")


# Processor6: ошибка при пустом шоппинг листе
processor6 = OrderProcessor(distance=34)
try:
    processor6.checkout()
except Exception as e:
    print(f"Ошибка: {e}")

# Processor7: ошибка, не выбран способ доставки
processor7 = OrderProcessor(distance=60)
processor7.add_item('ПК', 1000, 10)
try:
    processor7.checkout()
except Exception as e:
    print(f"Ошибка: {e}")
