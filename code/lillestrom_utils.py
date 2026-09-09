import pandas as pd


def get_teotil3_results(
    st_yr, end_yr, regine_list, agri_loss_model, nve_data_yr, stat="accum"
):
    df = pd.read_csv(
        f"/home/jovyan/shared/common/teotil3/teotil3_lillestrom/teotil3_lillestrom_nve{nve_data_yr}_agri-{agri_loss_model}-loss_{st_yr}-{end_yr}.csv"
    )
    df = df.query(
        "(regine in @regine_list) and (year >= @st_yr) and (year <= @end_yr)"
    ).copy()
    df["År"] = df["year"]
    cols = [i for i in df.columns if i.split("_")[0] == stat]
    df = df[["regine", "År"] + cols]
    for col in df.columns:
        if col.endswith("_kg"):
            new_col = col.replace("_kg", "_tonnes")
            df[new_col] = df[col] / 1000
            del df[col]

    return df


def get_aggregation_dict_for_columns(par, agg_dict=None, stat="accum"):
    if agg_dict is None:
        agg_dict = {
            "Jordbruk": [f"{stat}_agriculture_{par}_tonnes"],
            "Avløp": [
                f"{stat}_large-wastewater_{par}_tonnes",
                f"{stat}_spredt_{par}_tonnes",
                f"{stat}_overflow_{par}_tonnes",
            ],
            "Industri": [f"{stat}_industry_{par}_tonnes"],
            "Bebygd": [f"{stat}_urban_{par}_tonnes"],
            "Bakgrunn": [
                f"{stat}_agriculture-background_{par}_tonnes",
                f"{stat}_upland_{par}_tonnes",
                f"{stat}_wood_{par}_tonnes",
            ],
        }
    if par in ("totn", "din"):
        agg_dict["Bakgrunn"].append(f"{stat}_lake_{par}_tonnes")

    if par != "ss":
        agg_dict["Akvakultur"] = [f"{stat}_aquaculture_{par}_tonnes"]

    return agg_dict


def aggregate_parameters(df, par, agg_dict=None, stat="accum"):
    df = df.copy()
    agg_dict = get_aggregation_dict_for_columns(par, agg_dict=agg_dict, stat=stat)
    for group, cols in agg_dict.items():
        df[group] = df[cols].sum(axis=1)

    df = df[["regine", "År"] + list(agg_dict.keys())]

    return df