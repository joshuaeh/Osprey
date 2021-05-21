from code.BestBuyBird import BBbird, timestamp
from multiprocessing import Pool

def osprey(name, url, headless=True, threading=False, texts=True):
    print(f'{timestamp()}[{name}]Creating Instance')
    instance = BBbird(name, url, headless, threading, texts)
    print(f'{timestamp()}[{name}]Instance Created')
    print(f'{timestamp()}[{name}]Attempting to Open Page')
    instance.open_page()
    print(f'{timestamp()}[{name}]Page opened')
    print(f'{timestamp()}[{name}]Attempting to Checkout')
    instance.checkout()
    print(f'{timestamp()}[{name}]Checkout Successful. Nice.')
    print(f'{timestamp()}[{name}]Attempting to close')
    instance.close()
    print(f'{timestamp()}[{name}]Closed')
    return 0


def flock(arg_dict):
    arg_list = [(k,v) for k,v in arg_dict.items()]
    with Pool() as pool:
        pool.starmap(osprey, arg_list)
