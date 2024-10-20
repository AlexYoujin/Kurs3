from typing import List


class Product:
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity

    def __repr__(self) -> str:
        return (
            f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
        )


class Category:
    # Атрибуты класса для подсчета категорий и товаров
    total_categories: int = 0
    total_products: int = 0

    def __init__(self, name: str, description: str) -> None:
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = []

        # Увеличиваем количество категорий при создании нового объекта
        Category.total_categories += 1

    def add_product(self, product: Product) -> None:
        self.products.append(product)
        # Увеличиваем количество товаров при добавлении продукта
        Category.total_products += 1

    def __repr__(self) -> str:
        return f"Category(name='{self.name}', products={self.products})"


# Создаем продукты
product1 = Product(name="Молоко", description="Коровье молоко", price=1.5, quantity=100)
product2 = Product(
    name="Хлеб", description="Батон белого хлеба", price=0.8, quantity=50
)

# Создаем категории
dairy_category = Category(name="Молочные продукты", description="Все молочные продукты")
bakery_category = Category(name="Выпечка", description="Все виды хлеба")

# Добавляем продукты в категории
dairy_category.add_product(product1)
bakery_category.add_product(product2)

# Выводим информацию о категориях и количестве
print(dairy_category)
print(bakery_category)
print(f"Всего категорий: {Category.total_categories}")
print(f"Всего товаров: {Category.total_products}")
