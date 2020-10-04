#First the list is initialized. The NA's are changed to strings, because python is not happy with just the characters. 
rooms = [1, 2, 1, 3, 1, "NA", 3, 1, 3, 2, 1, "NA", 1, 8, 3, 1, 4, "NA", 1, 3, 1, 2, 1, 7, 1, "NA"]

clean_list_of_rooms = [room for room in rooms if room != "NA"]

room_counter = 0
for room in clean_list_of_rooms:
    if room > 2:
        room_counter += 1

print(room_counter)