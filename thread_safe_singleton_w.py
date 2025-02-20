import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()  # Ensures thread safety

    def __new__(cls):
        with cls._lock:  # Ensure only one thread can access this block at a time
            if cls._instance is None:
                cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
                cls._instance.data = "Thread-safe Singleton"
        return cls._instance

# Client code
def create_instance():
    singleton = ThreadSafeSingleton()
    print(singleton.data)

# Creating multiple threads
thread1 = threading.Thread(target=create_instance)
thread2 = threading.Thread(target=create_instance)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

