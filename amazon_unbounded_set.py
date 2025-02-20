from abc import ABC, abstractmethod

class ISet(ABC):
    """Interface for a generic set with expiration support."""

    @abstractmethod
    def insert(self, element, ttl):
        """Insert an element with expiration time (TTL in seconds)."""
        pass

    @abstractmethod
    def contains(self, element):
        """Check if an element exists and hasn't expired."""
        pass

    @abstractmethod
    def remove(self, element):
        """Remove an element from the set."""
        pass

    @abstractmethod
    def __iter__(self):
        """Return an iterator over non-expired elements."""
        pass


    @abstractmethod
    def __len__(self):
        """Return the number of non-expired elements."""
        pass


import time

class UnboundedSet(ISet):
    """An unbounded set where each entry has an expiration time."""

    def __init__(self):
        self._set = {}  # Stores elements with expiration times

    def insert(self, element, ttl):
        """Insert an element with a time-to-live (TTL in seconds)."""
        expiration_time = time.time() + ttl
        self._set[element] = expiration_time

    def _cleanup(self):
        """Remove expired elements."""
        current_time = time.time()
        self._set = {k: v for k, v in self._set.items() if v > current_time}

    def contains(self, element):
        """Check if an element exists and hasn't expired."""
        self._cleanup()
        return element in self._set

    def remove(self, element):
        """Remove an element from the set."""
        if element in self._set:
            del self._set[element]

    def __iter__(self):
        """Return an iterator over non-expired elements."""
        self._cleanup()
        return iter(self._set.keys())

    def __len__(self):
        """Return the number of non-expired elements."""
        self._cleanup()
        return len(self._set)
s = UnboundedSet()
s.insert("apple", ttl=3)
s.insert("banana", ttl=5)

print(s.contains("apple"))  # True

time.sleep(4)
print(s.contains("apple"))  # False
print(s.contains("banana")) # True

for element in s:
    print(element)  # Only "banana"
