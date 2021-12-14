VMC_LEVEL_COLORS = {
    0: '#cc00cc',
    1: '#ff0000',
    2: '#ff3000',
    3: '#ffff00',
    4: '#00ff00',
    5: '#0000ff',
}

""" Airports list.
    Dict[int, str]: Led index, icao code
"""
AIRPORTS = {
    0: 'LFRH',
    3: 'LFJR',
    8: 'LFOV',
    13: 'LFRN',
    18: 'LFRV',
    29: 'LFRI',
    36: 'LFRZ',
    40: 'LFRS',
    49: 'LFBH',
}

AVWX_WEATHER_API = {
    'daily_quota': 4000,
    'bearer': '<your_secret_token_goes_here>',
    'endpoint': 'https://avwx.rest/api/metar/',
}

NEOPIXEL = {
    # NeoPixels must be connected to D10, D12, D18 or D21 to work
    'gpio_pin': 'D18',
    # Number of led in the strip.
    'num_pixels': 50,
    'day_brightness': 0.2,
    'night_brightness': 0.05
}
