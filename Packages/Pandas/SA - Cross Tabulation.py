import pandas as pd

car_names = ['Suzuki','Honda','Toyota','Jeep','Tata']
fuel_type = ['diesel','petrol','diesel','petrol','diesel']
price = [10, 18, 27, 35, 15]

# Passing only required arguments

a = pd.crosstab(index=[car_names], columns=[fuel_type])

# Passing other arguments

b = pd.crosstab(index=[car_names],
            columns=[fuel_type],
            values=price,
            aggfunc=lambda x: x.sum()*2, 
            rownames=["Car Names"], # title of rows
            colnames=['Fuel type'], # title of columns
            dropna=False, #false will display all NaN columns
            margins=True, # Subtotals at the end
            margins_name="Totals") # subtotal's title

print(a)
print('**********************************')
print(b)