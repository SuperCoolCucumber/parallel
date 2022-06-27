from multiprocessing import Pool, Process, Queue
from parallel.thing import even_numbers_
import numpy as np

in_queue = Queue()
for _ in range(100):  
    in_queue.put(np.random.randint(10, size=10))

out_queue = Queue() 


processes = []
for _ in range(in_queue.qsize()):
    processes.append(
        Process(target=even_numbers_, args=(in_queue, out_queue))
    )

for process in processes:
    process.start()

for process in processes:
    process.join()

for process in processes:
    process.close()


results = [out_queue.get() for _ in range(out_queue.qsize())]
print(results)
