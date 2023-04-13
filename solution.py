import pandas as pd
import numpy as np
import math
from scipy.stats import t

chat_id = 628156322 # Ваш chat ID, не меняйте название переменной

def solution(control_NPV, test_NPV)-> bool:
    alpha=0.09
    n1 = len(control_NPV)
    n2 = len(test_NPV)
    mean1 = sum(control_NPV) / n1
    mean2 = sum(test_NPV) / n2
    var1 = sum((x - mean1)**2 for x in control_NPV) / (n1 - 1)
    var2 = sum((x - mean2)**2 for x in test_NPV) / (n2 - 1)
    s = math.sqrt((var1 + var2) / (n1 + n2 - 2))
    t_stat = (mean1 - mean2) / (s * math.sqrt(1/n1 + 1/n2))
    crit_val = t.ppf(1-alpha/2, n1+n2-2)
    if abs(t_stat) > crit_val:
        return True
    else:
        return False
