def make_album(name,band,num_tracks = 0):

    if num_tracks == 'none':
        info = {'name': name, 'band': band}
    else: info = {'name': name, 'band': band, 'tracks': num_tracks}


    return info # returning the value

# using a whileloop to create a user album
while True:
    print("Enter the information about the album.\nType 'q' to quite at anytime.\n")

    a_name = input("Name of the album: ")
    if a_name == 'q':
        break
    b_name = input("Name of the band: ")
    if b_name == 'q':
        break
    num_track = input("Number of tracks in the album: ")
    if num_track == 'q':
        break

    album_des = make_album(a_name,b_name,num_track) # calling the function and storing it into new variable

    print(f'{album_des}' + '\n')
