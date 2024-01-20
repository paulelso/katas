import sys
def run_timing():
    def run_timing():
        total_time = 0
        number_of_runs = 0
        while True:   
            run_time = input("Enter 10 km run time (press Enter to finish): ")
            if run_time == "":
                break
            try:            
                total_time += float(run_time)
            except ValueError:
                print("Invalid input, please enter a valid number.")
                sys.exit(1)         
            number_of_runs += 1
        if number_of_runs != 0:        
            average_time = total_time / number_of_runs
        print(f"Average of {average_time:.2f}, over {number_of_runs} runs")

    if __name__ == "__main__":
        run_timing()

if __name__ == "__main__":
    run_timing()
