VMC_LEVEL_COLORS = {
    0: '#cc00cc',
    1: '#ff0000',
    2: '#ff3000',
    3: '#ffff00',
    4: '#00ff00',
    5: '#0000ff',
}

AIRPORTS = (
    'LFRS',
    'LFRI',
    'LFRZ',
    'LFOV',
    'LFFI',
    'LFRN',
    'LFJB',
    'LFBH',
)

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
    'brightness': 0.2
}
