import numpy as np
import pandas as pd
import datetime

class MeanDummyRegressor():
    def predict(self, x):
        return np.mean(x)


CHARGE_CHEMISTRY = [{'DATETIME': datetime.datetime(2021, 6, 11, 4, 10),
              'CAO_charge': 10.2,
              'OSN_charge': 2.35,
              'TIO2_charge': 2.5},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 15),
              'CAO_charge': 10.2,
              'OSN_charge': 2.36,
              'TIO2_charge': 2.49},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 0),
              'CAO_charge': 10.1,
              'OSN_charge': 2.35,
              'TIO2_charge': 2.5},
             {'DATETIME': datetime.datetime(2021, 6, 11, 1, 0),
              'CAO_charge': 10.3,
              'OSN_charge': 2.36,
              'TIO2_charge': 2.49}]

LIMESTONE_CONSUMPTIONS = [{'DATETIME': datetime.datetime(2021, 6, 11, 5, 40),
               'limestone_consumption': 16.0646591186523},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 30),
              'limestone_consumption': 15.6317119598389},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 20),
              'limestone_consumption': 15.5927457809448},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 10),
              'limestone_consumption': 15.9572410583496},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 0),
              'limestone_consumption': 15.5615940093994},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 50),
              'limestone_consumption': 15.7822933197022},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 40),
              'limestone_consumption': 15.8518505096436},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 30),
              'limestone_consumption': 16.003246307373},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 20),
              'limestone_consumption': 15.9843339920044},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 10),
              'limestone_consumption': 15.9139966964722},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 0),
              'limestone_consumption': 16.1574821472168},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 50),
              'limestone_consumption': 16.0341854095459},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 40),
              'limestone_consumption': 15.9945793151855},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 30),
              'limestone_consumption': 16.0205516815186},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 20),
              'limestone_consumption': 16.1584014892578},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 10),
              'limestone_consumption': 16.0363502502441},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 0),
              'limestone_consumption': 15.9881801605225},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 50),
              'limestone_consumption': 16.007438659668},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 40),
              'limestone_consumption': 16.007043838501},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 30),
              'limestone_consumption': 15.9648380279541},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 20),
              'limestone_consumption': 15.8637504577637},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 10),
              'limestone_consumption': 15.9902877807617},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 0),
              'limestone_consumption': 15.9160490036011},
             {'DATETIME': datetime.datetime(2021, 6, 11, 1, 50),
              'limestone_consumption': 15.9927406311035}]

CHARGE_CONSUMPTIONS = [{'DATETIME': datetime.datetime(2021, 6, 11, 5, 40),
              'charge_consumption': 557.673095703125},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 30),
              'charge_consumption': 600.348266601562},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 20),
              'charge_consumption': 596.686340332031},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 10),
              'charge_consumption': 595.251220703125},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 0),
              'charge_consumption': 602.357727050781},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 50),
              'charge_consumption': 585.102111816406},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 40),
              'charge_consumption': 584.481323242188},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 30),
              'charge_consumption': 583.308044433594},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 20),
              'charge_consumption': 583.226257324219},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 10),
              'charge_consumption': 587.558288574219},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 0),
              'charge_consumption': 586.076293945313},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 50),
              'charge_consumption': 584.427734375},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 40),
              'charge_consumption': 585.692016601562},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 30),
              'charge_consumption': 583.805786132813},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 20),
              'charge_consumption': 585.79345703125},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 10),
              'charge_consumption': 584.238220214844},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 0),
              'charge_consumption': 587.659545898438},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 50),
              'charge_consumption': 586.328247070312},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 40),
              'charge_consumption': 586.489135742188},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 30),
              'charge_consumption': 585.878479003906},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 20),
              'charge_consumption': 588.330688476563},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 10),
              'charge_consumption': 587.436828613281},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 0),
              'charge_consumption': 588.378356933594},
             {'DATETIME': datetime.datetime(2021, 6, 11, 1, 50),
              'charge_consumption': 586.224609375}]

