import urequests

def wget(url):
    response = urequests.get(url)
    response.json()


def main():

    text = wget('https://raw.githubusercontent.com/mullinmax/esp32-programmer/master/main.py')

    with open(output.txt,'w') as f:
        f.write(text)


if __name__ == '__main__':
    main()