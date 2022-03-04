import pandas as pd


def read_pop():
    return read_pop_1901_2020()


def read_pop_1901_2020():
    df = pd.read_excel("assets/download/age_pyramid_1901_2020.xls",
                       sheet_name="France métropolitaine",
                       skiprows=[*range(8)] + [9])

    df.columns.values[0] = "sex"
    df.columns.values[1] = "age"

    # Remove blank and "total" rows
    df = df.drop(index=[106, 107, 108, 215, 216, 217, 218], axis=1)

    # Put sex on every row
    df.loc[:105, "sex"] = "M"
    df.loc[106:, "sex"] = "F"

    df["age"] = df["age"].replace(" 105 ou +", "105").astype(int)

    # Flatten the matrix
    df = df.melt(id_vars=["sex", "age"], var_name="year", value_name="pop")

    df["year"] = df["year"].astype(int)
    df[(df["sex"] == "F") & (df["year"] == 2020)]
    df["pop"] = df["pop"].replace("-", 0).astype(int)
    return df
