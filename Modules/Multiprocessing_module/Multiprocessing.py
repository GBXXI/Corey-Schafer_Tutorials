
import concurrent.futures
import multiprocessing
import time

# ------------------------------------Setup-------------------------------------
time_ = lambda: time.perf_counter()


def do_something():
    print("Sleeping 1 second..")
    time.sleep(1)
    print("Done Sleeping..")

def do_something_process():
    print("Sleeping 1 second..")
    time.sleep(1)
    print("Done Sleeping..")

def do_something_concurrent(seconds):
    print(f"Sleeping {seconds} seconds('s)..")
    time.sleep(seconds)
    return (f"Done Sleeping.. {seconds} seconds('s)")


# ------------------------------------------------------------------------------
if __name__ == "__main__":

# -------------------------------Synchronous Run--------------------------------
    start = time_()

    do_something()    
    do_something()

    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")

# --------------------------------Multiprocessing-------------------------------
    print()
    start = time_()
    process_1 = multiprocessing.Process(target=do_something_process)    
    process_2 = multiprocessing.Process(target=do_something_process)

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")

# ---------------------------Multiprocessing in a loop--------------------------
    print()
    start = time_()

    # We don't join our threads inside the loop, because that would cause our code
    # to run Synchronously.
    processes = list()
    for _ in range(10):
        process_1 = multiprocessing.Process(target=do_something_process)
        process_1.start()
        processes.append(process_1)
        
    for process in processes:
        process.join()


    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")   

# ------------------------------------------------------------------------------
    print()
    processes = list()
    for _ in range(10):
        process_1 = multiprocessing.Process(target=do_something_concurrent, args=[1.5])
        process_1.start()
        processes.append(process_1)
        
    for process in processes:
        process.join()


    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")   

# ---------------------------Concurrent "Process Pool"--------------------------     
    print()
    start = time_()

    # With python3.8 an OSError occurs, "Handle is closed", by using version 3.9
    # everything works perfectly.
    with concurrent.futures.ProcessPoolExecutor() as executor:
        future_ = executor.submit(do_something_concurrent, 1.7)
        print(future_.result())
    
    finish = time_()
    
    print(f"Finished in {round(finish-start,2)} second('s)")
    
# ------------------------------------------------------------------------------
    print()
    start = time_()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(do_something_concurrent, 1.3) for _ in range(10)]

        for future_ in concurrent.futures.as_completed(results):
            print(future_.result())

    finish = time_()
    
    print(f"Finished in {round(finish-start,2)} second('s)")
    
# ------------------------------------------------------------------------------
    print()
    start = time_()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        sec = [7, 6, 5, 4, 3, 2, 1]
        results = [executor.submit(do_something_concurrent, s) for s in sec]

        for future_ in concurrent.futures.as_completed(results):
            print(future_.result())

    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")

# ------------------------------------------------------------------------------
    print()
    start = time_()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        sec = [7, 6, 5, 4, 3, 2, 1]
        results = executor.map(do_something_concurrent, sec)

        for result in results:
            print(result)

    finish = time_()

    print(f"Finished in {round(finish-start,2)} second('s)")

