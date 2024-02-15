import pandas as pd


def clean(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df_merge = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df_merge.drop('id', axis=1, inplace=True)
    df_merge.dropna(inplace=True)
    df_merge = df_merge[~df_merge['job'].str.contains('insurance', case=False)]
    df_merge.to_csv(output, index=False)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='First input data file (CSV)')
    parser.add_argument('input2', help='Second input data file (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    clean(args.input1, args.input2, args.output)