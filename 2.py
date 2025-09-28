# 2 Лабораторная. 3 Задание Комбинированное задание: Система обработки заказов
# с динамическими скидками (Декоратор + Стратегия)
import abc

# 1. Компонент (Component): Базовый интерфейс
class Order(abc.ABC):
    @abc.abstractmethod
    def get_total_cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


# 2. Конкретный Компонент (Concrete Component)
class BasicOrder(Order):

    def get_total_cost(self):
        pass

    def get_description(self):
        pass


# 3. Декоратор (Decorator): Базовый класс
class OrderDiscountDecorator(Order, abc.ABC):
    def __init__(self, decorated_order):
        self._decorated_order = decorated_order

    @abc.abstractmethod
    def get_total_cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


# 4. Конкретные Декораторы (Concrete Decorators): Различные
class  PercentageDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        return self._decorated_order.get_total_cost()*0.9

    def get_description(self):
        pass


class  FixedAmountDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        sum =  self._decorated_order.get_total_cost()
        if sum>=15:
            return self._decorated_order.get_total_cost()-5
        return sum

    def get_description(self):
        pass


class  LoyaltyDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        return self._decorated_order.get_total_cost()*0.5

    def get_description(self):
        pass


# 1. Интерфейс Стратегии (Strategy Interface): Общий интерфейс
class DeliveryCostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self, distance: float, weight: float):
        pass


# 2. Конкретные Стратегии (Concrete Strategies)
class StandardDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return distance*0.1 + weight*1


class ExpressDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return distance*0.2 + weight*2


class FreeDeliveryThreshold(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return 0


# 3. Контекст (Context): Класс, который использует стратегию и декоратор
class OrderProcessor:
    def __init__(self, distance):
        self.distance = distance
        self.items = []
        self.total_amount = 0.0
        self.total_weight = 0.0
        self._delivery_strategy = None
        self._discount_decorator = None

    def add_item(self, item_name: str, price: float, weight: float):
        self.items.append((item_name, price, weight))
        self.total_amount += price
        self.total_weight += weight
        print(f"Добавлен товар: {item_name}, Цена: {price} $, Вес: {weight}")

    def set_discount_decorator(self, decorator: OrderDiscountDecorator):
        self._discount_decorator = decorator
        print(f"Выбрана скидка: {decorator.__class__.__name__}")
    
    def set_delivery_strategy(self, strategy: DeliveryCostStrategy):
        self._delivery_strategy = strategy
        print(f"Установлен способ доставки: {strategy.__class__.__name__}")
    
    def checkout(self):
        self._delivery_strategy.calculate_cost(self.total_weight, self.distance)