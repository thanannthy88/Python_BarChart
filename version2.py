# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:28:20 2023

@author: User88
"""
# -*- coding: utf-8 -*-


import matplotlib
matplotlib.use("TkAgg")
from barchart import BarChart
import time

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return value

def plot_chart(chart, data_group, caption, bar_count):
    chart.reset()
    for data_point in data_group[:bar_count]:
        chart.add(data_point[1], data_point[3], data_point[4])
    chart.set_caption(caption)
    chart.draw()

def read_chart_data(file_path):
    data = []
    with open(file_path, "r") as file:
        title = file.readline().strip()
        x_axis_label = file.readline().strip()
        source = file.readline().strip()
        for line in file:
            values = line.strip().split(',')
            if len(values) > 3:
                converted_values = [convert_to_int(value) for value in values]
                data.append(converted_values)
    return title, x_axis_label, source, data

def sort_chart_data(chart_data):
    return sorted(chart_data, key=lambda x: (x[0], -int(x[3])))

def get_year_limits(sorted_data):
    min_year = int(sorted_data[0][0].split('-')[0])
    max_year = int(sorted_data[-1][0].split('-')[0])
    return min_year, max_year

def main():
    input_file = 'babyname.txt'
    title, x_axis_label, source, chart_data = read_chart_data(input_file)
    sorted_chart_data = sort_chart_data(chart_data)
    min_year, max_year = get_year_limits(sorted_chart_data)
    
    chart = BarChart(title, x_axis_label, source)
    
    for year in range(min_year, max_year + 1):
        data_group = [line for line in sorted_chart_data if str(year) in line[0]]
        plot_chart(chart, data_group, str(year), 6)
        time.sleep(0.001)
    
    chart.leave_window_open()

if __name__ == "__main__":
    main()

