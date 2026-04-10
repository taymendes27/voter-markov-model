def assign_state(df):
    def get_state(row):
        if row["VOTED"] == 0:
            return "U"
        elif row["REGSTAT"] == 1:
            return "R"
        elif row["VOTED"] == 1:
            return "A"
        else:
            return "D"

    df["state"] = df.apply(get_state, axis=1)
    return df
