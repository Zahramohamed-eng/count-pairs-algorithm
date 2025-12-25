import time
import random
import tkinter as tk
from algorithm1 import count_pairs_naive

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def count_pairs_optimized(arr, L, R):
    merge_sort(arr)
    count = 0
    n = len(arr)

    for i in range(n - 1):
        j = i + 1
        while j < n and arr[i] + arr[j] < L:
            j += 1
        k = j
        while k < n and arr[i] + arr[k] <= R:
            k += 1
        count += k - j

    return count

def main():
    arr = [random.randint(1, 10000) for _ in range(2000)]
    L, R = 5000, 15000

    start = time.perf_counter()
    naive = count_pairs_naive(arr, L, R)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    opt = count_pairs_optimized(arr.copy(), L, R)
    t2 = time.perf_counter() - start

    result.config(
        text=f"Naive Solution\n"
             f"Pairs : {naive}\n"
             f"Time  : {t1:.5f} sec\n\n"
             f"Optimized Solution\n"
             f"Pairs : {opt}\n"
             f"Time  : {t2:.5f} sec"
    )


root = tk.Tk()
root.title("Pair Sum Visualizer")
root.geometry("400x300")
root.configure(bg="#1e1e2f")

tk.Label(
    root,
    text="Pair Sum Counter",
    bg="#1e1e2f",
    fg="#00ffcc",
    font=("Helvetica", 16, "bold")
).pack(pady=10)

tk.Label(
    root,
    text="Array Size: 2000\nSum Range: 5000 – 15000",
    bg="#1e1e2f",
    fg="white",
    font=("Arial", 10)
).pack()

tk.Button(
    root,
    text="Run Algorithm",
    command=main,
    bg="#00ffcc",
    fg="black",
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=20,
    pady=5
).pack(pady=15)

result = tk.Label(
    root,
    text="",
    bg="#2a2a40",
    fg="white",
    font=("Courier New", 10),
    justify="left",
    padx=15,
    pady=10
)
result.pack(pady=10, fill="x", padx=20)

root.mainloop()
