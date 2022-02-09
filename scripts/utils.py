"""Multithreading Module
"""
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from typing import Callable
def chunk(iterables, n=20):
    return [iterables[i : i + n] for i in range(0, int(len(iterables)), int(n))]


def multithread(
    func, iterables, max_workers=8, chunksize=20, show_progress_bar: bool = False
):
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, it) for it in chunk(iterables, chunksize)]
        results = []
        for future in as_completed(futures):
            results.append(future.result())
        return results


def multiprocess(
    func,
    iterables,
    static_args,
    max_workers=8,
    chunksize=20,
    post_func_hook: Callable = None,
):
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, it, static_args) for it in chunk(iterables, chunksize)]
        results = []
        for future in as_completed(futures):
            if post_func_hook:
                results.append(post_func_hook(future.result()))
            else:
                results.append(future.result())
        return results
