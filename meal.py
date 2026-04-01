def main():
    time=input("What time is it ? ")
    range=convert(time)
    if 7<=range<=8:
        print("breakfast time")
    elif 12<=range<=13:
        print("lunch time")
    elif 18<=range<=19:
        print("dinner time")


def convert(time):
    hours,min=time.split(":")
    hours=float(hours)
    min=float(min)
    min=min/60
    return hours+min


if __name__ == "__main__":
    main()
