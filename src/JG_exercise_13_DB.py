# JG
# November 27, 2024
# The program creates a database with cities in Florida

import sqlite3
import matplotlib.pyplot as plt

# Create a list of cities with population
cities = [("Miami", 455924), ("Orlando", 320742), ("Tampa", 403364), ("Jacksonville", 985843), ("Ocala", 68426), ("Clermont", 48621), ("Bradenton", 57076), ("Tallahassee", 202221), ("Naples", 19704), ("Sarasota", 57602)]

def insert_cities(conn):

    # Make a cursor with the connection
    cursor = conn.cursor()

    # Insert all of the cities
    for city, population in cities:

        cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city, 2024, population))

    conn.commit()


def grow_population(conn):

    cursor = conn.cursor()

    # Calculate population growth for the next 20 years
    for year in range(2025, 2044):

        # Calculate population growth for every city
        for city_name in cities:

            # Get the population in the previous year
            current_population = cursor.execute('SELECT population FROM population WHERE city = ? AND year = ?', (city_name, year - 1))

            # Increase the population by 2%
            new_population = int(current_population * 1.02)

            # Save the projected population to the table
            cursor.execute('INSERT INTO population (city, year, population) VALUES (?, ?, ?)', (city_name, year, new_population))

    conn.commit()


# Function to plot population growth for a selected city
def show_city_growth(conn):

    # Make a cursor with the connection
    cursor = conn.cursor()

    # Loop
    while True:

        # Ask the user to choose a city or to exit
        city = input("Choose a city from the following options: Miami, Orlando, Tampa, Jacksonville, Ocala, Clermont, Bradenton, Tallahassee, Naples, Sarasota (or type 'exit'): ")

        # Check if the user wants to quit
        if city == 'exit':
            break

        years = []

        populations = []

        # Get the population for all years
        rows = cursor.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (city,))

        # Create arrays for the population data
        for row in rows:

            years.append(row[0])

            populations.append(row[1])

        # Show the data in a plot
        plt.plot(years, populations, marker='o')

        plt.title(f'Population Growth in {city}')

        plt.xlabel('Year')

        plt.ylabel('Population')

        plt.grid()

        plt.show()


def main():

    # Create the population database
    conn = sqlite3.connect('population_JG.db')

    cursor = conn.cursor()

    # Create the population table
    cursor.execute('''
        create table if not exists population (
            city text,
            year integer,
            population integer
        )
    ''')

    conn.commit()

    insert_cities(conn)

    grow_population(conn)

    show_city_growth(conn)

    conn.close()


main()
