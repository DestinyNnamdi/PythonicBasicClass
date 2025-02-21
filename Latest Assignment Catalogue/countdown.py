import time

def countdown(t):
    start_time = time.time()
    end_time = start_time + t
    checkpoints = (0.25, 0.5, 0.75)
    while time.time() < end_time:
        current_time = time.time()
        elapsed_time = current_time - start_time
        remaining_time = end_time - current_time
        percentage = (elapsed_time / t) * 100

        for checkpoint in checkpoints:
            if percentage >= checkpoint * 100 and percentage < (checkpoint + 0.01) * 100:
                print(f"Countdown: {percentage:2f}% remaining")

        # Update every 0.1 second.
        time.sleep(0.1)

    print("Countdown Completed!")

countdown(60)