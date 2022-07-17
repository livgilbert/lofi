# lofi

A script I've thrown together to open up everyone's favorite YouTube livestream in the background, bring the volume down, and optionally make an ambient clock as well.

## Usage
Just run `python lofi.py`. You can add `noclock` if you don't want the clock to open.

## Requirements

All Python requirements are listed in `requirements.txt` and can be installed with `pip install -r requirements.txt`. The script also expects the adblocker uBlock for Firefox to be located at "~/.mozilla/extensions/uBlock0@raymondhill.net.xpi"

`termclock` is required for the clock component, and currently the terminal to use is hardcoded as `kitty`.

## Configuration

The volume to adjust the stream to can be set by changing `PLAYBACK_VOLUME` in the `lofi.py` script. It ranges from 0 to 65535, and is 32768 (50%) by default.

## Todo

- Improve CLI
  - Help menu
  - Allow termclock parameters to be passed to the script
  - Allow for any terminal emulator to be used for the clock
- Various performance improvements can likely be made
