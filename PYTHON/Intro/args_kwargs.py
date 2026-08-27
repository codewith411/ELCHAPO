def args_kwargs(*args, **kwargs):
    print("--------------------------------")
    print("All args:", args)
    print("All kwargs:", kwargs)
    print("--------------------------------")


# Positional arguments go into *args
# Keyword arguments go into **kwargs

args_kwargs(12, 27, 64, name="Brian", age=28)