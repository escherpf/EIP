import pandas as pd
import pyfixest as pf

pf.feols(
    'd_EX_T_t  ~ 0 + r + AGE_AVG_t + d_NUM_ADTS_t + d_NUM_KIDS_t | EIPIII_t ~ EIPIII_r',
    data = df_test.reset_index().iloc[:1000],
    weights = 'FINLWT21_AVG',
    ).tidy()
