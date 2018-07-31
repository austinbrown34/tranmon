DAY_SECONDS = 86400
MHS_HASH = 1000000
HASH_NUMBER = 4294967296
HOUR_SECS = 3600
DAY_HOURS = 24
KW_WATS = 1000
SOLS_PER_HASH = 2
EQUIHASH_BLOCK_HEIGHT_CUTOFF = 850000
FULL_MINER_SHARE = 1
REDUCED_MINER_SHARE = 0.8

FORMULA_A_ALGORITHMS = ['LBRY', 'Skunkhash', 'Lyra2REv2', 'NeoScrypt', 'Pascal', 'Groestl', 'X11Gost', 'Blake (14r)', 'Myriad-Groestl']
FORMULA_B_ALGORITHMS = ['Ethash', 'CryptoNight', 'Blake (2b)']
FORMULA_C_ALGORITHMS = ['Equihash']

GPU_ALGORITHM_PERFORMANCE = {
    '_1080': {
        'Ethash': {
            'hashrate': 23.3,
            'power': 140
        },
        'Groestl': {
            'hashrate': 44.5,
            'power': 150
        },
        'X11Gost': {
            'hashrate': 13.5,
            'power': 145
        },
        'CryptoNight': {
            'hashrate': 0.00058,
            'power': 100
        },
        'Equihash': {
            'hashrate': 0.00055,
            'power': 130
        },
        'Lyra2REv2': {
            'hashrate': 46.5,
            'power': 150
        },
        'NeoScrypt': {
            'hashrate': 1.06,
            'power': 150
        },
        'LBRY': {
            'hashrate': 360,
            'power': 150
        },
        'Blake (2b)': {
            'hashrate': 2150,
            'power': 150
        },
        'Blake (14r)': {
            'hashrate': 3300,
            'power': 150
        },
        'Pascal': {
            'hashrate': 1250,
            'power': 150
        },
        'Skunkhash': {
            'hashrate': 36.5,
            'power': 150
        },
        'Myriad-Groestl': {
            'hashrate': 65.415,
            'power': 150
        }
    },
    '_280x': {
        'Ethash': {
            'hashrate': 11,
            'power': 220
        },
        'Groestl': {
            'hashrate': 23.8,
            'power': 250
        },
        'X11Gost': {
            'hashrate': 2.9,
            'power': 200
        },
        'CryptoNight': {
            'hashrate': 0.00049,
            'power': 220
        },
        'Equihash': {
            'hashrate': 0.00029,
            'power': 230
        },
        'Lyra2REv2': {
            'hashrate': 14.05,
            'power': 220
        },
        'NeoScrypt': {
            'hashrate': 0.490,
            'power': 250
        },
        'LBRY': {
            'hashrate': 60,
            'power': 200
        },
        'Blake (2b)': {
            'hashrate': 960,
            'power': 250
        },
        'Blake (14r)': {
            'hashrate': 1450,
            'power': 220
        },
        'Pascal': {
            'hashrate': 580,
            'power': 250
        },
        'Skunkhash': {
            'hashrate': 0,
            'power': 0
        },
        'Myriad-Groestl': {
            'hashrate': 34.986,
            'power': 250
        }
    },
    '_380': {
        'Ethash': {
            'hashrate': 20.2,
            'power': 145
        },
        'Groestl': {
            'hashrate': 15.5,
            'power': 130
        },
        'X11Gost': {
            'hashrate': 2.5,
            'power': 120
        },
        'CryptoNight': {
            'hashrate': 0.00053,
            'power': 120
        },
        'Equihash': {
            'hashrate': 0.000205,
            'power': 130
        },
        'Lyra2REv2': {
            'hashrate': 6.4,
            'power': 125
        },
        'NeoScrypt': {
            'hashrate': 0.35,
            'power': 145
        },
        'LBRY': {
            'hashrate': 44,
            'power': 135
        },
        'Blake (2b)': {
            'hashrate': 760,
            'power': 150
        },
        'Blake (14r)': {
            'hashrate': 1140,
            'power': 155
        },
        'Pascal': {
            'hashrate': 480,
            'power': 145
        },
        'Skunkhash': {
            'hashrate': 9,
            'power': 120
        },
        'Myriad-Groestl': {
            'hashrate': 22.785,
            'power': 130
        }
    },
    'Fury': {
        'Ethash': {
            'hashrate': 28.2,
            'power': 180
        },
        'Groestl': {
            'hashrate': 17.4,
            'power': 180
        },
        'X11Gost': {
            'hashrate': 4.5,
            'power': 140
        },
        'CryptoNight': {
            'hashrate': 0.0008,
            'power': 120
        },
        'Equihash': {
            'hashrate': 0.000455,
            'power': 200
        },
        'Lyra2REv2': {
            'hashrate': 14.2,
            'power': 190
        },
        'NeoScrypt': {
            'hashrate': 0.5,
            'power': 160
        },
        'LBRY': {
            'hashrate': 83,
            'power': 200
        },
        'Blake (2b)': {
            'hashrate': 1400,
            'power': 260
        },
        'Blake (14r)': {
            'hashrate': 1900,
            'power': 270
        },
        'Pascal': {
            'hashrate': 950,
            'power': 270
        },
        'Skunkhash': {
            'hashrate': 0,
            'power': 0
        },
        'Myriad-Groestl': {
            'hashrate': 25.578,
            'power': 180
        }
    },
    '_470': {
        'Ethash': {
            'hashrate': 26,
            'power': 120
        },
        'Groestl': {
            'hashrate': 14.5,
            'power': 120
        },
        'X11Gost': {
            'hashrate': 5.3,
            'power': 125
        },
        'CryptoNight': {
            'hashrate': 0.00066,
            'power': 100
        },
        'Equihash': {
            'hashrate': 0.00026,
            'power': 110
        },
        'Lyra2REv2': {
            'hashrate': 4.4,
            'power': 120
        },
        'NeoScrypt': {
            'hashrate': 0.6,
            'power': 140
        },
        'LBRY': {
            'hashrate': 80,
            'power': 120
        },
        'Blake (2b)': {
            'hashrate': 800,
            'power': 120
        },
        'Blake (14r)': {
            'hashrate': 1100,
            'power': 120
        },
        'Pascal': {
            'hashrate': 510,
            'power': 120
        },
        'Skunkhash': {
            'hashrate': 15,
            'power': 105
        },
        'Myriad-Groestl': {
            'hashrate': 21.315,
            'power': 120
        }
    },
    '_480': {
        'Ethash': {
            'hashrate': 29.5,
            'power': 135
        },
        'Groestl': {
            'hashrate': 18,
            'power': 130
        },
        'X11Gost': {
            'hashrate': 6.7,
            'power': 140
        },
        'CryptoNight': {
            'hashrate': 0.00073,
            'power': 110
        },
        'Equihash': {
            'hashrate': 0.00029,
            'power': 120
        },
        'Lyra2REv2': {
            'hashrate': 4.9,
            'power': 130
        },
        'NeoScrypt': {
            'hashrate': 0.65,
            'power': 150
        },
        'LBRY': {
            'hashrate': 95,
            'power': 140
        },
        'Blake (2b)': {
            'hashrate': 990,
            'power': 150
        },
        'Blake (14r)': {
            'hashrate': 1400,
            'power': 150
        },
        'Pascal': {
            'hashrate': 690,
            'power': 135
        },
        'Skunkhash': {
            'hashrate': 18,
            'power': 115
        },
        'Myriad-Groestl': {
            'hashrate': 26.46,
            'power': 130
        }
    },
    '_570': {
        'Ethash': {
            'hashrate': 27.9,
            'power': 120
        },
        'Groestl': {
            'hashrate': 15.5,
            'power': 110
        },
        'X11Gost': {
            'hashrate': 5.6,
            'power': 110
        },
        'CryptoNight': {
            'hashrate': 0.0007,
            'power': 110
        },
        'Equihash': {
            'hashrate': 0.00026,
            'power': 110
        },
        'Lyra2REv2': {
            'hashrate': 5.5,
            'power': 110
        },
        'NeoScrypt': {
            'hashrate': 0.63,
            'power': 140
        },
        'LBRY': {
            'hashrate': 115,
            'power': 115
        },
        'Blake (2b)': {
            'hashrate': 840,
            'power': 115
        },
        'Blake (14r)': {
            'hashrate': 1140,
            'power': 115
        },
        'Pascal': {
            'hashrate': 580,
            'power': 135
        },
        'Skunkhash': {
            'hashrate': 16.3,
            'power': 110
        },
        'Myriad-Groestl': {
            'hashrate': 22.785,
            'power': 110
        }
    },
    '_580': {
        'Ethash': {
            'hashrate': 30.2,
            'power': 135
        },
        'Groestl': {
            'hashrate': 18.5,
            'power': 115
        },
        'X11Gost': {
            'hashrate': 6.9,
            'power': 110
        },
        'CryptoNight': {
            'hashrate': 0.00069,
            'power': 115
        },
        'Equihash': {
            'hashrate': 0.00029,
            'power': 120
        },
        'Lyra2REv2': {
            'hashrate': 5.7,
            'power': 120
        },
        'NeoScrypt': {
            'hashrate': 0.065,
            'power': 150
        },
        'LBRY': {
            'hashrate': 135,
            'power': 145
        },
        'Blake (2b)': {
            'hashrate': 990,
            'power': 150
        },
        'Blake (14r)': {
            'hashrate': 1350,
            'power': 130
        },
        'Pascal': {
            'hashrate': 690,
            'power': 145
        },
        'Skunkhash': {
            'hashrate': 18.5,
            'power': 115
        },
        'Myriad-Groestl': {
            'hashrate': 27.195,
            'power': 115
        }
    },
    'Vega56': {
        'Ethash': {
            'hashrate': 36.5,
            'power': 210
        },
        'Groestl': {
            'hashrate': 38,
            'power': 190
        },
        'X11Gost': {
            'hashrate': 10.5,
            'power': 230
        },
        'CryptoNight': {
            'hashrate': 0.00185,
            'power': 190
        },
        'Equihash': {
            'hashrate': 440,
            'power': 190
        },
        'Lyra2REv2': {
            'hashrate': 13,
            'power': 190
        },
        'NeoScrypt': {
            'hashrate': 0.29,
            'power': 160
        },
        'LBRY': {
            'hashrate': 260,
            'power': 210
        },
        'Blake (2b)': {
            'hashrate': 1900,
            'power': 230
        },
        'Blake (14r)': {
            'hashrate': 2600,
            'power': 210
        },
        'Pascal': {
            'hashrate': 1350,
            'power': 230
        },
        'Skunkhash': {
            'hashrate': 36,
            'power': 210
        },
        'Myriad-Groestl': {
            'hashrate': 55.86,
            'power': 190
        }
    },
    'Vega64': {
        'Ethash': {
            'hashrate': 40,
            'power': 230
        },
        'Groestl': {
            'hashrate': 44,
            'power': 200
        },
        'X11Gost': {
            'hashrate': 12,
            'power': 250
        },
        'CryptoNight': {
            'hashrate': 0.00185,
            'power': 200
        },
        'Equihash': {
            'hashrate': 0.00045,
            'power': 200
        },
        'Lyra2REv2': {
            'hashrate': 13,
            'power': 200
        },
        'NeoScrypt': {
            'hashrate': 0.29,
            'power': 170
        },
        'LBRY': {
            'hashrate': 280,
            'power': 230
        },
        'Blake (2b)': {
            'hashrate': 2200,
            'power': 250
        },
        'Blake (14r)': {
            'hashrate': 2900,
            'power': 230
        },
        'Pascal': {
            'hashrate': 1550,
            'power': 250
        },
        'Skunkhash': {
            'hashrate': 40,
            'power': 230
        },
        'Myriad-Groestl': {
            'hashrate': 64.68,
            'power': 200
        }
    },
    '_750Ti': {
        'Ethash': {
            'hashrate': 0.5,
            'power': 45
        },
        'Groestl': {
            'hashrate': 8.3,
            'power': 80
        },
        'X11Gost': {
            'hashrate': 2,
            'power': 55
        },
        'CryptoNight': {
            'hashrate': 0.00025,
            'power': 55
        },
        'Equihash': {
            'hashrate': 0.000075,
            'power': 55
        },
        'Lyra2REv2': {
            'hashrate': 6.64,
            'power': 70
        },
        'NeoScrypt': {
            'hashrate': 0.22,
            'power': 75
        },
        'LBRY': {
            'hashrate': 51,
            'power': 75
        },
        'Blake (2b)': {
            'hashrate': 350,
            'power': 75
        },
        'Blake (14r)': {
            'hashrate': 610,
            'power': 75
        },
        'Pascal': {
            'hashrate': 200,
            'power': 55
        },
        'Skunkhash': {
            'hashrate': 0,
            'power': 0
        },
        'Myriad-Groestl': {
            'hashrate': 12.201,
            'power': 80
        }
    },
    '_1050Ti': {
        'Ethash': {
            'hashrate': 13.9,
            'power': 70
        },
        'Groestl': {
            'hashrate': 14.5,
            'power': 75
        },
        'X11Gost': {
            'hashrate': 4.9,
            'power': 75
        },
        'CryptoNight': {
            'hashrate': 0.0003,
            'power': 50
        },
        'Equihash': {
            'hashrate': 0.00018,
            'power': 75
        },
        'Lyra2REv2': {
            'hashrate': 14.5,
            'power': 75
        },
        'NeoScrypt': {
            'hashrate': 0.42,
            'power': 75
        },
        'LBRY': {
            'hashrate': 110,
            'power': 75
        },
        'Blake (2b)': {
            'hashrate': 700,
            'power': 75
        },
        'Blake (14r)': {
            'hashrate': 1050,
            'power': 75
        },
        'Pascal': {
            'hashrate': 380,
            'power': 75
        },
        'Skunkhash': {
            'hashrate': 11.5,
            'power': 75
        },
        'Myriad-Groestl': {
            'hashrate': 21.315,
            'power': 75
        }
    },
    '_1060': {
        'Ethash': {
            'hashrate': 22.5,
            'power': 90
        },
        'Groestl': {
            'hashrate': 20.5,
            'power': 90
        },
        'X11Gost': {
            'hashrate': 7.2,
            'power': 90
        },
        'CryptoNight': {
            'hashrate': 0.00043,
            'power': 70
        },
        'Equihash': {
            'hashrate': 0.00027,
            'power': 90
        },
        'Lyra2REv2': {
            'hashrate': 20.3,
            'power': 90
        },
        'NeoScrypt': {
            'hashrate': 0.5,
            'power': 90
        },
        'LBRY': {
            'hashrate': 170,
            'power': 90
        },
        'Blake (2b)': {
            'hashrate': 990,
            'power': 80
        },
        'Blake (14r)': {
            'hashrate': 1550,
            'power': 90
        },
        'Pascal': {
            'hashrate': 590,
            'power': 90
        },
        'Skunkhash': {
            'hashrate': 18,
            'power': 90
        },
        'Myriad-Groestl': {
            'hashrate': 30.135,
            'power': 90
        }
    },
    '_1070': {
        'Ethash': {
            'hashrate': 30,
            'power': 120
        },
        'Groestl': {
            'hashrate': 35.5,
            'power': 130
        },
        'X11Gost': {
            'hashrate': 11.5,
            'power': 120
        },
        'CryptoNight': {
            'hashrate': 0.0005,
            'power': 100
        },
        'Equihash': {
            'hashrate': 0.00043,
            'power': 120
        },
        'Lyra2REv2': {
            'hashrate': 35.5,
            'power': 130
        },
        'NeoScrypt': {
            'hashrate': 1,
            'power': 155
        },
        'LBRY': {
            'hashrate': 270,
            'power': 120
        },
        'Blake (2b)': {
            'hashrate': 1600,
            'power': 120
        },
        'Blake (14r)': {
            'hashrate': 2500,
            'power': 125
        },
        'Pascal': {
            'hashrate': 940,
            'power': 120
        },
        'Skunkhash': {
            'hashrate': 26.5,
            'power': 120
        },
        'Myriad-Groestl': {
            'hashrate': 52.185,
            'power': 130
        }
    },
    '_1080Ti': {
        'Ethash': {
            'hashrate': 35,
            'power': 140
        },
        'Groestl': {
            'hashrate': 58,
            'power': 210
        },
        'X11Gost': {
            'hashrate': 19.5,
            'power': 170
        },
        'CryptoNight': {
            'hashrate': 0.00083,
            'power': 140
        },
        'Equihash': {
            'hashrate': 0.000685,
            'power': 190
        },
        'Lyra2REv2': {
            'hashrate': 64,
            'power': 190
        },
        'NeoScrypt': {
            'hashrate': 1.4,
            'power': 190
        },
        'LBRY': {
            'hashrate': 460,
            'power': 190
        },
        'Blake (2b)': {
            'hashrate': 2800,
            'power': 190
        },
        'Blake (14r)': {
            'hashrate': 4350,
            'power': 210
        },
        'Pascal': {
            'hashrate': 1700,
            'power': 210
        },
        'Skunkhash': {
            'hashrate': 47.5,
            'power': 190
        },
        'Myriad-Groestl': {
            'hashrate': 85.26,
            'power': 210
        }
    }
}
