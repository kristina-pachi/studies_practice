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

    def __init__(self, total_amount):
        self.total_amount = total_amount

    def get_total_cost(self):
        return self.total_amount

    def get_description(self):
        return f"Базовая стоимость заказа: {self.total_amount:.2f}$"



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
        return self._decorated_order.get_description() + f'. Сумма с учётом скидки в 10%: {self.get_total_cost():.2f}$ '


class  FixedAmountDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        sum =  self._decorated_order.get_total_cost()
        if sum>=15:
            return self._decorated_order.get_total_cost()-5
        return sum

    def get_description(self):
        return self._decorated_order.get_description() + f'. Сумма с учётом скидки в 5$ : {self.get_total_cost():.2f}$ '


class  LoyaltyDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        return self._decorated_order.get_total_cost()*0.5

    def get_description(self):
        return self._decorated_order.get_description() + f'. Сумма с учётом скидки в 50%, для лояльных клиентов: {self.get_total_cost():.2f}$ '


# 1. Интерфейс Стратегии (Strategy Interface): Общий интерфейс
class DeliveryCostStrategy(abc.ABC):
    @abc.abstractmethod
    def calculate_cost(self, distance: float, weight: float):
        pass


# 2. Конкретные Стратегии (Concrete Strategies)
class StandardDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return distance*0.2 + weight*1


class ExpressDelivery(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return distance*0.4 + weight*3


class FreeDeliveryThreshold(DeliveryCostStrategy):
    def calculate_cost(self, distance: float, weight: float):
        return 0


# 3. Контекст (Context): Класс, который использует стратегию и декоратор
class OrderProcessor:
    def __init__(self, distance):
        if not isinstance(distance, (int, float)):
            raise TypeError(f"Расстояние должно быть числовым, а не {type(distance).__name__}")
        
        if distance <= 0:
            raise ValueError("Расстояние - положительное число")

        self.distance = distance
        self.items = []
        self.total_amount = 0.0
        self.total_weight = 0.0
        self._delivery_strategy = None
        self._discount_decorator = None

    def add_item(self, item_name: str, price: float, weight: float):
        if not isinstance(price, (int, float)):
            raise TypeError(f"price должна быть числом, а не {type(price).__name__}")

        if not isinstance(weight, (int, float)):
            raise TypeError(f"weight должн быть числом, а не {type(weight).__name__}")
        self.items.append((item_name, price, weight))
        self.total_amount += price
        self.total_weight += weight
        print(f"Добавлен товар: {item_name}, Цена: {price:.2f}$, Вес: {weight} кг")

    def set_discount_decorator(self, decorator: OrderDiscountDecorator):
        self._discount_decorator = decorator
        print(f"Выбрана скидка: {decorator.__name__}")
    
    def set_delivery_strategy(self, strategy: DeliveryCostStrategy):
        self._delivery_strategy = strategy
        print(f"Установлен способ доставки: {strategy.__class__.__name__} на расстояние в {self.distance:.2f} км")
    
    def checkout(self):
        if self.items == []:
            raise ValueError('Для оформления заказа добавьте товар в корзину')
        base_order = BasicOrder(self.total_amount)
        if self._discount_decorator:
            decorated_order = self._discount_decorator(base_order)
        else:
            decorated_order = base_order
        
        if self._delivery_strategy == None:
            raise ValueError('Для оформления заказа выберите способ доставки')

        delivery_cost = self._delivery_strategy.calculate_cost(self.distance, self.total_weight)
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
        print(f"Ошибка при checkout у processor4: {e}")


# Processor5: ошибка при добавлении товара с неверным типом price
try:
    processor5 = OrderProcessor(distance=34)
    processor5.add_item('ПК', 'сто', 10)
except Exception as e:
    print(f"Ошибка в processor5: {e}")
else:
    try:
        processor5.checkout()
    except Exception as e:
        print(f"Ошибка при checkout у processor5: {e}")


# Processor6: ошибка при пустом шоппинг листе
processor6 = OrderProcessor(distance=34)
try:
    processor6.checkout()
except Exception as e:
    print(f"Ошибка при checkout у processor6: {e}")

# Processor7: ошибка, не выбран способ доставки
processor7 = OrderProcessor(distance=60)
processor7.add_item('ПК', 1000, 10)
try:
    processor7.checkout()
except Exception as e:
    print(f"Ошибка при checkout у processor7: {e}")
