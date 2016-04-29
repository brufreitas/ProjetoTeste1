import threading
import datetime
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, sleep):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.sleep = sleep


    def run(self):
        threadLock.acquire()
        print ("Starting " + self.name)
        threadLock.release()

        print_time(self.name, self.sleep, 9)

        threadLock.acquire()
        threads.remove(self.name)
        print ("Exiting " + self.name)
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        # Get lock to synchronize threads
        threadLock.acquire()
        print ("%s: Counter: %s, %s ativas: %s" % (threadName, counter, datetime.datetime.now(), threading.active_count()))
        # Free lock to release next thread
        threadLock.release()
        counter -= 1


threadLock = threading.Lock()
threadList = ["Thread-1", "Thread-2", "Thread-3", "Thread-4", "Thread-5", "Thread-6",
              "Thread-7", "Thread-8", "Thread-9"]
threads = []
threadID = 1

# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, threadID * 0.5)
    thread.start()
    threads.append(thread)
    threadID += 1

print (threads)

# Wait for all threads to complete
while len(threads) > 0:
    time.sleep(1)
    print ("----------> Ainda tem ativas: " + str(threading.active_count()) + '/' + str(len(threads)))

print ("Exiting Main Thread")
