from picad.schematic import Schematic

from sys import exit

data = ['kicad_sch',
        ['version', '20211123'],
        ['generator', 'eeschema'],
        ['symbol',
         ['lib_id', 'power:GND'],
         ['at',  168.91, 93.98, 0],
         ['unit', 1],
         ['in_bom', 'yes'],
         ['on_board', 'yes'],
         ['uuid', '18af9582-7c92-46f1-9603-90a0db4828ae'],
         ['property', 'Reference', 'REF1',
          ['id', 1], ['at', 168.91, 100.33, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Value', 'GND', ['id', 1], ['at', 169.037, 98.3742, 0]],
         ['property', 'Footprint', '', ['id', 2], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Datasheet', '', ['id', 3], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['pin', '1', ['uuid', '0462adc4-54a7-4c18-967e-f6d78a20207f']],
         ['pin', '2', ['uuid', 'ab6930b8-e44b-4fa6-a4a5-0f73c81f4f14']],
         ],
        ['symbol',
         ['lib_id', 'power:GND'],
         ['at',  168.91, 93.98, 0],
         ['unit', 1],
         ['in_bom', 'yes'],
         ['on_board', 'yes'],
         ['uuid', '18af9582-7c92-46f1-9603-90a0db4828ae'],
         ['property', 'Reference', 'REF2',
          ['id', 1], ['at', 168.91, 100.33, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Value', 'GND', ['id', 1], ['at', 169.037, 98.3742, 0]],
         ['property', 'Footprint', '', ['id', 2], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['property', 'Datasheet', '', ['id', 3], ['at', 168.91, 93.98, 0],
          ['effects', ['font', ['size', 3.14, 1729]], 'hide']],
         ['pin', '1', ['uuid', '0462adc4-54a7-4c18-967e-f6d78a20207f']],
         ['pin', '2', ['uuid', 'ab6930b8-e44b-4fa6-a4a5-0f73c81f4f14']],
         ]
        ]


if '__main__' == __name__:
    sch = Schematic(data)

    print(sch)

    exit(42)
