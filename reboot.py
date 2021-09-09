from datetime import datetime, date, timedelta
import re


THIS_YEAR = date.today().year

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """

    extract_dt = re.sub(r"reboot(\W+)", "", reboots).strip("\n").split("\n")
    convt_dt = [datetime.strptime(date, "%a %b %d %H:%M") for date in extract_dt]
    ret_list = []
    for idx in range(0, len(convt_dt)):
        if convt_dt[idx] == convt_dt[-1]:
            continue
        else:
            ret_list.append(
                (
                    (convt_dt[idx] - convt_dt[idx + 1]).days,
                    datetime.strftime(
                        convt_dt[idx].replace(year=THIS_YEAR), "%Y-%m-%d"
                    ),
                )
            )
    return max(ret_list)




#pybites
from dateutil.parser import parse

def calc_max_uptime(reboots):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    tstamps = [parse(line.split('~')[1].strip())
               for line in
               reversed(reboots.strip().splitlines())]

    diffs = {}
    for i, j in zip(tstamps, tstamps[1:]):
        diffs[j - i] = j
        max_uptime = max(diffs)

    return max_uptime.days, str(diffs[max_uptime].date())