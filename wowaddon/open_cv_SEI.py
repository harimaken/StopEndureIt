import pyscreenshot as imagegrab
import time

# screen_size = None
# screen_start_point = None
# screen_end_point = None


def check_screen_size():
    print("Checking screen size")
    img = imagegrab.grab()
    # img.save('temp.png')
    screen_size = None
    screen_start_point = None
    screen_end_point = None

    screen_size = (img.size[0], img.size[1])

    screen_start_point = (screen_size[0] * 0.39, screen_size[1] * 0.18)
    screen_end_point = (screen_size[0] * 0.61, screen_size[1] * 0.42)
    print("Screen size is " + str(screen_size))
    return screen_start_point, screen_end_point

def make_screenshot():
    screen_start_point, screen_end_point = check_screen_size()
    print("Capturing screen")
    time.sleep(3)
    screenshot = imagegrab.grab(bbox=(screen_start_point[0], screen_start_point[1], screen_end_point[0], screen_end_point[1]))
    #screenshot_name = 'lfg_' + str(int(time.time())) + '.png'
    screenshot_name = 'lfg' + '.png'
    screenshot.save(screenshot_name)
    return screenshot_name


if __name__ == '__main__':
    check_screen_size()
    make_screenshot()