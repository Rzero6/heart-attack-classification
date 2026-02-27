import pandas as pd

def preprocess_input(df, label_encoders, onehot_encoder, risk_encoder):
    df = df.copy()
    
    # Label Encoding
    for col, le in label_encoders.items():
        if col == 'Hemisphere':
            continue
        df[col] = le.transform(df[col])


    # One-Hot Encoding
    for col in onehot_encoder.feature_names_in_:
        if col not in df.columns:
            df[col] = "NaN" 

    # Transform seperti biasa
    onehot_array = onehot_encoder.transform(df[onehot_encoder.feature_names_in_])
    onehot_df = pd.DataFrame(
        onehot_array,
        columns=onehot_encoder.get_feature_names_out(onehot_encoder.feature_names_in_),
        index=df.index
    )

    df = df.drop(columns=onehot_encoder.feature_names_in_)
    df = pd.concat([df, onehot_df], axis=1)
    
#    Risk / Target Encoding
    df["Country"] = df["Country"].fillna("Unknown")

    df["Country_risk_encoded"] = (
        df["Country"].map(risk_encoder["mapping"])  # mapping per country
        .fillna(risk_encoder["global_mean"])       # fallback global mean
    )
    
    # Drop kolom yang tidak dipakai
    df.drop(columns=["Blood Pressure", "Country"], inplace=True, errors="ignore")
    df.drop(columns=[col for col in df.columns if col.startswith("Continent")], inplace=True, errors="ignore")

    return df