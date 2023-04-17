import pandas as pd
import ydata_profiling as pp
import fredapi
import configparser
import matplotlib as plt


def download_housing_data(api):
    # Define the housing data series you want to download
    housing_series = {
        'CASESHILLER': 'SPCS20RSA',
        'HOUST': 'HOUST',
        'MSPUS': 'MSPUS'
    }

    # Download the data using the FRED API
    housing_data = pd.DataFrame()

    for series_id in housing_series.values():
        data = api.get_series(series_id)
        housing_data[series_id] = data

    # Rename the columns to something more descriptive
    housing_data.columns = list(housing_series.keys())
    print(housing_data.columns)

    # Save the data to a CSV file
    csv_file = f'{proj_path}/housing_data.csv'
    housing_data.to_csv(csv_file, index=False)
    print(f"CSV File : {csv_file}")


def plot_data():
    # Load the data from the CSV file
    housing_data = pd.read_csv('venv/data/housing_data.csv')

    # Print some summary statistics
    print(housing_data.describe())

    # Plot the data
    fig, axs = plt.subplots(3, figsize=(10, 15))

    axs[0].plot(housing_data['CASESHILLER'])
    axs[0].set_title('S&P/Case-Shiller U.S. National Home Price Index')

    axs[1].plot(housing_data['HOUST'])
    axs[1].set_title('Housing Starts: Total: New Privately Owned Houses Started')

    axs[2].plot(housing_data['MSPUS'])
    axs[2].set_title('Median Sales Price of Houses Sold for the United States')

    plt.show()


def data_profiler():
    # Load the data from the CSV file
    housing_data = pd.read_csv(f'{proj_path}/housing_data.csv')

    # Generate a report using pandas_profiling
    housing_data_profile = pp.ProfileReport(housing_data)
    housing_data_profile.to_file('housing_data_report.html')
    print("Profiling Report: housing_data_report.html")


config = configparser.ConfigParser()
config.read('util/config.ini')

api_key = config.get('API', 'key')
fred = fredapi.Fred(api_key=api_key)
proj_path = config.get('PATH', 'data_path')

download_housing_data(fred)
# plot_data()
data_profiler()
