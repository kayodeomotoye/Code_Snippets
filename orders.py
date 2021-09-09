import os
from urllib.request import urlretrieve

import pandas as pd

TMP = os.getenv("TMP", "/tmp")
EXCEL = os.path.join(TMP, "order_data.xlsx")
if not os.path.isfile(EXCEL):
    urlretrieve("https://bites-data.s3.us-east-2.amazonaws.com/order_data.xlsx", EXCEL)


def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
    into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, sheet_name="SalesOrders")


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
    column. You probably need to make an extra column for
    year, return the new df as shown in the Bite description"""
    df["Year"] = pd.DatetimeIndex(df["OrderDate"]).year
    return df.groupby(["Year", "Region"]).sum().Total


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
    the total of his/her sales"""
    sales_dict = (df.groupby("Rep")["Total"].sum()).to_dict()
    best_rep_dict = {
        Rep: total_sales
        for Rep, total_sales in sales_dict.items()
        if total_sales == max(sales_dict.values())
    }
    return list(best_rep_dict.items())[0]


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
    and the number of units sold"""
    unit_dict = (df.groupby("Item")["Units"].sum()).to_dict()
    best_item_dict = {
        item: unit
        for item, unit in unit_dict.items()
        if unit == max(unit_dict.values())
    }
    return list(best_item_dict.items())[0]


if __name__ == "main":
    df = load_excel_into_dataframe(excel=EXCEL)



#pybites

def load_excel_into_dataframe(excel=EXCEL):
    """Load the SalesOrders sheet of the excel book (EXCEL variable)
       into a Pandas DataFrame and return it to the caller"""
    return pd.read_excel(excel, 'SalesOrders')


def get_year_region_breakdown(df):
    """Group the DataFrame by year and region, summing the Total
       column. You probably need to make an extra column for
       year, return the new df as shown in the Bite description"""
    df['Year'] = df['OrderDate'].map(lambda x: x.year)
    return df.groupby(['Year', 'Region']).sum()['Total']


def get_best_sales_rep(df):
    """Return a tuple of the name of the sales rep and
       the total of his/her sales"""
    ret = df.groupby(['Rep']).sum()\
        .sort_values(by=['Total']).iloc[-1]
    return (ret.name, ret.Total)


def get_most_sold_item(df):
    """Return a tuple of the name of the most sold item
       and the number of units sold"""
    ret = df.groupby(['Item']).sum()\
        .sort_values(by=['Units']).iloc[-1]
    return (ret.name, ret.Units)