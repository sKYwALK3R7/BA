import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime

time_absolutes = [0.0]
time_deltas = []
timestamps = []

def extract_data():
    file_path = "measurement_data_edited.tsv"
    data = pd.read_csv(file_path, sep="\t")
    # print(data)

    for entry in data["TimeStamp"]:
        clean_teimstamp = entry.split()[0]
        timestamp_1 = datetime.datetime.strptime(clean_teimstamp, "%Y-%m-%d_%H-%M-%S.%f")
        timestamps.append(timestamp_1)
    for i in range(0, len(timestamps) - 1):
        time_deltas.append((timestamps[i+1] - timestamps[i]).total_seconds())

    for j in range(0, len(time_deltas)):
        time_absolutes.append(round((time_absolutes[j] + time_deltas[j]), 3))
    
    # for k in time_absolutes:
    #     print(k)
    
    # print(time_absolutes)
    return data



if __name__ == "__main__":
    data_get = extract_data()

    fig, ax = plt.subplots()
    ax.plot(time_absolutes, data_get["Impedance_Z"])
    ax.set_xlabel("Zeit [s]")
    ax.set_ylabel("Impedanz [Ohm]")
    ax.set_title("Impedanz über Zeit")
    ax.grid(True)
    plt.show()
    fig.savefig("Plots/impedance_over_time.pdf")

    fig, ax = plt.subplots()
    ax.plot(time_absolutes, data_get["Resistance_Rp"])
    ax.set_xlabel("Zeit [s]")
    ax.set_ylabel("Wiederstand R_p [Ohm]")
    ax.set_title("Wiederstand R_p über Zeit")
    ax.grid(True)
    plt.show()

    fig, ax = plt.subplots()
    print(data_get.dtypes)
    ax.plot(time_absolutes, data_get["Capacity_Cp[pF]"])
    ax.set_xlabel("Zeit [s]")
    ax.set_ylabel("Kapazität [pF]")
    ax.set_title("Kapazität über Zeit")
    ax.grid(True)    
    plt.show()
    fig.savefig("Plots/capacity_over_time.pdf")

    fig, ax = plt.subplots()
    ax.plot(time_absolutes, data_get["Phase"])
    ax.set_xlabel("Zeit [s]")
    ax.set_ylabel("Phase [°]")
    ax.set_title("Phase über Zeit")
    ax.grid(True)
    plt.show()
    fig.savefig("Plots/phase_over_time.pdf")

    fig, ax = plt.subplots()
    ax.plot(time_absolutes, data_get["Force"])
    ax.set_xlabel("Zeit [s]")
    ax.set_ylabel("Kraft [N]")
    ax.set_title("Kraft über Zeit")
    ax.grid(True)
    plt.show()
    fig.savefig("Plots/force_over_time.pdf")

    fig, ax = plt.subplots()
    ax.plot(data_get["Force"], data_get["Capacity_Cp[pF]"])
    ax.set_xlabel("Kraft [N]")
    ax.set_ylabel("Kapazität [pF]")
    ax.set_title("Kapazität über Kraft")
    ax.grid(True)
    plt.show()
    fig.savefig("Plots/capacity_over_force.pdf")

    fig, ax = plt.subplots()
    ax.plot(data_get["Force"], data_get["Impedance_Z"])
    ax.set_xlabel("Kraft [N]")
    ax.set_ylabel("Impedanz [Ohm]")
    ax.set_title("Impedanz über Kraft")
    ax.grid(True)
    plt.show()
    fig.savefig("Plots/impedance_over_force.pdf")