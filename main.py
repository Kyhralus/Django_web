'''
Python实验题目1：
# 某研究生从上海某211大学编程相关专业毕业后，在某头部互联网公司找到了一份年收入（税后）
# 30万元的工作。公司承诺每年薪金增长15%，到达60万每年后达到薪金天花板，每年薪金增长5%。
# 该学生刚毕业时在嘉定区看中了一套市价600万元的二手房，该二手房房价每年上涨10%。
# 请问：
# 1.假设该学生的工资全部用来买房，需要多少年才能攒够首付（房价的30%）？
# 2.若买得起房的当年该学生并未买房，10年后他还买得起这套房么？
'''
def salary_calc(year):
    salary = 30
    for i in range(year-1):
        if salary >= 60:
            salary = salary * 0.05 + salary
        else:
            salary = salary * 0.15 + salary
    return salary

def housing_price_calc(year):
    housing_price = 600
    for i in range(year):
        housing_price = housing_price * 0.1 + housing_price
    return housing_price

def deposit_calc(year):
    sum = 0
    for i in range(year):
        sum = sum + salary_calc(i+1)
    return sum
# test
# salary = salary_calc(10)
# housing_price = housing_price_calc(10)
# salary = salary_calc(2)
# housing_price = housing_price_calc(2)
# deposit = deposit_calc(2)
# Promble1
year = 1
deposit = deposit_calc(year)
housing_price = housing_price_calc(year)
salary = salary_calc(year)
while deposit < 0.3 * housing_price:
    deposit = deposit_calc(year)
    housing_price = housing_price_calc(year)
    salary = salary_calc(year)
    print("------- The {} year--------".format(year))
    print("current year's salary: ", salary, "\ncurrent year's housing_price: ", housing_price
          ,"\ncurrent year's posit: ", deposit)
    year = year + 1
year = year - 1
print("The COWDOG has worked ",year , "year(s) to get the house!!!!")

print("========= 10 years later ==========")
deposit = deposit_calc(year + 10)
housing_price = housing_price_calc(year + 10)
salary = salary_calc(year + 10)
print("deposit", deposit, ", housing_price", housing_price, ", salary", salary)
if (deposit >= 0.3 * housing_price):
    print("he/she can also afford the housing price!!!")
else:
    print("he/she can't afford...")