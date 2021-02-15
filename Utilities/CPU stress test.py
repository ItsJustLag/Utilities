import math, time, os
try:
    from multiprocessing import Process
except:
    os.system("pip install multiprocessing")
    from multiprocessing import Process

try:
    import psutil
except:
    os.system("pip install psutil")
    import psutil

def main():
    threadcount = int(0)
    while True:
        calc1 = math.factorial(100000000)
        threadcount += 1
        threadcount_ = str(threadcount)
        print("Thread " + threadcount_)

if __name__ == "__main__":
    print("Test started")
    while True:
        while psutil.cpu_percent() < 85:
            Process(target=main).start()
        time.sleep(0.5)