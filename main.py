#notifier

from plyer import notification
import time
if __name__ ==__name__:
    while True:
        notification.notify(
        title = "It's time to take rest",
        message=" Technologies, such as handheld tablets, smartphones, and computers, can hold a person's attention for long periods. This maylead     to eyestrain. Symptoms of digital eyestrain can include blurred vision and dry eyes." ,
        timeout=10
        )
        time.sleep(3600*2)
