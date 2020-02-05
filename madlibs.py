def main():
	time = input("Enter a number between 1 and 12:   ")
	items = input("Name the nearest non-electrical object to you:   ")
	name = input("Who is your favorite singer?    ").title()
	scream = input("What is your favorite song?    ").upper()
	action = input("Enter a verb    ")
	
	print("""It was {} o'clock when I heard a knock at the door.
	I opened the door and there was a box full of {} with a note saying "From {}."
	Just as I closed the door I heard a scream "{}."
	I froze in place and all I could do was {}.""".format(time, items, name, scream, action))





if __name__ == '__main__':
	main()
