
import numpy as np
import pandas as pd

# 1️⃣ 设定基本参数
initial_FCF = 18e9  # 2023年NVIDIA的自由现金流 (18B)
growth_rate_first_5_years = 0.15  # 前5年增长15%
growth_rate_next_5_years = 0.05  # 后5年增长5%
discount_rate = 0.10  # 贴现率 (WACC 10%)
terminal_growth_rate = 0.05  # 终值增长率 5%
years = 10  # 预测年数
shares_outstanding = 2.5e9  # 总股本 (25亿股)

# 2️⃣ 计算未来10年的自由现金流 (FCF)
fcf_values = []
fcf = initial_FCF

for year in range(1, years + 1):
    if year <= 5:
        fcf *= (1 + growth_rate_first_5_years)
    else:
        fcf *= (1 + growth_rate_next_5_years)
    fcf_values.append(fcf)

# 3️⃣ 计算终值 (Terminal Value) - Gordon Growth Model
terminal_value = fcf_values[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)

# 4️⃣ 计算折现现金流 (Discounted Cash Flow)
discounted_fcf = [fcf / ((1 + discount_rate) ** (year)) for year, fcf in enumerate(fcf_values, start=1)]
discounted_terminal_value = terminal_value / ((1 + discount_rate) ** years)

# 5️⃣ 计算企业价值 (Enterprise Value)
enterprise_value = sum(discounted_fcf) + discounted_terminal_value

# 6️⃣ 计算每股合理价值 (Fair Value per Share)
fair_value_per_share = enterprise_value / shares_outstanding

# 7️⃣ 组织数据并输出结果
data = {
    "Year": list(range(1, years + 1)),
    "FCF ($B)": [round(fcf / 1e9, 2) for fcf in fcf_values],
    "Discounted FCF ($B)": [round(d_fcf / 1e9, 2) for d_fcf in discounted_fcf],
}

df = pd.DataFrame(data)

# 打印DCF计算结果
print(f"📊 未来10年DCF计算结果:\n{df}")
print(f"\n💰 计算出的每股合理价值: ${fair_value_per_share:.2f}")

