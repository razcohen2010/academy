import threading
import time
counter = 0
LOOP_COUNT=10
# 1. Define a function for the thread to execute
def counterplus():
    global counter
    print("[plus] Starting thread.")
    for i in range(0, LOOP_COUNT):  
        # counter +=1
        x = counter
        counter = x + 1
        print(f"[plus] working {counter}")

def counterminus():
    global counter
    print("[minus] Starting thread.")
    for i in range(0, 2):
        counter -=1
        print(f"[minus] working {counter}")


print("[Main] Starting main thread.")

# 2. Create thread objects
# 'target' is the function, 'args' is a tuple of arguments passed to it
thread1 = threading.Thread(target=counterplus)
thread2 = threading.Thread(target=counterminus)

# 3. Start the threads (they begin running in the background)
thread1.start()
thread2.start()


print("[Main] Main thread continues running while workers do their job.")

# 4. Wait for both threads to finish before moving on
thread1.join()
thread2.join()

print (f"counter {counter}")
