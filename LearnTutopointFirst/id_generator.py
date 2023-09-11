def id_sequence():
    counter = 0
    while True:
        counter +=1
        yield counter
sequence_id = id_sequence()