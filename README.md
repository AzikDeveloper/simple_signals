# simple_signals
Simple signal implementation like Django's one

```
from core.signals import pre_init, post_init


class Car:
    def __init__(self, name, wheels):
        pre_init.send(self.__class__, self, name, wheels)

        self.name = name
        # some magic here
        self.wheels = wheels
        print(f"Car {self.name} is initiated")

        post_init.send(self.__class__, self)


def save_car_to_cache(sender, instance, name, wheels):
    print(f"save_to_cache: {name}")


def save_car_to_db(sender, instance):
    print(f"save_to_db: {instance.name}")


pre_init.connect(save_car_to_cache, sender=Car)
post_init.connect(save_car_to_db, sender=Car)

car1 = Car("BMW", 4)
```

**Result:**
```
save_to_cache: BMW
Car BMW is initiated
save_to_db: BMW
```
