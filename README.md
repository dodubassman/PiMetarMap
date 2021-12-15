# PiMetarMap

PiMetarMap is yet another METAR plotter running on raspberry pi. It uses Adafruit CircuitPython NeoPixel to controle WS2811 addressable LEDs.

Most of the solution on Github are made using US VFR/MVFR/IFR rules to drive led colors.

This project is using French MétéoFrance color code as pictured here

- Blue: visibility > 9999m and ceiling above 3000ft
- Green: visibility > 8000m and ceiling above 2000ft
- Yellow: visibility > 5000m and ceiling above 1000ft
- Orange: visibility > 1500m and ceiling above 500ft
- Red: visibility > 800m and ceiling above 200ft
- Purple: visibility <= 800m and ceiling bellow 200ft

## Configuration

### VMC levels

From 0 to 5, or very bad weather to very nice, following the scale explain right above.

Colors have to be hex RGB values.

You can cheat and select the same color if you need less precision and don't want to tweak the code.

Default values are :

VMC_LEVEL_COLORS = {
    0: '#cc00cc',
    1: '#ff0000',
    2: '#ff3000',
    3: '#ffff00',
    4: '#00ff00',
    5: '#0000ff',
}

### Airports

Add ICAO airports codes with Led position in the strip as index.

```Python
AIRPORTS = {
    0: 'LFRH',
    3: 'LFJR',
    8: 'LFOV',
    13: 'LFRN',
    18: 'LFRV',
...
}
```

### Weather API

Currently using [Aviation Weather REST API](https://avwx.rest/). But easly adaptable to other services by implementing the [ProviderInterface](https://github.com/dodubassman/PiMetarMap/blob/main/pmm/metar/provider/__init__.py#L6).

You'll need to register for free and get an authorisation token if you plan to use AVWX.rest.

Api calls are throttled to stay within the quota of the METAR provider service. You'll have to specify this quota. AVWX.rest limit free account to 4000 call/day.

```Python
AVWX_WEATHER_API = {
    'daily_quota': 4000,
    'bearer': '<your_secret_token_goes_here>',
    'endpoint': 'https://avwx.rest/api/metar/',
}
```

### NeoPixel

Some mandatory settings to specify :

* The Raspberry Pi GPIO pin the commande wire of your led strip is connected to (NeoPixel requires that it is only one of D10, D12, D18 or D21)
* Number of led you have on your strip
* Brightness used on daylight, before 6am (float value from 0 to 1. 0 is "on", 1 is "eye piercing", and you'll need an extra power supply because your DC5V @2.1Amp from usb will not be enough if you powered it to max brightness! 0.2 if really enough)
* Brighness used after 8pm.


```Python
NEOPIXEL = {
    'gpio_pin': 'D18',
    'num_pixels': 50,
    'day_brightness': 0.2,
    'night_brightness': 0.05
}
```
