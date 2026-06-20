for entry in parsed_records:
            for course in metrics:
                metrics[course] += int(entry[course])
            counter += 1
