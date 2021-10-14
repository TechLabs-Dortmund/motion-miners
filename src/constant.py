import numpy as np

"""
Pre-defined information for analysis
"""

# this dict is based on layout_overview.pdf
region_flow_dict = {
    "region_name": [
        "Not in use",
        "Pre-checkin",
        "Waiting Checkin",
        "Checkin Main",
        "Waiting I",
        "Doctor Table",
        "Vaccination",
        "Waiting II",
        "Checkout",
        "Waiting III",
    ],
    "region_id": [
        1,
        [2, 5],
        90,
        [3, 4],
        91,
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
        92,
        [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
        93,
    ],
    "flow_id": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
}

txpower_vs_distance = {
    "Distance(m)": [0, 1, 3, 5, 10, 15, 20, 30, 40, 50],
    "-30(dBm)": [
        -63,
        -92,
        -99,
        -101,
        np.nan,
        np.nan,
        np.nan,
        np.nan,
        np.nan,
        np.nan,
    ],
    "-20(dBm)": [-47, -79, -84, -90, -95, -98, -102, np.nan, np.nan, np.nan],
    "-16(dBm)": [-42, -71, -82, -88, -95, -97, -102, np.nan, np.nan, np.nan],
    "-12(dBm)": [-40, -68, -74, -84, -89, -95, -97, -102, np.nan, np.nan],
    "-8(dBm)": [-40, -66, -73, -82, -87, -92, -94, -96, -99, -102],
    "-4(dBm)": [-34, -58, -70, -74, -81, -90, -92, -93, -99, -102],
    "0(dBm)": [-27, -59, -67, -71, -79, -84, -87, -92, -94, -100],
    "4(dBm)": [-2, -57, -62, -67, -75, -82, -85, -88, -91, -99],
}

regions = [
    "Not in use",
    "Pre-checkin",
    "Waiting Checkin",
    "Checkin Main",
    "Waiting I",
    "Doctor Table",
    "Vaccination",
    "Waiting II",
    "Checkout",
    "Waiting III",
]

beacons_each_region = {
    "Not in use": [
        "Beacon_201",
        "Beacon_202",
        "Beacon_203",
        "Beacon_258",
        "Beacon_259",
        "Beacon_260",
    ],
    "Pre-checkin": [
        "Beacon_271",
        "Beacon_257",
        "Beacon_256",
        "Beacon_255",
        "Beacon_254",
        "Beacon_253",
    ],
    "Waiting Checkin": [],
    "Checkin Main": [
        "Beacon_204",
        "Beacon_205",
        "Beacon_206",
        "Beacon_207",
        "Beacon_208",
        "Beacon_209",
        "Beacon_210",
    ],
    "Waiting I": [],
    "Doctor Table": [
        "Beacon_211",
        "Beacon_212",
        "Beacon_213",
        "Beacon_214",
        "Beacon_215",
        "Beacon_216",
        "Beacon_217",
        "Beacon_218",
        "Beacon_219",
        "Beacon_220",
    ],
    "Vaccination": [
        "Beacon_221",
        "Beacon_222",
        "Beacon_223",
        "Beacon_224",
        "Beacon_225",
        "Beacon_226",
        "Beacon_227",
        "Beacon_228",
        "Beacon_229",
        "Beacon_230",
        "Beacon_231",
        "Beacon_232",
        "Beacon_233",
        "Beacon_234",
        "Beacon_235",
        "Beacon_236",
        "Beacon_237",
        "Beacon_238",
        "Beacon_239",
        "Beacon_240",
    ],
    "Waiting II": [],
    "Checkout": [
        "Beacon_241",
        "Beacon_242",
        "Beacon_243",
        "Beacon_244",
        "Beacon_245",
        "Beacon_246",
        "Beacon_247",
        "Beacon_248",
        "Beacon_249",
        "Beacon_250",
        "Beacon_251",
        "Beacon_272",
    ],
    "Waiting III": [],
}

layout_for_indexing = {
    "region_name": [
        "Not in use",
        "Pre-checkin",
        "Checkin Main",
        "Doctor Table",
        "Vaccination",
        "Checkout",
    ],
    "beacons": [
        [
            "Beacon_201",
            "Beacon_202",
            "Beacon_203",
            "Beacon_258",
            "Beacon_259",
            "Beacon_260",
        ],
        [
            "Beacon_271",
            "Beacon_257",
            "Beacon_256",
            "Beacon_255",
            "Beacon_254",
            "Beacon_253",
        ],
        [
            "Beacon_205",
            "Beacon_204",
            "Beacon_206",
            "Beacon_207",
            "Beacon_208",
            "Beacon_209",
            "Beacon_210",
        ],
        [
            "Beacon_211",
            "Beacon_212",
            "Beacon_213",
            "Beacon_214",
            "Beacon_215",
            "Beacon_216",
            "Beacon_217",
            "Beacon_218",
            "Beacon_219",
            "Beacon_220",
        ],
        [
            "Beacon_221",
            "Beacon_222",
            "Beacon_223",
            "Beacon_224",
            "Beacon_225",
            "Beacon_226",
            "Beacon_227",
            "Beacon_228",
            "Beacon_229",
            "Beacon_230",
            "Beacon_231",
            "Beacon_232",
            "Beacon_233",
            "Beacon_234",
            "Beacon_235",
            "Beacon_236",
            "Beacon_237",
            "Beacon_238",
            "Beacon_239",
            "Beacon_240",
        ],
        [
            "Beacon_241",
            "Beacon_242",
            "Beacon_243",
            "Beacon_244",
            "Beacon_245",
            "Beacon_246",
            "Beacon_247",
            "Beacon_248",
            "Beacon_249",
            "Beacon_250",
            "Beacon_251",
            "Beacon_272",
        ],
    ],
}