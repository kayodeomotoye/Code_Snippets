from collections import namedtuple

import pandas as pd

DATA_FILE = "https://bites-data.s3.us-east-2.amazonaws.com/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def load_data():
    """Load the data file and create the DataFrames"""
    df = pd.read_csv(DATA_FILE, parse_dates=["Date"])
    df["Date"] = pd.DatetimeIndex(df["Date"]).date

    # rename column Data_Value to Value
    df.rename(columns={"Data_Value": "Value"}, inplace=True)

    # divide temperature entries by 10 to convert to Celsius
    df.loc[:, "Value"] /= 10

    # index by Month & Day and sort
    df["Day"] = pd.DatetimeIndex(df["Date"]).day
    df["Month"] = pd.DatetimeIndex(df["Date"]).month
    df.set_index(["Month", "Day"], inplace=True)
    df.sort_index(inplace=True)

    # Remove 29th of Feb to leave only 365 days
    df.drop([(2, 29)], inplace=True)

    # separate the data between 2005-2014 and 2015
    df["Year"] = pd.DatetimeIndex(df["Date"]).year
    df_2015 = df[df["Year"] == 2015]
    df = df[df["Year"] != 2015]

    return df, df_2015


def extremes_values(dataframe, with_date=False):
    """Extracts extreme temperature values"""
    high_temp_df = dataframe[dataframe["Element"] == "TMAX"]
    low_temp_df = dataframe[dataframe["Element"] == "TMIN"]

    # generate a series or a dataframe
    if with_date:
        high_temp = high_temp_df.loc[
            high_temp_df.groupby(["Month", "Day"])["Value"].idxmax()
        ]
        low_temp = low_temp_df.loc[
            low_temp_df.groupby(["Month", "Day"])["Value"].idxmin()
        ]
    else:
        high_temp = high_temp_df.groupby(["Month", "Day"])["Value"].max()
        low_temp = low_temp_df.groupby(["Month", "Day"])["Value"].min()

    return high_temp, low_temp


def temp_df_gen(dataframe, dataframe_2015, mode="high"):
    """Generates the high/low record breakers DataFrame"""
    temps = []
    for idx, rows in dataframe_2015.iterrows():
        if mode == "high":
            if rows["Value"] > dataframe.loc[idx]:
                temps.append((rows["Date"], rows["Value"], rows["ID"]))
        else:
            if rows["Value"] < dataframe.loc[idx]:
                temps.append((rows["Date"], rows["Value"], rows["ID"]))

    # convert temps list into a DataFrame
    temp_df = pd.DataFrame(temps, columns=["Date", "Value", "ID"])
    temp_df.set_index("Date", inplace=True)

    return temp_df


def namedtuple_gen(dataframe, func):
    """Generate namedtuple from DataFrame"""
    if func == "max":
        tmp_df = dataframe.where(
            dataframe["Value"] == dataframe["Value"].max()
        ).dropna()
    else:
        tmp_df = dataframe.where(
            dataframe["Value"] == dataframe["Value"].min()
        ).dropna()

    tmp_df.reset_index(inplace=True)
    record_breaker = STATION(
        tmp_df["ID"].values[0], tmp_df["Date"].values[0], tmp_df["Value"].values[0]
    )

    return record_breaker


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a
    datetime.date() object. The temperatures in the dataset are in tenths
    of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.

    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day / station pair between 2005-2015
       * Extract lowest temperatures for each  day / station  between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days

    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015

    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID,
         Date, Value
         
    5. From the record breakers in 2015, extract the high/low of all the
       temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    data, data_2015 = load_data()
    max_temp, min_temp = extremes_values(data)
    max_temp_2015, min_temp_2015 = extremes_values(data_2015, with_date=True)
    high_df = temp_df_gen(max_temp, max_temp_2015, "high")
    low_df = temp_df_gen(min_temp, min_temp_2015, "low")
    record_high_2015 = namedtuple_gen(high_df, "max")
    record_low_2015 = namedtuple_gen(low_df, "min")

    return record_high_2015, record_low_2015