import sys, time
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    seconds = int(sys.argv[1])
    while seconds > 0:
        print(f"Temps restant : {seconds} sec", end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTimer terminé.")
else:
    print("Usage: timer <secondes>")