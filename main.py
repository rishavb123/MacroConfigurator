from multiprocessing import Process, Queue

def f(q):
    x = 0
    q.put([x, None, 'hello'])
    while True:
        x += 1
        q.put([x, None, 'hello'])
if __name__  == '__main__':
    q = Queue()
    p = Process(target=f, args=(q, ))
    p.start()
    print(q.get())
    # p.join()
    while True:
        print(q.get())