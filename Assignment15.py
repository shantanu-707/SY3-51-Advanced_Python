import gc
import sys
import time
import weakref
import tracemalloc


def section(title):
    print("\n========", title, "========")

class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(self.name, "destroyed")

def exp1():
    section("1. Reference Counting")

    a = Node("A")
    print("Reference count:", sys.getrefcount(a))

    b = a
    print("After b = a:", sys.getrefcount(a))

    del a
    print("After deleting a:", sys.getrefcount(b))

    del b
    print("Object destroyed immediately")

def exp2():
    section("2. Reference Cycle")

    gc.collect()
    gc.disable()

    print("GC enabled?", gc.isenabled())

    x = Node("X")
    y = Node("Y")

    x.other = y
    y.other = x

    del x, y
    print("Deleted both names. Objects are still in memory.")

    print("Collected:", gc.collect())

    gc.enable()

def exp3():
    section("3. GC Thresholds and Statistics")

    print("Thresholds:", gc.get_threshold())
    print("Counts:", gc.get_count())
    print("Statistics:", gc.get_stats())

def exp4():
    section("4. Automatic Collection")

    events = []

    def watcher(phase, info):
        if phase == "stop":
            events.append(info["generation"])

    gc.callbacks.append(watcher)

    old = gc.get_threshold()
    gc.collect()
    gc.set_threshold(50, 5, 5)

    for i in range(300):
        a = []
        b = []
        a.append(b)
        b.append(a)

    gc.set_threshold(*old)
    gc.callbacks.remove(watcher)

    print("Automatic collections:", len(events))
    print("Generations collected:", events)

def exp5():
    section("5. GC Generations")

    gc.collect()

    keeper = [Node("K")]
    keeper[0].other = keeper

    print("Before collection:",
          [len(gc.get_objects(g)) for g in range(3)])

    gc.collect(0)
    print("After generation 0:",
          [len(gc.get_objects(g)) for g in range(3)])

    gc.collect(1)
    print("After generation 1:",
          [len(gc.get_objects(g)) for g in range(3)])

    keeper[0].other = None
    del keeper

def exp6():
    section("6. Memory Measurement")

    gc.collect()
    gc.disable()

    tracemalloc.start()
    base = tracemalloc.get_traced_memory()[0]

    for i in range(20000):
        a = {}
        b = {}
        a["b"] = b
        b["a"] = a
        del a, b

    used = tracemalloc.get_traced_memory()[0] - base

    print("Memory before collection:",
          round(used / 1024, 2), "KB")

    collected = gc.collect()

    after = tracemalloc.get_traced_memory()[0] - base

    print("Objects collected:", collected)
    print("Memory after collection:",
          round(after / 1024, 2), "KB")

    tracemalloc.stop()
    gc.enable()

def exp7():
    section("7. DEBUG_SAVEALL")

    gc.collect()
    gc.set_debug(gc.DEBUG_SAVEALL)

    p = [1]
    q = [2]

    p.append(q)
    q.append(p)

    del p, q

    gc.collect()

    print("Garbage:", gc.garbage)

    gc.set_debug(0)
    gc.garbage.clear()
    gc.collect()

def exp8():
    section("8. Object Tracking and Weak References")

    values = [5, "hello", [1, 2], {}, (1, 2)]

    for obj in values:
        print(type(obj).__name__, gc.is_tracked(obj))

    n = Node("W")
    ref = weakref.ref(n)

    print("Weak reference alive:", ref() is not None)

    del n

    print("After deletion:", ref() is not None)

def exp9():
    section("9. Freeze and Unfreeze")

    gc.collect()

    print("Before freeze:", gc.get_freeze_count())

    gc.freeze()
    print("After freeze:", gc.get_freeze_count())

    gc.unfreeze()
    print("After unfreeze:", gc.get_freeze_count())

def exp10():
    section("10. GC Timing")

    def work():
        data = []
        for i in range(400000):
            data.append([i])

    for enabled in [True, False]:
        gc.collect()

        if enabled:
            gc.enable()
            print("GC enabled:", end=" ")
        else:
            gc.disable()
            print("GC disabled:", end=" ")

        start = time.perf_counter()
        work()
        end = time.perf_counter()

        print(round((end - start) * 1000, 2), "ms")

    gc.enable()

if __name__ == "__main__":
    print("Python Version:", sys.version.split()[0])

    exp1()
    exp2()
    exp3()
    exp4()
    exp5()
    exp6()
    exp7()
    exp8()
    exp9()
    exp10()