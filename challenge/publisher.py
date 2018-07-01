
from generator import callback


if __name__=="__main__":
    value = callback.apply_async((1,2), queue="broadcast_tasks")

    print(value.ready())