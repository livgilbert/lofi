from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
import warnings
import time
import subprocess
import sys
import re
import os

# volume ranges from 0 to 65535
PLAYBACK_VOLUME = 32768

# suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# setup webdriver
options = webdriver.FirefoxOptions()
options.headless = True

driver = webdriver.Firefox(options=options)

# adblock
driver.install_addon(os.path.join(os.path.expanduser("~"), ".mozilla/extensions/uBlock0@raymondhill.net.xpi"), temporary=True)

print("Initialized Driver")

# load video
driver.get("https://www.youtube.com/results?search_query=lofi+hip+hop+radio")

# waits for video element to be loaded
WebDriverWait(driver, 10).until(cond.presence_of_element_located((By.TAG_NAME, "ytd-video-renderer")))

video_item = driver.find_element_by_tag_name("ytd-video-renderer")
title = video_item.find_element_by_tag_name("a")
title.click()

print("Video Loaded")

# adjust volume

def get_audio_sinks():
    pactl_sink_inputs = subprocess.check_output(["pactl", "list", "sink-inputs"])
    return re.findall("Sink Input #(\d*)", str(pactl_sink_inputs))

initial_sinks = get_audio_sinks()

while(True):
    new_sinks = get_audio_sinks()
    if len(new_sinks) > len(initial_sinks):
        webdriver_sink = [sink for sink in new_sinks if sink not in initial_sinks][0]
        subprocess.run(["pactl", "set-sink-input-volume", webdriver_sink, str(PLAYBACK_VOLUME)])
        break
    else:
        time.sleep(0.1)

if "noclock" not in sys.argv:
    subprocess.Popen(["kitty", "--start-as=fullscreen", os.path.join(os.path.dirname(__file__), "clock.sh")])

while(True):
    time.sleep(1)