COKE_CONSUMPTIONS = [{'DATETIME': datetime.datetime(2021, 6, 11, 5, 40),
              'coke_percent': 5.98915672302246},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 30),
              'coke_percent': 6.03918504714966},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 20),
              'coke_percent': 6.08117151260376},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 10),
              'coke_percent': 6.13159513473511},
             {'DATETIME': datetime.datetime(2021, 6, 11, 5, 0),
              'coke_percent': 5.99619960784912},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 50),
              'coke_percent': 6.08766603469849},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 40),
              'coke_percent': 6.08927869796753},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 30),
              'coke_percent': 6.09051752090454},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 20),
              'coke_percent': 6.1020770072937},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 10),
              'coke_percent': 6.06522798538208},
             {'DATETIME': datetime.datetime(2021, 6, 11, 4, 0),
              'coke_percent': 6.10583257675171},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 50),
              'coke_percent': 6.13866329193115},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 40),
              'coke_percent': 6.08378648757935},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 30),
              'coke_percent': 6.07007265090942},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 20),
              'coke_percent': 6.15929889678955},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 10),
              'coke_percent': 6.11061429977417},
             {'DATETIME': datetime.datetime(2021, 6, 11, 3, 0),
              'coke_percent': 6.11808776855469},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 50),
              'coke_percent': 6.07032632827759},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 40),
              'coke_percent': 6.07576704025269},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 30),
              'coke_percent': 6.08071088790894},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 20),
              'coke_percent': 6.05781269073486},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 10),
              'coke_percent': 6.10465621948242},
             {'DATETIME': datetime.datetime(2021, 6, 11, 2, 0),
              'coke_percent': 6.07241725921631},
             {'DATETIME': datetime.datetime(2021, 6, 11, 1, 50),
              'coke_percent': 6.00185203552246}]

COKE_SIEVING = [{'DATETIME': datetime.datetime(2021, 6, 11, 5, 0), 'Sieving3mm_fuel': 17.0},
     {'DATETIME': datetime.datetime(2021, 6, 10, 21, 0), 'Sieving3mm_fuel': 12.4}]

LIMESTONE_CAO = [{'DATETIME': datetime.datetime(2021, 6, 11, 5, 0), 'CAO_limestone': 55.5},
    {'DATETIME': datetime.datetime(2021, 6, 10, 21, 0), 'CAO_limestone': 54.8}]


