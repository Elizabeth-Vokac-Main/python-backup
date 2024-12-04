# fill dictionary from input

hotel_bookings1 = {'846': 'Abe'}
hotel_bookings2 = {}
ref_record1 = hotel_bookings1  # For testing purposes, ref_record1 references hotel_bookings1
ref_record2 = hotel_bookings2  # For testing purposes, ref_record2 references hotel_bookings2

input_line = input()
while input_line != 'exit':
	room, guest = input_line.split()
	hotel_bookings2[room] = guest
	input_line = input()
