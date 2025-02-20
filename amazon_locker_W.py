from typing import List, Optional
from abc import ABC, abstractmethod

# -------------------------
# Product Class
# -------------------------
class Product:
    """Represents a product with dimensions."""
    def __init__(self, name: str, width: float, height: float, depth: float):
        self.name = name
        self.width = width
        self.height = height
        self.depth = depth

# -------------------------
# Box Class
# -------------------------
class Box:
    """Represents a shipping box."""
    def __init__(self):
        self.width = 0
        self.height = 0
        self.depth = 0
        self.weight = 0
        self.products: List[Product] = []

    def add_product(self, product: Product):
        """Adds a product and updates box dimensions."""
        self.products.append(product)
        self.width = max(self.width, product.width)
        self.height += product.height  # Stacking assumption
        self.depth = max(self.depth, product.depth)

    def calculate_size(self):
        """Returns final box dimensions."""
        return self.width, self.height, self.depth

# -------------------------
# Locker Class
# -------------------------
class Locker:
    """Represents an Amazon Locker compartment."""
    def __init__(self, size: str, width: float, height: float, depth: float, max_weight: float):
        self.size = size
        self.width = width
        self.height = height
        self.depth = depth
        self.max_weight = max_weight

    def can_fit(self, box: Box) -> bool:
        """Checks if a box fits within the locker dimensions."""
        return (box.width <= self.width and
                box.height <= self.height and
                box.depth <= self.depth and
                box.weight <= self.max_weight)

# -------------------------
# Strategy Interface: Locker Selection
# -------------------------
class LockerSelectionStrategy(ABC):
    """Interface for locker selection strategies."""
    @abstractmethod
    def find_best_locker(self, box: Box, lockers: List[Locker]) -> Optional[Locker]:
        pass

# Strategy: Smallest Locker that Fits
class SmallestLockerStrategy(LockerSelectionStrategy):
    def find_best_locker(self, box: Box, lockers: List[Locker]) -> Optional[Locker]:
        """Finds the smallest locker that fits the box."""
        for locker in sorted(lockers, key=lambda l: (l.width, l.height, l.depth)):
            if locker.can_fit(box):
                return locker
        return None

# Strategy: Largest Locker that Fits
class LargestLockerStrategy(LockerSelectionStrategy):
    def find_best_locker(self, box: Box, lockers: List[Locker]) -> Optional[Locker]:
        """Finds the largest locker that fits the box."""
        for locker in sorted(lockers, key=lambda l: (-l.width, -l.height, -l.depth)):
            if locker.can_fit(box):
                return locker
        return None





# -------------------------
# Locker Manager
# -------------------------
class LockerManager:
    """Manages lockers using a strategy."""
    def __init__(self, lockers: List[Locker], strategy: LockerSelectionStrategy):
        self.lockers = lockers
        self.strategy = strategy

    def find_best_locker(self, box: Box) -> Optional[Locker]:
        """Uses the strategy to find the best locker."""
        return self.strategy.find_best_locker(box, self.lockers)

# -------------------------
# Strategy Interface: Box Optimization
# -------------------------
class BoxOptimizationStrategy(ABC):
    """Interface for box optimization strategies."""
    @abstractmethod
    def optimize_box(self, products: List[Product]) -> Box:
        pass

# Strategy: Stacking Box
class StackingBoxStrategy(BoxOptimizationStrategy):
    def optimize_box(self, products: List[Product]) -> Box:
        """Stacks items to optimize height."""
        box = Box()
        for product in products:
            box.add_product(product)
        return box

# Strategy: Compact Box (Placeholder for advanced packing logic)
class CompactBoxStrategy(BoxOptimizationStrategy):
    def optimize_box(self, products: List[Product]) -> Box:
        """Packs items in a more compact way (advanced algorithm placeholder)."""
        box = Box()
        for product in products:
            box.add_product(product)
        return box

# -------------------------
# Box Optimizer
# -------------------------
class BoxOptimizer:
    """Optimizes a box using a strategy."""
    def __init__(self, strategy: BoxOptimizationStrategy):
        self.strategy = strategy

    def optimize_box(self, products: List[Product]) -> Box:
        return self.strategy.optimize_box(products)
