# coding: utf-8

import os

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False


def sep(title):
    print("\n")
    print(title)
    print("-" * 10)


sep("题目1：Series对象创建")
data = {'工商银行': 601398, '招商银行': 600036}
s = pd.Series(data, name='stock_code')
print(s)


sep("题目2：Series数据访问")
s = pd.Series([20.5, 18.3, 22.1, 19.8], index=['2023-01', '2023-02', '2023-03', '2023-04'])
print("iloc第二个月：", s.iloc[1])
print("loc第三个月：", s.loc['2023-03'])


sep("题目3：DataFrame创建与列操作")
data = [
    ['贵州茅台', 600519, 1800.0],
    ['宁德时代', 300750, 450.5]
]
df = pd.DataFrame(data, columns=['名称', '代码', '价格'], index=['A', 'B'])
df['市值'] = df['价格'] * 1e8
print(df)


sep("题目4：数据筛选")
df = pd.DataFrame({
    '股票名称': ['腾讯控股', '阿里巴巴', '美团', '京东'],
    '收盘价': [320.5, 150.8, 180.2, 280.4],
    '成交量': [1e6, 2e6, 8e5, 1.2e6]
})
result = df[(df['收盘价'] > 200) & (df['成交量'] > 1e6)]
print(result)


sep("题目5：数据统计与排序")
s = pd.Series([3.2, 5.1, 2.8, 4.9, 6.0])
print("均值：", s.mean())
print("方差：", s.var())
print("降序前3：")
print(s.sort_values(ascending=False).head(3))


sep("题目6：数据清洗")
df = pd.DataFrame({
    '日期': ['2023-01', '2023-02', '2023-03'],
    '开盘价': [10.5, None, 12.3],
    '收盘价': [11.0, 9.8, None]
})
df['开盘价'] = df['开盘价'].ffill()
df['收盘价'] = df['收盘价'].fillna(df['收盘价'].mean())
print(df)


sep("题目7：时间序列处理")
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sz000004.csv')
df = pd.read_csv(file)
df['trade_date'] = pd.to_datetime(df['trade_date'].astype(str))
df = df.set_index('trade_date').sort_index()
df_q1 = df['2022-01':'2022-03']
daily_return = df_q1['close'] / df_q1['close'].shift(1) - 1
print("2022年1-3月数据：")
print(df_q1.head())
print("日均收益率：", daily_return.mean())


sep("题目8：数据可视化")
df = pd.read_csv(file)
df['trade_date'] = pd.to_datetime(df['trade_date'].astype(str))
df = df.set_index('trade_date').sort_index()
df_2022 = df['2022':'2022']
plt.figure(figsize=(10, 5))
plt.plot(df_2022.index, df_2022['close'])
plt.title('2022年股票收盘价走势')
plt.xlabel('日期')
plt.ylabel('价格')
plt.grid(True)
plt.show()


sep("题目9：复合条件查询")
df = pd.DataFrame({
    '股票名称': ['平安银行', '中国平安', '万科A', '格力电器'],
    '行业': ['银行', '保险', '房地产', '家电'],
    '市盈率': [8.5, 12.3, 6.7, 15.0]
})
result = df[((df['行业'] == '银行') | (df['行业'] == '保险')) & (df['市盈率'] < 10)]
print(result)


sep("题目10：自定义函数应用")
df = pd.DataFrame({'涨跌幅': [0.05, -0.03, 0.12, -0.08]})


def classify(x):
    if x >= 0.05:
        return '大涨'
    elif x <= -0.05:
        return '大跌'
    else:
        return '震荡'


df['分类'] = df['涨跌幅'].apply(classify)
print(df)
