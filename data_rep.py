import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime

time_absolutes = [0.0]
time_deltas = []
timestamps = []

plt.rcParams.update({
    'font.size': 14,  # Allgemeine Schriftgröße
    'axes.labelsize': 16,  # Achsenbeschriftung
    'axes.titlesize': 18,  # Titelgröße
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 14,
    'figure.figsize': (8, 6),
    'lines.linewidth': 2,
})

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

    def plot_graph(x, y, xlabel, ylabel, title, filename, use_log=False):
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', markersize=4, linestyle='-', alpha=0.8)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid(True, linestyle='--', linewidth=0.5)
        
        # Set logarithmische Skala, falls notwendig
        if use_log:
            ax.set_yscale('log')
        
        # Tausender-Trennzeichen
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.2f}'))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:.1e}'))
        
        plt.tight_layout()
        plt.savefig(f"Plots/{filename}", dpi=600, bbox_inches='tight')
        plt.show()
    
    
    def plot_graph_theta(x, y, xlabel, ylabel, title, filename, use_log=False):
        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o', markersize=4, linestyle='-', alpha=0.8)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title)
        ax.grid(True, linestyle='--', linewidth=0.5)
        
        # Set logarithmische Skala, falls notwendig
        if use_log:
            ax.set_yscale('log')
        
        # Tausender-Trennzeichen
        ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.2f}'))
        ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x:,.2f}'))
        
        plt.tight_layout()
        plt.savefig(f"Plots/{filename}", dpi=600, bbox_inches='tight')
        plt.show()


    # Plots generieren
    plot_graph(time_absolutes, data_get["Impedance_Z"], "Zeit [s]", "Impedanz [Ohm]", "Impedanz über Zeit", "impedance_over_time.pdf", use_log=True)
    plot_graph(time_absolutes, data_get["Resistance_Rp"], "Zeit [s]", "Widerstand [Ohm]", "Wiederstand über Zeit", "resistance_over_time.pdf")
    plot_graph(time_absolutes, data_get["Capacity_Cp[pF]"], "Zeit [s]", "Kapazität [pF]", "Kapazität über Zeit", "capacity_over_time.pdf", use_log=True)
    plot_graph_theta(time_absolutes, data_get["Phase"], "Zeit [s]", "Phase [°]", "Phase über Zeit", "phase_over_time.pdf")
    plot_graph(time_absolutes, data_get["Force"], "Zeit [s]", "Kraft [N]", "Kraft über Zeit", "force_over_time.pdf")
    plot_graph(data_get["Force"], data_get["Capacity_Cp[pF]"], "Kraft [N]", "Kapazität [pF]", "Kapazität über Kraft", "capacity_over_force.pdf", use_log=True)
    plot_graph(data_get["Force"], data_get["Impedance_Z"], "Kraft [N]", "Impedanz [Ohm]", "Impedanz über Kraft", "impedance_over_force.pdf", use_log=True)


    # fig, ax = plt.subplots()
    # ax.plot(time_absolutes, data_get["Impedance_Z"])
    # ax.set_xlabel("Zeit [s]")
    # ax.set_ylabel("Impedanz [Ohm]")
    # ax.set_title("Impedanz über Zeit")
    # ax.grid(True)
    # plt.show()
    # fig.savefig("Plots/impedance_over_time.pdf")

    # fig, ax = plt.subplots()
    # ax.plot(time_absolutes, data_get["Resistance_Rp"])
    # ax.set_xlabel("Zeit [s]")
    # ax.set_ylabel("Wiederstand R_p [Ohm]")
    # ax.set_title("Wiederstand R_p über Zeit")
    # ax.grid(True)
    # plt.show()

    # fig, ax = plt.subplots()
    # print(data_get.dtypes)
    # ax.plot(time_absolutes, data_get["Capacity_Cp[pF]"])
    # ax.set_xlabel("Zeit [s]")
    # ax.set_ylabel("Kapazität [pF]")
    # ax.set_title("Kapazität über Zeit")
    # ax.grid(True)    
    # plt.show()
    # fig.savefig("Plots/capacity_over_time.pdf")

    # fig, ax = plt.subplots()
    # ax.plot(time_absolutes, data_get["Phase"])
    # ax.set_xlabel("Zeit [s]")
    # ax.set_ylabel("Phase [°]")
    # ax.set_title("Phase über Zeit")
    # ax.grid(True)
    # plt.show()
    # fig.savefig("Plots/phase_over_time.pdf")

    # fig, ax = plt.subplots()
    # ax.plot(time_absolutes, data_get["Force"])
    # ax.set_xlabel("Zeit [s]")
    # ax.set_ylabel("Kraft [N]")
    # ax.set_title("Kraft über Zeit")
    # ax.grid(True)
    # plt.show()
    # fig.savefig("Plots/force_over_time.pdf")

    # fig, ax = plt.subplots()
    # ax.plot(data_get["Force"], data_get["Capacity_Cp[pF]"])
    # ax.set_xlabel("Kraft [N]")
    # ax.set_ylabel("Kapazität [pF]")
    # ax.set_title("Kapazität über Kraft")
    # ax.grid(True)
    # plt.show()
    # fig.savefig("Plots/capacity_over_force.pdf")

    # fig, ax = plt.subplots()
    # ax.plot(data_get["Force"], data_get["Impedance_Z"])
    # ax.set_xlabel("Kraft [N]")
    # ax.set_ylabel("Impedanz [Ohm]")
    # ax.set_title("Impedanz über Kraft")
    # ax.grid(True)
    # plt.show()
    # fig.savefig("Plots/impedance_over_force.pdf")