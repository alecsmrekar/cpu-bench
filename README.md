# Introduction on this CPU Performance Benchmark
It is interesting to see how the CPU advanced throughout the years. This repository is a simple performance benchmark, derived from my workflow that heavily uses Python3 and Numpy. 
Unlike other benchmarks, my benchmark's performance metric **has actual meanings**. The metric is the **runtime (in seconds) of completing some number of tasks concurrently**, and each task is fixed -- repeating $10\times10$ matrix multiplication $10^7$ times.

# How to Run the Benchmark
Stress a CPU by small matrix multiplication. I observe that small matrix multiplication in Numpy only uses a single core, so *# of tasks is equivalent to # of CPU cores*. To start the benchmark, please run the following in the terminal:
```
python stress.py -t 1 2 4 6 8 12 16
```
# How Software Impacts the Performance
- *Operating System*. Linux is apparently faster than Windows (Windows performance is also strange, and varies a lot across different power modes). Microsoft smartly put Linux inside Windows and created Windows Subsystems for Linux (WSL). The WSL 2 is faster than Windows. MacOS performance should be similar to Linux.

- *Python version*. I have tested that Python 3.11 is a little over *10% faster* than 3.8 based on my benchmark. The difference is larger than I expected, since my benchmark's bottleneck is running numpy.dot(), which is implemented in C, and C rarely changes, and I think the matrix multiplication algorithm can barely improve. When newer Python verison come out, I do not rerun the old results because very often the results are run on other people's computers, so it is inconvenient to rerun. 

# Results

![cpu_perf](cpu_perf.png)

**Evaluation**
1. Intel has finally significantly improved in recent years. The 13th gen (purple line) desktop CPU is a lot faster than the 10th gen (orange line).
2. M1 Pro is a laptop CPU (green line), but it beats the high-end desktop Intel CPU (orange line), not to mention the laptop 10th-gen Intel CPU (blue line). 
3. M2 in MacBook Air (red line) is faster than M1 Pro (green line) when the number of tasks is 4 or under, but is slower when the number of tasks is larger than 4. This is because the M1 Pro has 6 performance cores and 2 efficiency cores while the M2 has 4 performance cores and 4 efficiency cores.


**More**: The complete raw data is [here](results). The oldest data point is from a MacBook Pro (Retina, 15-inch, Mid 2012).
