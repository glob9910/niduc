from device import Device
class signalCompare():
	def signal_compare(Device_A, Device_B):#potem mo�na to przerobic na por�wnywanie tablic z sygna�ami
		if Device_A.signal==Device_B.signal:
			print("SIGNALS EQUAL")
		else :
			print("ERROR")