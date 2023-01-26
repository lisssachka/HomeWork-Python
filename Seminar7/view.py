def console_view(data, end = '\n'):
    if type(data) == list:
        data_new = data[:]
        data_new = '\n'.join(data_new)

        print(data_new, end=end)

    elif type(data) == str:
        print(data + end)