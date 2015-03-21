This is a multithreaded(ish) app for load testing.

This is largely centered around xmlrpc right now as that is my current use case.

Config options:
overload = True|False
max_threshold = (integer)
  The script keeps track of performance and depending on configuratiouration.
  If overload is False once performance decreases it'll revert to the optimal
  thread level.  If overload is True and max_threshold is set to > 0 it will
  go passed peak performance.  Once the max_threshold is reached it'll return
  to normal.  max_threshold should be a small number as it's increase every
  round that has worse performance.  So, depending on how many steps you're
  using with thread counts it should probably be less than 5.  10 at maximum.
  But I don't check it, so have fun.

errors_threshold = (integer)
  This relates to connection errors.  If it goes over the test automatically
  quits and spits out the results so far, and how far you got.  This depends
  on how many threads and clients you want, but for hundreds of threads a
  number in the low 100s would be fine.  But you'll have to test it out and
  see how many errors you're getting.

need_count = (integer)
  This sets a goal to reach in terms of how many times your action is done.
  If you enter in a thread count that doesn't reach your goal, it automatically
  adjusts the final count to acheive your goal.

Future Plans/TODO:
Server/Client architecture
Add kill switch to overload class(don't self-optimize)
Add handling for fixed number of jobs #done
Add random/record/replay features of logs
