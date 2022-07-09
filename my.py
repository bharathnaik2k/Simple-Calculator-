
from colorama import Fore,Back,Style

print(Back.WHITE + Fore.BLACK + Style.BRIGHT + "-------------------------simple calculater------------------------" + Style.RESET_ALL + Fore.RESET + Back.RESET)

print()

print(Fore.YELLOW + "Opstion 1 = Addision" + Fore.RESET)
print(Fore.YELLOW  + Style.DIM + "Opstion 2 = Substrasion" + Style.RESET_ALL + Fore.RESET)
print(Fore.YELLOW + "Opstion 3 = Multifacsion" + Fore.RESET)
print(Fore.YELLOW + "Opstion 4 = Division" + Fore.RESET)

print()

while True :
	opstion = int(input(Fore.MAGENTA + 'Chose Your Opstion (1/2/3/4) >> ' + Fore.RESET))

	print()

	Num1 = int(input(Fore.RED + 'Type your number > ' + Fore.RESET))
	Num2 = int(input(Fore.RED + 'Type your number > ' + Fore.RESET))

	print()

	if opstion == 1 :
		print(Fore.GREEN + f'Answer = {Num1+Num2}' + Fore.RESET)
	elif opstion == 2 :
		print(Fore.GREEN + f'Answer = {Num1-Num2}' + Fore.RESET)
	elif opstion == 3 :
		print(Fore.GREEN + f'Answer = {Num1*Num2}' + Fore.RESET)
	elif opstion == 4 :
		print(Fore.GREEN + f'Answer = {Num1//Num2}' + Fore.RESET)
	else :
		print("That One Opstion Is Invild.....!!!! Please Chose - 1/2/3/4 ")
	
	print()
	
