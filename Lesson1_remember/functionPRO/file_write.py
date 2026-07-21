with open("greeting.txt","w", encoding="utf-8") as file:
    file.write("Hello,automated tests!\n")
    file.write("Second line")

    # "r" - read
    # "w" - write
    # "a" - append
    # "r+" - read & write
    # "rb", "wb" - pdf, screenshots

    def log_test_result(test_name, status):
        with open("test_run.log","w",encoding="utf-8") as log_file: # будет перезаписывать и выдаст последний вызов функции
            log_file.write(f"{test_name}:{status}\n")

    log_test_result("test_login","PASSED")
    log_test_result("test_registration", "FAILED")
    log_test_result("test_logout", "SKIPPED")

