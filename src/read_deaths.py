import pandas as pd


def read_deaths() -> pd.DataFrame:
    df_1962_2020 = _read_deaths_1962_2020()
    return df_1962_2020


def _read_deaths_1962_2020() -> pd.DataFrame:
    df = pd.read_csv("assets/download/deaths_1962_2020.csv", sep=";")

    # France métropolitaine uniquement
    df = df.query("CHAMP == 'FM'").drop(["CHAMP"], axis=1)

    df = df.rename(columns={
        "SEXE": "sex",
        "ANNEE_1962_2020": "year",
        "DECES": "deaths",
        "AGE_ATTEINT_R": "age",
    })

    df = df.query("age != 'DEC'")

    df = df.copy()
    df["age"] = df["age"].map(lambda x: int(x[1:]))
    df["sex"] = df["sex"].map({"H": "M", "F": "F", "E": "E"})

    return df
