import os

def clear(space=50):
    if "PYCHARM_HOSTED" in os.environ:
        print("\n" * space)
    else:
        os.system("cls" if os.name == "nt" else "clear")