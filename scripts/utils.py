



# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
# from typing import Callable

# def multiprocess(
#     func,
#     iterables,
#     max_workers=8,
#     chunksize=20,
#     post_func_hook: Callable = None,
#     show_progress_bar: bool = False,
# ):
#     # with progress_bar(total=int(len(iterables) / chunksize),
#     #     show_progress_bar=show_progress_bar) as pbar:
#     with ProcessPoolExecutor(max_workers=max_workers) as executor:
#         # Create trackers
#         # progress_tracker = progress_bar(
#         #     range(math.ceil(len(iterables) / chunksize)),
#         #     show_progress_bar=show_progress_bar,
#         # )
#         # progress_iterator = iter(progress_tracker)

#         # futures = [executor.submit(func, it) for it in chunk(iterables, chunksize)]
#         futures = []
#         results = []
#         for future in as_completed(futures):
#             if post_func_hook:
#                 results.append(post_func_hook(future.result()))
#             else:
#                 results.append(future.result())
#             # if progress_tracker is not None:
#             #     next(progress_iterator)
#             # if show_progress_bar is True:
#             #     progress_tracker.update(1)
#         return results
