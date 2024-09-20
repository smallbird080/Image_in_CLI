# Image_in_CLI

## feature (on dev.)

display image on shell !

ASCII(gray-scale) / Color (rgb pixel) mode


## Usage

```markdown
python showimg.py [-h] [-a] [-r] [-c] filename [string] [width]

display image in terminal : Color or ASCII art

positional arguments:
    filename    path to image file
    string      string to use for pixel representation in normal color mode (default: "██")
    width       width of the image in characters (default: terminal width)

options:
    -h, --help  show this help message and exit
    -a          ascii mode: display image as ascii art (default: False)
    -r          resize image - decrease height (default: False)
    -c          advanced color mode: combine color and ascii mode (default: False)
```


## TODO

fix advanced color mode

argument parsing exception handling