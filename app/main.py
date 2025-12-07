def create_report(data_file_name: str, report_file_name: str):
    file = open(data_file_name, "r")
    my_dict = {"supply": 0, "buy": 0}

    for line in file.readlines():
        my_dict[line.split(",")[0]] += int(line.split(",")[1])

    my_dict["result"] = my_dict.get("supply") - my_dict.get("buy")

    result = "\n".join(f"{key},{value}" for key, value in my_dict.items()) + "\n"

    fp = open(report_file_name, "w")
    fp.write(result)
    fp.close()
    file.close()
    return  fp

# create_report("../bananas.csv", "grs.csv")
