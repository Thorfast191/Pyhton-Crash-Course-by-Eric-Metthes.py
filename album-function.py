def make_album(name,band,num_tracks = 0):

    if num_tracks:
        info = {'name': name, 'band': band, 'tracks': num_tracks}
    else: info = {'name': name, 'band': band}

    return info # returning the value

# calling the functions
album_des1 = make_album('skyline','omnium gatherum')
album_des2 = make_album('winters gate','insomnium',7)

print(album_des1)
print(album_des2)