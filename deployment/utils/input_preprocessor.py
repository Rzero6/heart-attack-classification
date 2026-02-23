import pandas as pd

def preprocess_input(df, label_encoders, onehot_encoder, risk_encoder):
    df = df.copy()
    df["Pulse Pressure"] = df["Systolic BP"] - df["Diastolic BP"]
    
    # Label Encoding
    for col, le in label_encoders.items():
        df[col] = le.transform(df[col])


    # One-Hot Encoding
    cat_cols = onehot_encoder.feature_names_in_
    onehot_array = onehot_encoder.transform(df[cat_cols])

    onehot_df = pd.DataFrame(
        onehot_array,
        columns=onehot_encoder.get_feature_names_out(cat_cols),
        index=df.index
    )

    df = df.drop(columns=cat_cols)
    df = pd.concat([df, onehot_df], axis=1)
    
    # Risk / Target Encoding
    enc = risk_encoder["Country"]
    df["Country_risk_encoded"] = (
        df["Country"].map(enc["mapping"])
        .fillna(enc["global_mean"])
    )
    for col, enc in risk_encoder.items():
        df[col] = df[col].map(enc["mapping"]).fillna(enc["global_mean"])

    # Drop columns NOT used in training
    df.drop(
        columns=["Blood Pressure", "Country", "Diastolic BP"],
        inplace=True,
        errors="ignore"
    )
    return df