# HR-Diagram

- Software for drawing H-R diagram.
- Crawls data from [SDSS DR7 Navigate Tool](http://skyserver.sdss.org/dr7/sp/tools/chart/navi.asp).
- Uses 'g'(green), 'r'(red) filter.
- Based on Python3.


## Instructions
- Fill out the form at `ClusterInfo.ini`.
  - If you change only the threshold, then it will skip crawling data and plot directly.
- Run `main.py`.
> python main.py

## Example

<img src='./img/NGC2420_114.543-114.665-21.526-21.641-0.005.png'>


## TODOs

- Multithreaded crawling
- GUI
