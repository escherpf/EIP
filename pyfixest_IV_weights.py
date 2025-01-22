import pandas as pd
import pyfixest as pf

df_test = pd.read_csv('df_test.csv')

pf.feols(
    'd_EX_T_t  ~ 0 + r + AGE_AVG_t + d_NUM_ADTS_t + d_NUM_KIDS_t | EIPIII_t ~ EIPIII_r',
    data = df_test,
    weights = 'FINLWT21_AVG',
    ).tidy()
