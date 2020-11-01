
import concurrent.futures
import threading
import time

# ------------------------------------Setup-------------------------------------
time_ = lambda: time.perf_counter()

# -------------------------------Synchronous Run--------------------------------

start = time_()

def do_something():
    print("Sleeping 1 second..")
    time.sleep(1)
    print("Done Sleeping..")

do_something()    
do_something()

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# ----------------------------------Threading-----------------------------------

start = time_()

def do_something_thread():
    print("Sleeping 1 second..")
    time.sleep(1)
    print("Done Sleeping..")

thread_1 = threading.Thread(target=do_something_thread)    
thread_2 = threading.Thread(target=do_something_thread)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# -----------------------------Threading in a loop------------------------------
start = time_()

# We don't join our threads inside the loop, because that would cause our code
# to run Synchronously.
threads = list()
for _ in range(10):
    thread_1 = threading.Thread(target=do_something_thread)
    thread_1.start()
    threads.append(thread_1)
    
for thread in threads:
    thread.join()


finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# ---------------------------Concurrent "Thread Pool"---------------------------

start = time_()

def do_something_concurrent(seconds):
    print(f"Sleeping {seconds} seconds('s)..")
    time.sleep(seconds)
    return (f"Done Sleeping.. {seconds} seconds('s)")


with concurrent.futures.ThreadPoolExecutor() as executor:
    future_ = executor.submit(do_something_concurrent, 1)
    print(future_.result())

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# ------------------------------------------------------------------------------
print()
start = time_()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(do_something_concurrent, 1) for _ in range(10)]

    for future_ in concurrent.futures.as_completed(results):
        print(future_.result())

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# ------------------------------------------------------------------------------
print()
start = time_()

with concurrent.futures.ThreadPoolExecutor() as executor:
    sec = [7, 6, 5, 4, 3, 2, 1]
    results = [executor.submit(do_something_concurrent, s) for s in sec]

    for future_ in concurrent.futures.as_completed(results):
        print(future_.result())

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")

# ------------------------------------------------------------------------------
print()
start = time_()

with concurrent.futures.ThreadPoolExecutor() as executor:
    sec = [7, 6, 5, 4, 3, 2, 1]
    results = executor.map(do_something_concurrent, sec)

    for result in results:
        print(result)

finish = time_()

print(f"Finished in {round(finish-start,2)} second('s)")
