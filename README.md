# HR-Diagram

- Software for drawing H-R diagram.
- Crawls data from [SDSS DR7 Navigate Tool](http://skyserver.sdss.org/dr7/sp/tools/chart/navi.asp).
- Uses 'g'(green), 'r'(red) filter.
- Based on Python3.


## Instructions
- Type the name and area of cluster at `main.py`.
- Type the threshold to exclude background stars.
  - If you change only the threshold, then it will skip crawling data and plot directly.
```
ra_0 = 114.543
dec_0 = 21.641
ra_1 = 114.665
dec_1 = 21.526
interval = 0.02
clustername = 'NGC2420'
threshold = 18
```
- Run `main.py`.
> python main.py

## Example

<img src='./img/NGC2420_114.543-114.665-21.526-21.641-0.005.png'>


## TODOs

- Multithreaded crawling
- GUI
