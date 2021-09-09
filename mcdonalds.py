import pandas as pd

data = "https://s3.us-east-2.amazonaws.com/bites-data/menu.csv"
# load the data in once, functions will use this module object
df = pd.read_csv(data)

pd.options.mode.chained_assignment = None  # ignore warnings


def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    result = df.groupby("Calories").max()
    return result.tail(1).values[0][1]


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
    5 foods with the best ratio.

    This function has a excl_drinks switch which, when turned on,
    should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

    You will probably need to filter out foods with 0 calories to get the
    right results.

    Return a list of the top 5 foot Item stings."""
    if excl_drinks:
        df = df[(df.Category != "Coffee & Tea") & (df.Category != "Beverages")]
    df_filtered = df[df["Calories"] != 0]
    df_filtered["Percent"] = df_filtered.Protein / df.Calories
    result = df_filtered.nlargest(5, "Percent")
    return [food[1] for food in result.values]


#pybites

def get_food_most_calories(df=df):
    """Return the food "Item" string with most calories"""
    return df.iloc[df['Calories'].idxmax()]['Item']


def get_bodybuilder_friendly_foods(df=df, excl_drinks=False):
    """Calulate the Protein/Calories ratio of foods and return the
       5 foods with the best ratio.

       This function has a excl_drinks switch which, when turned on,
       should exclude 'Coffee & Tea' and 'Beverages' from this top 5.

       You will probably need to filter out foods with 0 calories to get the
       right results.

       Return a list of the top 5 foot Item stings."""
    df = df[df['Calories'] > 0]
    df['prot_per_calorie'] = df['Protein'] / df['Calories']

    if excl_drinks:
        df = df[~df['Category'].isin(['Coffee & Tea', 'Beverages'])]

    return df.sort_values(by="prot_per_calorie",
                          ascending=False).head(5)['Item'].values
