""" primitive date format inferrer """

from enum import Enum
from datetime import datetime
from collections import Counter


class DateFormat(Enum):
    DDMMYY = 0  # dd/mm/yy
    MMDDYY = 1  # mm/dd/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError


class InfDateFmtError(Exception):
    """custom exception when it is not possible to infer a date format
    e.g. too many NONPARSABLE or a tie """
    pass


def _maybe_DateFormats(date_str):
    """ Args:
    date_str (str) string representing a date in unknown format
    Returns:
    a list of enum members, where each member represents
    a possible date format for the input date_str
    """
    d_parse_formats = DateFormat.get_d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            _parsed_date = datetime.strptime(date_str, d_parse_fmt) # pylint: disable=W0612
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats


def _inf_most_prevalent_DateFormat(dates):
    total_possible_d_formats = []
    for date_str in dates:
        possible_d_formats = _maybe_DateFormats(date_str)
        total_possible_d_formats.extend(possible_d_formats)
    cnt_d_formats = Counter(total_possible_d_formats)

    if len(cnt_d_formats.most_common()) > 1:
        if cnt_d_formats.most_common()[0][1] == cnt_d_formats.most_common()[1][1]:
            # tie
            raise InfDateFmtError("Cannot decide a date format")

    if cnt_d_formats.most_common()[0][0] == DateFormat.NONPARSABLE:
        raise InfDateFmtError("Too many NONPARSABLE dates to infer a date format")

    return cnt_d_formats.most_common()[0][0].value


def get_dates(dates):
    """ Args:
    dates (list) list of date strings
        where each list item represents a date in unknown format
    Returns:
    list of date strings, where each list item represents
    a date in yyyy-mm-dd format. Date format of input date strings is inferred
    based on the most prevalent format in the dates list.
    Allowed/supported date formats are defined in a DateFormat enum class.
    """
    d_format_value = _inf_most_prevalent_DateFormat(dates)
    d_parse_format = DateFormat.get_d_parse_formats(d_format_value)

    out_dates = []
    for date_str in dates:
        try:
            date = datetime.strptime(date_str, d_parse_format)
            date = datetime.strftime(date, "%Y-%m-%d")
            out_dates.append(date)
        except ValueError:
            out_dates.append("Invalid")
    return out_dates