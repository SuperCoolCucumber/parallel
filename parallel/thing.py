def even_numbers_(in_queue, out_queue):
    my_list = in_queue.get()
    count = 0
    for item in my_list:
        if item % 2 == 0:
            count += 1
    
    out_queue.put(count)