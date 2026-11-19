# coding: utf-8

from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_DOWN


def sep(title):
    print("\n")
    print(title)
    print("-" * 10)


sep("题目1：字符串处理与股票代码清洗")
codes = ["SH.600519", "SZ.000001", "SH.600188"]
result1 = [c.replace("SH.", "沪市：").replace("SZ.", "深市：") for c in codes]
print("replace 方法：", result1)

result2 = []
for c in codes:
    prefix, num = c.split(".")
    market = "沪市" if prefix == "SH" else "深市"
    result2.append(f"{market}：{num}")
print("split 方法：  ", result2)


sep("题目2：列表操作与收益率计算")
prices = [100.0, 105.5, 110.2, 108.0, 112.3]
returns = [
    (prices[i] - prices[i - 1]) / prices[i - 1]
    for i in range(1, len(prices))
]
rounded = list(map(lambda x: round(x, 2), returns))
print("原始收益率：", returns)
print("round 结果：", rounded)

rounded_sample = [
    float(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_DOWN))
    for x in returns
]
print("匹配题目示例：", rounded_sample)


sep("题目3：条件判断与交易信号生成")
current_price = 9.8
buy_price = 10.0
if current_price >= buy_price * 1.1:
    print("止盈")
elif current_price <= buy_price * 0.9:
    print("止损")
else:
    print("继续持有")


sep("题目4：函数与投资组合收益计算")
def calculate_portfolio_return(returns, weights):
    if len(returns) != len(weights):
        raise ValueError("returns与weights长度要一致")
    if not weights:
        raise ValueError("weights不可为空")
    total_weight = sum(weights)
    return sum(r * w for r, w in zip(returns, weights)) / total_weight


print(calculate_portfolio_return([0.1, 0.2], [0.6, 0.4]))


sep("题目5：列表的增删与统计")
codes = ['SH.600000', 'SZ.000001', 'SH.600188']
codes.append("SZ.000007")
codes.insert(1, "SZ.000001")
codes.remove("SH.600188")
count = codes.count("SZ.000001")
print("操作后列表：", codes)
print("SZ.000001 出现次数：", count)


sep("题目6：日期处理与交易时间分析")
days = (date.today() - date(2023, 1, 1)).days
print("自然日天数：", days)

t = datetime.strptime("2023-05-10 14:30:00", "%Y-%m-%d %H:%M:%S")
formatted = f"{t.year}年{t.month}月{t.day}日 {t.hour}时{t.minute}分{t.second:02d}秒"
print("格式化交易时间：", formatted)


sep("题目7：循环控制（for 与 while）")
stocks = ["贵州茅台", "工商银行", "中国平安", "招商银行", "工商银行"]

for_result = []
for name in stocks:
    if name == "工商银行":
        continue
    for_result.append(name)
print("for 结果：", for_result)

while_result = []
i = 0
while i < len(stocks):
    name = stocks[i]
    i += 1
    if name == "工商银行":
        continue
    while_result.append(name)
print("while 结果：", while_result)
if for_result == while_result:
    print("结果一致：")


sep("题目8：多态与股票信息输出")
class FinancialInstrument:
    def display_info(self):
        raise NotImplementedError("子类必须实现 display_info 方法")


class Stock(FinancialInstrument):
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def display_info(self):
        print(f"股票代码：{self.code}，名称：{self.name}")


class Bond(FinancialInstrument):
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def display_info(self):
        print(f"债券代码：{self.code}，名称：{self.name}")


Stock("600519", "贵州茅台").display_info()
Bond("010107", "国债010107").display_info()


sep("题目9：面向对象与 property 属性")
# 复用stock类
class Stock:
    def __init__(self, price, volume):
        self._price = price
        self._volume = volume

    @property
    def cost_value(self):
        return self._price * self._volume

    @cost_value.setter
    def cost_value(self, values):
        self._price, self._volume = values

    @cost_value.deleter
    def cost_value(self):
        del self._price
        del self._volume


s = Stock(10.0, 100)
print("初始总金额：", s.cost_value)

s.cost_value = (12.0, 200)
print("修改后总金额：", s.cost_value)

del s.cost_value
print("删除后是否还有 _price：", hasattr(s, "_price"))

try:
    print(s.cost_value)
except AttributeError as e:
    print("访问已删除属性时：", e)