def predict_cao(charge_chemistry, limestone_consumptions,
        charge_consumptions, coke_consumptions, coke_sieving, limestone_cao):
    charge = pd.DataFrame(charge_chemistry)
    limestone_consumption = pd.DataFrame(
        limestone_consumptions)
    charge_consumptions = pd.DataFrame(
        charge_consumptions)
    concentrate_limestone_consumption = charge_consumptions.copy()
    charge_consumptions.columns = ['DATETIME',
                                      'concentrate_limestone_consumption']
    coke_percent = pd.DataFrame(coke_consumptions)
    Sieving3mm_fuel = pd.DataFrame(
        coke_sieving)
    CAO_limestone = pd.DataFrame(limestone_cao)
    params = {'limestone_consumption': limestone_consumption,
              'charge_consumption': charge_consumptions,
              'concentrate_limestone_consumption': concentrate_limestone_consumption,
              'coke_percent': coke_percent,
              'Sieving3mm_fuel': Sieving3mm_fuel,
              'CAO_limestone': CAO_limestone,
              'charge': charge, }
    for param in params:
        params[param].index = params[param]['DATETIME']
        params[param].sort_index(ascending=False)
        params[param].drop(columns=['DATETIME'], inplace=True)
    frequent_df = params['limestone_consumption']
    frequent_params = ['concentrate_limestone_consumption',
                       'charge_consumption', 'coke_percent']
    for param in frequent_params:
        frequent_df = pd.merge_asof(right=frequent_df.sort_index(),
                                    left=params[param].sort_index(),
                                    left_index=True,
                                    right_index=True,
                                    tolerance=pd.Timedelta('5m'),
                                    direction='nearest'
                                    )
    frequent_df.dropna(inplace=True)
    params_df = pd.DataFrame()
    params_df['Расход кокса'] = (frequent_df['charge_consumption'] *
                                 frequent_df['coke_percent'] * 0.01
                                 ).resample('60T').mean()
    params_df['Расход извести + концентрата'] = (
        frequent_df['concentrate_limestone_consumption'].resample('60T').mean())
    params_df['Расход извести'] = (
        frequent_df[frequent_df.index.minute == 0]['limestone_consumption']
    )
    params_df['Расход концентрата'] = (
        params_df['Расход извести + концентрата'] -
        params_df['Расход извести'])
    params_df['Расход шихты '] = (
        params_df['Расход извести + концентрата']
        - params_df['Расход кокса'])
    params_df['Concentrate'] = (params_df['Расход концентрата'] /
                                params_df['Расход шихты '])
    columns_to_delete = ['Расход кокса', 'Расход извести + концентрата',
                         'Расход извести', 'Расход концентрата',
                         'Расход шихты ']
    params_df.drop(columns=columns_to_delete, inplace=True)
    charge_df = params['charge']
    params_df = pd.merge_asof(
        left=params_df.sort_index(),
        right=charge_df.sort_index(),
        left_index=True,
        right_index=True,
        tolerance=pd.Timedelta('30m'),
        direction='nearest',
    )
    params_df.dropna(inplace=True)
    sieveing_df = params['Sieving3mm_fuel']
    cao_limestone_df = params['CAO_limestone']
    date_time_list = (list(sieveing_df.index) + list(cao_limestone_df.index)
                      + list(params_df.index))
    time_indecies = [x for x in pd.date_range(
        min(date_time_list) - pd.Timedelta('1h'),
        max(date_time_list) + pd.Timedelta('1h'),
        freq='H')
                     ]
    temp_df = pd.DataFrame(data=np.zeros(len(time_indecies)),
                           index=time_indecies
                           )
    temp_df = temp_df.merge(sieveing_df,
                            left_index=True,
                            right_index=True,
                            how='outer'
                            )
    temp_df = temp_df.merge(cao_limestone_df,
                            left_index=True,
                            right_index=True,
                            how='outer'
                            )
    for col in temp_df.columns:
        temp_df[col] = temp_df[col].replace({0: None})
        temp_df[col] = temp_df[col].astype(float).interpolate()
    temp_df = temp_df.drop(columns=[0])
    params_df = pd.merge_asof(
        left=params_df,
        right=temp_df,
        left_index=True,
        right_index=True,
        tolerance=pd.Timedelta('30m'),
        direction='nearest',
    )
    params_df['DATETIME'] = params_df.index
    params_df.reset_index(drop=True, inplace=True)

    params_df = params_df.dropna()
    params_df = params_df.reset_index(drop=True)
    columns_rolling_4 = ['CAO_charge', 'Concentrate',
                         'OSN_charge', 'TIO2_charge',
                         'Sieving3mm_fuel'
                         ]
    columns_rolling_3 = []
    columns_rolling_2 = ['CAO_charge',
                         'CAO_limestone']
    rolls = [columns_rolling_2, columns_rolling_3,
        columns_rolling_4]
    params_df_with_rolling = params_df.copy()
    for number, rol in enumerate(rolls):
        for col in rol:
            try:
                params_df_with_rolling[[col + f"_rolling_{number + 2}"]] = (
                    params_df_with_rolling[[col]].rolling(number + 2).mean()
                )
            except (RuntimeError, TypeError, NameError):
                pass
    params_df_with_rolling = params_df_with_rolling.fillna(10.0)
    params_df_with_rolling = params_df_with_rolling.reset_index(drop=True)
    features = pd.DataFrame()
    features['CAO_charge_rolling_2'] = (
        params_df_with_rolling['CAO_charge_rolling_2']
    )
    features['log(Concentrate_rolling_4)/CAO_charge_rolling_4'] = (
        (np.log(params_df_with_rolling['Concentrate_rolling_4']))
            .divide(params_df_with_rolling['CAO_charge_rolling_4'])
    )
    features['CAO_charge_rolling_2**3*OSN_charge_rolling_4'] = (
        (params_df_with_rolling['CAO_charge_rolling_2'] ** 3)
            .multiply(params_df_with_rolling['OSN_charge_rolling_4'])
    )
    features['CAO_charge/TIO2_charge_rolling_4'] = (
        (params_df_with_rolling['CAO_charge'])
            .divide(params_df_with_rolling['TIO2_charge_rolling_4'])
    )
    features['CAO_charge**3*log(Sieving3mm_fuel_rolling_4)'] = (
        (params_df_with_rolling['CAO_charge'] ** 3)
            .multiply(
            np.log(params_df_with_rolling['Sieving3mm_fuel_rolling_4']))
    )
    features['sqrt(CAO_limestone_rolling_2)*CAO_charge**3'] = (
        (np.sqrt(params_df_with_rolling['CAO_limestone_rolling_2']))
            .multiply((params_df_with_rolling['CAO_charge'] ** 3))
    )
    model = MeanDummyRegressor()
    result = float(model.predict(features.iloc[1]))
    return result

if __name__ == '__main__':
    print(predict_cao(CHARGE_CHEMISTRY, LIMESTONE_CONSUMPTIONS, CHARGE_CONSUMPTIONS,
                COKE_CONSUMPTIONS, COKE_SIEVING, LIMESTONE_CAO))