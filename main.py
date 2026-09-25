import os
import random
import sqlite3
import matplotlib.pyplot as plt


def init_database(db_path: str = "data.db") -> None:
    """Initializes a local SQLite database with dummy financial and climate data."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            price REAL NOT NULL,
            temp_day INTEGER NOT NULL,
            temp_night INTEGER NOT NULL
        )
    """)
    
    # Populate with initial mock data if empty
    cursor.execute("SELECT COUNT(*) FROM metrics")
    if cursor.fetchone()[0] == 0:
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        mock_data = []
        for i, day in enumerate(days):
            price = round(random.uniform(70.0, 80.0), 2)
            t_day = random.randint(15, 25)
            t_night = t_day - random.randint(5, 10)
            mock_data.append((f"2026-03-0{i+1}", price, t_day, t_night))
            
        cursor.executemany(
            "INSERT INTO metrics (date, price, temp_day, temp_night) VALUES (?, ?, ?, ?)",
            mock_data
        )
        conn.commit()
    conn.close()


def fetch_metrics(db_path: str = "data.db") -> list:
    """Fetches metric records from the SQLite database."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT date, temp_day, temp_night, price FROM metrics ORDER BY date")
    rows = cursor.fetchall()
    conn.close()
    return rows


def generate_temperature_plot(data: list, output_file: str = "temperature_plot.png") -> str:
    """Generates and saves a weekly temperature trend plot using Matplotlib."""
    dates = [row[0] for row in data]
    temp_day = [row[1] for row in data]
    temp_night = [row[2] for row in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, temp_day, marker='o', color='r', linestyle='--', label='Day Temperature (°C)')
    plt.plot(dates, temp_night, marker='o', color='b', linestyle='--', label='Night Temperature (°C)')
    
    plt.title('Weekly Temperature Trend Analysis', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Temperature (°C)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    plt.savefig(output_file, dpi=300)
    plt.close()
    return output_file


if __name__ == "__main__":
    db_file = "data.db"
    init_database(db_file)
    records = fetch_metrics(db_file)
    
    plot_path = generate_temperature_plot(records)
    print(f"Plot successfully saved to {plot_path}")
