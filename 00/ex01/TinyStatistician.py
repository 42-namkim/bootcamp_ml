import numpy as np

#np.array?
class TinyStatistician:
    def __init__(self):
        pass

    def check_data(self, data):
        # should i consider ndarray dimension?
        if isinstance(data, list) or isinstance(data, np.ndarray) :
            if len(data) == 0:
                return False
            return True
        else:
            return False

    def mean(self, data):
        if (self.check_data(data)):
            sum = 0.
            for i in data:
                sum += i
            return sum / len(data)
        else:
            return None

    def median(self, data):
        if not self.check_data(data):
            return None
        sorted_data = sorted(data)
        if len(sorted_data) % 2 == 0:
            return float((sorted_data[len(sorted_data) // 2] + sorted_data[len(sorted_data) // 2 - 1]) / 2)
        else:
            return float(sorted_data[len(sorted_data) // 2])
            
    def quartile(self, data):
        if not self.check_data(data):
            return None 
        sorted_data = sorted(data)
        q1 = self.median(sorted_data[:(len(sorted_data) + 1) // 2])
        q3 = self.median(sorted_data[len(sorted_data) // 2:])
        return [q1, q3]

    def percentile(self, data, percent):
        if not self.check_data(data):
            return None
        sorted_data = sorted(data)
        index = (percent / 100) * (len(sorted_data) - 1)    #
        index_integer = int(index)
        index_decimal = index - index_integer
        if index_decimal == 0:
            return sorted_data[index_integer]
        else:
            return sorted_data[index_integer] * (1 - index_decimal) + sorted_data[index_integer + 1] * index_decimal
        
    def var(self, data):
        if not self.check_data(data):
            return None
        mean = self.mean(data)
        squared_diff_sum = 0.
        for i in data:
            squared_diff_sum += (i - mean) ** 2
        return squared_diff_sum / (len(data) - 1)

    def std(self, data):
        if not self.check_data(data):
            return None
        return self.var(data) ** 0.5