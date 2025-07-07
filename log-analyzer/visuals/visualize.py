import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV report
df = pd.read_csv("../reports/output.csv")

# =============================
# 1. IP Origin by Country (Bar Chart)
# =============================
def plot_country_counts():
    country_counts = df['country'].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    country_counts.plot(kind='bar', color='skyblue')
    plt.title("Top IP Origin Countries")
    plt.xlabel("Country")
    plt.ylabel("Number of Logins")
    plt.tight_layout()
    plt.savefig("country_bar_chart.png")
    print("[+] Saved: visuals/country_bar_chart.png")

# =============================
# 2. Login Attempts per Hour
# =============================
def plot_login_hours():
    # Fix time formatting
    df['hour'] = df['timestamp'].str.extract(r'\d{2}:(\d{2}):')[0]
    df['hour'] = pd.to_numeric(df['hour'], errors='coerce')

    plt.figure(figsize=(10, 5))
    df['hour'].dropna().astype(int).plot.hist(bins=24, rwidth=0.8)
    plt.title("Login Attempts by Minute Value")
    plt.xlabel("Minute")
    plt.ylabel("Number of Attempts")
    plt.tight_layout()
    plt.savefig("login_hour_histogram.png")
    print("[+] Saved: visuals/login_hour_histogram.png")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))  # switch to visuals/ dir
    plot_country_counts()
    plot_login_hours()
