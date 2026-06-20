with open("report.txt", "w") as log:
        log.write("============ STUDENT PERFORMANCE REPORT ============\n")
        log.write(f"Total Students Processed: {counter}\n\n")

        for course, aggregated_sum in metrics.items():
            computed_average = aggregated_sum / counter
            log.write(f"Average {course} Score: {computed_average:.2f}\n")

        log.write("====================================================\n")
