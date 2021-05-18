from airium import Airium

from pathlib import Path



def generate_html():
    a = Airium()

    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="Speech Evaluation")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
        with a.body():
            a.h5(_t="Hello, world!")

    return str(a)


if __name__ == '__main__':
    html = generate_html()
    Path('./out/').mkdir(exist_ok=True)
    with open('./out/index.html', 'w') as file:
        file.write(html)
