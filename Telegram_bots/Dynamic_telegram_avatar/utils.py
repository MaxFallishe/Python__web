from fstring import fstring
import sys
from datetime import datetime


# Oh man, this is actually temptingly nice:
def f(string):
  frame = sys._getframe(1)
  return string.format(**frame.f_locals)


def convert_time_to_string(dt):
    return f("{dt.hour}:{dt.minute:02}")


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != prev_time
