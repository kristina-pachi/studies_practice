# 2 Лабораторная. 3 Задание Комбинированное задание: Система обработки заказов
# с динамическими скидками (Декоратор + Стратегия)
import abc

class Order(abc.ABC):
    @abc.abstractmethod
    def get_total_cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


class BasicOrder(Order):

    def get_total_cost(self):
        pass

    def get_description(self):
        pass


class OrderDiscountDecorator(Order, abc.ABC):
    def __init__(self, decorated_order):
        self._decorated_order = decorated_order

    @abc.abstractmethod
    def get_total_cost(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass


class  PercentageDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        pass

    def get_description(self):
        pass


class  FixedAmountDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        pass

    def get_description(self):
        pass


class  LoyaltyDiscount(OrderDiscountDecorator):
    def get_total_cost(self):
        pass

    def get_description(self):
        pass
