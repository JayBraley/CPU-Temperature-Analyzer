import sys
from parse_temps import (parse_raw_temps)
from piecewise_linear_interpolation import (interpolate)
from lin_least_squares import (least_square)

def main():
    '''
    This is the main driver for the CPU temperature analysis program.
    '''
    
    input_temps = sys.argv[1]

    # Collect the temperature data from the given input file
    with open(input_temps, 'r') as temps_file:
        times = []
        core_data = [[] for _ in range(0, 4)]

        for time, raw_core_data in parse_raw_temps(temps_file):
            times.append(time)
            for core_idx, reading in enumerate(raw_core_data):
                core_data[core_idx].append(reading)

        # For each core, print the time stamp and linear interpolation polynomial
        for core_idx in range(0, len(core_data)):
            x_set = []
            y_set = []

            # Set up file naming convention
            file_name = f"sample-input-core-{str(core_idx + 1).zfill(2)}.txt"
            with open(file_name, 'w') as output_file:

                for time_idx in range(0, len(times) - 1):
                    # Perform the interpolation for each timeframe within the subjected core
                    x0 = times[time_idx]
                    x1 = times[time_idx + 1]
                    y0 = core_data[core_idx][time_idx]
                    y1 = core_data[core_idx][time_idx + 1]
                    x_set.append(times[time_idx])
                    y_set.append(core_data[core_idx][time_idx])

                    # On the last interval, append the last x and y values
                    if (time_idx == len(times) - 2):
                        x_set.append(times[time_idx + 1])
                        y_set.append(core_data[core_idx][time_idx + 1])

                    (slope, intercept) = interpolate(y0, y1, x0, x1)
                    output_file.write(f"{x0} <= x <= {x1} ; y = {intercept:.4f} + {slope:.4f}x ; interpolation\n")
                    print(f"{x0} <= x <= {x1} ; y = {intercept:.4f} + {slope:.4f}x ; interpolation")

                # Perform the least squares approximation
                constants = least_square(x_set, y_set)
                output_file.write(f"0 <= x <= {x1} ; y = {constants[0]:.4f} + {constants[1]:.4f}x ; least-squares\n")
                print(f"0 <= x <= {x1} ; y = {constants[0]:.4f} + {constants[1]:.4f}x ; least-squares\n")
            
    
if __name__ == "__main__":
    main()