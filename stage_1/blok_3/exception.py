try:
    print(1 / 0)
except:  # łapie wszystko
    print("wyjątek")
finally:
    print("co by się nie działo to ja się uruchamiam")

try:
    print("info")
except ValueError:
    print("wyjątek")
else:
    print("nie bylo wyjatku")

try:
    raise Exception("Jakis blad")
except Exception as e:
    print(f"to było do przewidzenia...{e}")
else:
    print("to sie nie wykona")
finally:
    print("to się wykona zawsze.")




