import math
class Statcalc:
    def __init__(self, data):
        self.data = data
        
    # Mean
    def mean(self, data):
        mean = 0
        for x in data:
            mean += x
        mean = mean/len(data)
        
        return mean
    
    # Median
    def median(self, data):
        data.sort()
        n = len(data)

        if n % 2 == 0:
            mid = int(n/2)
            med_vals = data[mid-1] + data[mid]
            median = med_vals/2
        else:
            mid = (n + 1)/2
            median = data[mid]

        return median

    # STD
    def popn_std(self, data):
        dif = []
        for x in data:
            dif.append(((x-Statcalc.mean(data))**2))

        asum = 0
        for x in dif:
            asum += x

        popn_std = asum/(len(data))
        popn_std = math.sqrt(popn_std)

        return popn_std
    
    def sample_std(self, data):
        dif = []
        for x in data:
            dif.append(((x-Statcalc.mean(data))**2))
        

        asum = 0
        for x in dif:
            asum += x

        sample_std = asum/(len(data)-1)
        sample_std = math.sqrt(sample_std)

        return sample_std
    
    # Z-score
    def popn_z(self, data):
        zs = []

        for x in data:
            z = (x-Statcalc.mean(data))/Statcalc.popn_std(data)
            zs.append(z)

        return zs
    
    def sample_z(self, data):
        zs = []

        for x in data:
            z = (x-Statcalc.mean())/Statcalc.sample_std(data)
            zs.append(z)
        
        return zs

    # Z-score
    def z(self, data, mean, std):        
        z = (data - mean)/std
        return z

    # IQR
    def iqr(self, data):
        data.sort()
        
        n = len(data)
        half = n//2

        if n % 2 == 0:
            lower_half = data[:half]
            upper_half = data[half:]
        else:
            lower_half = data[:half]
            upper_half = data[half+1:]
        
        global q1
        global q3

        q1 = Statcalc.median(lower_half)
        q3 = Statcalc.median(upper_half)

        iqr = q3 - q1
        return iqr
    # Outlier
    def outlier(self, data):
        outliers = []
        low_outlier = (q1 - 1.5*(Statcalc.iqr(data)))
        high_outlier = (q3 + 1.5*(Statcalc.iqr(data)))

        for x in data() < low_outlier or x > high_outlier:
            outliers.append(x)
        return outliers

    # Probability
    def prob(self, condition, sample):
        event = 0

        for x in condition:
            if x in sample:
                event += 1

        prob = event/len(sample)
        return prob
    
    # Regression line
    def regress(self, data):
        X = list(self.data.keys())
        Y = list(self.data.values())

        x_mean = Statcalc.mean(X)
        y_mean = Statcalc.mean(Y)
        
        m = Statcalc.r()*((Statcalc.sample_std(Y))/((Statcalc.sample_std(X))))
        b = y_mean - m*x_mean
        return m, b

    # Sample Variance
    def sample_var(self, data):
        dif = []
        for x in data:
            dif.append(((x-Statcalc.mean(data))**2))
        
        asum = 0
        for x in dif:
            asum += x

        var = asum/(len(data)-1)
        return var
    
    # Popn_Variance
    def popn_var(self, data):
        dif = []
        for x in data:
            dif.append(((x-Statcalc.mean(data))**2))
        
        asum = 0
        for x in dif:
            asum += x

        var = asum/(len(data))
        return var

    # correlation
    def r(self):
        X = list(self.keys())
        Y = list(self.values())
        sum_xy = 0

        for x, y in X, Y:
            xy = (x-Statcalc(X))(y-Statcalc(Y))
            sum_xy += xy
            std_x = Statcalc.sample_std(X)
            std_y = Statcalc.sample_std(Y)
            std_xy = std_x *std_y
            n = len(X)-1

            r = (1/(n*std_xy)) *(sum_xy)
            return r

    # Coefficient of Variation
    def coef_va(self, data):
        coef = Statcalc.sample_std(data)/Statcalc.mean(data) * 100

        return coef

data = {
    1: 2,
    2: 4,
    3: 6,
    4: 8,
    5: 10
}