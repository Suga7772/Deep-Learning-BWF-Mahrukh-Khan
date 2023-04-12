import csv

with open('examples/macrodata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["year", "quarter", "realgdp", "realcons", "realinv", "realgovt", "realdpi", "cpi", "ml", "tbilrate", 'unemp', 'pop', 'infl', 'realint']

    writer.writerow(field)
    writer.writerow([1959.0, 1.0, 2710.349, 1707.4, 286.898, 470.045, 1886.9, 28.98, 139.7, 2.82, 5.8, 177.146, 0.00, 0.00])
    writer.writerow([1959.0, 2.0, 2778.801, 1733.7, 310.859, 481.301, 1919.7, 29.15, 139.7, 2.82, 5.8, 177.146, 0.00, 0.00])
    writer.writerow([1959.0, 3.0, 2775.488, 1751.8, 289.226, 491.260, 1916.4, 29.35, 140.5, 3.82, 5.3, 178.657, 2.74, 1.09])
    writer.writerow([1959.0, 4.0, 2785.204, 1753.7, 299.356, 484.052, 1931.3, 29.37, 140.0, 4.33, 5.6, 179.386, 0.27, 4.06])
    writer.writerow([1960.0, 1.0, 2847.699, 1770.5, 331.722, 462.199, 1955.5, 29.54, 139.6, 3.50, 5.2, 180.007, 2.31, 1.19])