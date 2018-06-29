
from task1 import sendmail


if __name__=="__main__":
    value = sendmail.apply_async((1,2), queue="broadcast_tasks")

    print(value.ready())