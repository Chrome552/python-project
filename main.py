from win10toast import ToastNotifier
from timers import timer
from timers import cdt

choice = int(input('Choose which timer to use:\n1 - Timer\n2 - Countdown Timer\n'))

if choice == 1:
    time = int(input('Enter number of seconds: '))
    timer(time)
    n = ToastNotifier()
    n.show_toast("Notification", "Time's up", duration=5, icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")

elif choice == 2:
    time = int(input('Enter number of seconds: '))
    cdt(time)
    n = ToastNotifier()
    n.show_toast("Notification", "Time's up", duration=5, icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")

else:
    print("Invalid input")