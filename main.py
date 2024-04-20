from device import Device
from noNoiseChannel import NoNoiseChannel
from signalCompare import signalCompare
from cableCuttedOffChannel import CableCuttedOffChannel

def show_menu():
    print("1. Generate random signal (Device A)")
    print("2. Show signal (Device A)")
    print("3. Show signal (Device A)")
    print("4. Send signal from A to B")
    print("5. No noise channel")
    print("6. Cut the cable!")
    print("7. Compare signals")
    print("0. Quit")    

device_A = Device()
device_B = Device()
noise = NoNoiseChannel()
choice = 1
while choice!=0:
    show_menu()
    choice = input()
    if choice.isnumeric():
        choice = int(choice)

    if choice == 1:
        device_A.create_random_signal()
    elif choice == 2:
        print(device_A.data)
    elif choice == 3:
        print(device_B.data)
    elif choice == 4:
        noise.receive_signal(device_A.send_signal())
        device_B.receive_signal(noise.send_signal())
    elif choice == 5:
        noise = NoNoiseChannel()
    elif choice == 6:
        noise = CableCuttedOffChannel()
    elif choice==7:
        signalCompare.signal_compare(device_A,device_B)
    elif choice == 0:
        print("Quitting")
    else:
        print("No such an option")

