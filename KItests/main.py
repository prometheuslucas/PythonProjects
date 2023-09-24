import PySimpleGUI as sg
import numpy as np
import math


# gaussian function
def gaussian(mu, var, x):
    ''' f takes in a mean and squared variance, and an input x
       and returns the gaussian value.'''
    coefficient = 1.0 / math.sqrt(2.0 * math.pi * var)
    exponential = math.exp(-0.5 * (x - mu) ** 2 / var)
    return coefficient * exponential


def create_sensor_matrix(climate, measurement):
    """
    create sensor model

    Args:
        climate (): list of 12 temperature values
        measurement (): temperature measurement

    Returns:
        numpy array: with a normalized distance between the measurement and the temperature values in climate
    """
    sensor_list = [gaussian(temp, 2., measurement) for temp in climate]

    sensor_mat = np.array(sensor_list)
    return sensor_mat


def sense(p, climate, measurement):
    """
    get probability of being in a month after the measurement

    Args:
        p (): probability vector of being in a month
        climate (): list of 12 temperature values
        measurement (): temperature measurement

    Returns:
        probability of being in a month after the measurement

    """
    sensor_mat = create_sensor_matrix(climate, measurement)

    aux = sensor_mat * np.array(p).flatten()  # dot product
    aux = aux / np.sum(aux)  # normalization

    return aux


def create_transition_matrix():
    """
    create transition model

    Returns:
        transition model as numpy array
    """
    trans_vec = np.zeros(12)
    trans_vec[0] = 0.9
    trans_vec[-1] = 0.1

    transition_list = [np.roll(trans_vec, 1 + i) for i in range(0, 12)]

    transition_mat = np.array(transition_list)

    return transition_mat


def move(p):
    """
    Calculate probability of being in a month after movement of 28 days

    Args:
        p (): probability vector of being in a month

    Returns:
        probability of being in a month after movement of 28 days
    """
    transition_mat = create_transition_matrix()

    aux = np.matmul(transition_mat.transpose(), np.array(p).flatten())  # matrix multiplication

    return aux


def localize(climate, measurements):
    """
    estimate in which month we are given a list of temperature measurements taken with a distance of 28 days
    in the given climate zone

    Args:
        climate (): list of 12 temperature values
        measurements (): list of temperature measurements

    Returns:
        final probability of being in a month after taken len(measurements) measurements
        trajectory of probabilities
    """
    p = 1 / 12 * np.ones(12)

    trajectory_move = []
    trajectory_move.append(p)

    def decimal_to_percent(x):
        return str(np.around(x * 100, decimals=4)) + '%'

    for k in range(len(measurements)):
        p = move(p)
        print('After move')
        print(np.vectorize(decimal_to_percent)(p))
        p = sense(p, climate, measurements[k])
        print('After sense')
        print(np.vectorize(decimal_to_percent)(p))
        trajectory_move.append(p)

    return p, trajectory_move


if __name__ == '__main__':
    ui = False
    if (ui):
        # Define the window layout
        layout = [
            [sg.Text("Enter measurements (comma-separated):")],
            [sg.Input(key="-MEASUREMENTS-")],
            [sg.Text("Enter climate (comma-separated):")],
            [sg.Input(key="-CLIMATE-")],
            [sg.Button("Run"), sg.Button("Exit")]
        ]

        # Create the window
        window = sg.Window("Localize", layout)

        # Create an event loop
        while True:
            event, values = window.read()
            # End program if user closes window or presses the Exit button
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            # Run the localize function if user presses the Run button
            elif event == "Run":
                # Get the input values as lists of floats
                measurements = [float(x) for x in values["-MEASUREMENTS-"].split(",")]
                climate = [float(x) for x in values["-CLIMATE-"].split(",")]
                # Call the localize function and print the result
                p, trajectory_move = localize(climate, measurements)

        # Close the window
        window.close()

    else:
        measurements = [20, 15, 10, 4]
        climate_gm = [0.8, 1.1, 4.3, 8.6, 12.6, 15.6, 17.5, 17, 13.7, 9.7, 5.2, 2]

        p, trajectory_move = localize(climate_gm, measurements)
