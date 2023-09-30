import numpy as np
import pandas as pd
import json

# Opening JSON file
f = open('full_format_recipes.json')
j_data = json.load(f)

recipi_data =pd.DataFrame(j_data)
recipi_data.dropna(inplace=True)
importent_data = recipi_data[['title', 'calories', 'protein', 'rating', 'ingredients', 'fat', 'directions']]
cuisine_keywords = {
    'Italian': [
        'pizza', 'pasta', 'risotto', 'lasagna', 'gnocchi', 'spaghetti', 'cannoli',
        'calzone', 'panettone', 'tiramisu', 'osso buco', 'carbonara', 'cacciatore',
        'pesto', 'caprese', 'polenta', 'ricotta', 'prosciutto', 'bruschetta',
        'limoncello', 'tortellini', 'parmigiana', 'amaretto', 'taleggio', 'ciabatta',
        'focaccia', 'tagliatelle', 'cappuccino', 'marsala', 'straciatella', 'arancini',
        'minestrone', 'panna cotta', 'frittata', 'cacio e pepe', 'amaretti', 'canoli',
        'spumoni', 'biscotti', 'lasagne', 'cannelloni', 'vermicelli', 'mortadella',
        'burrata', 'tartufo', 'calamari', 'caponata', 'frutti di mare', 'limoncello',
        'affogato', 'gorgonzola', 'polpette', 'cioppino', 'marinara', 'zeppole',
        'capocollo', 'scampi', 'struffoli', 'pastina', 'ciacci', 'polpo', 'sbrisolona',
        'pandoro', 'piadina', 'taralli', 'angioletti', 'rosticceria', 'sorbetto',
        'frittelle', 'spaghetti alla chitarra', 'americano', 'risi e bisi',
        'salumi', 'cipollini', 'tarallucci', 'agnolotti', 'melanzane', 'porchetta',
        'verde', 'vitello', 'parmigiano', 'peperoncino', 'aragosta', 'bottarga',
        'bolognese', 'saltimbocca', 'ossobuco', 'limonata', 'pomodoro', 'gelato',
        'pancetta', 'panforte', 'pizzelle', 'zeppola', 'pizzoccheri', 'amaro'
    ],
    'Mexican': [
        'taco', 'burrito', 'enchilada', 'guacamole', 'salsa', 'quesadilla', 'churro',
        'nachos', 'tostada', 'flauta', 'tlayuda', 'chilaquiles', 'horchata',
        'elote', 'mole', 'chiles rellenos', 'sopes', 'pozole', 'tamales',
        'al pastor', 'carnitas', 'menudo', 'aguas frescas', 'cochinita pibil',
        'molletes', 'atole', 'salsa verde', 'salsa roja', 'nopalitos', 'birria',
        'huaraches', 'cebiche', 'chapulines', 'chapulín', 'escamoles', 'mezcal',
        'tequila', 'margarita', 'michelada', 'pulque', 'charro beans', 'tamarind',
        'birria de res', 'chayote', 'tostilocos', 'cacahuate', 'chocolate',
        'aguachile', 'carne asada', 'ceviche', 'cotija', 'hoja santa', 'mexicola',
        'chileatole', 'piloncillo', 'puebla', 'veracruz', 'chiapas', 'oaxaca',
        'hidalgo', 'yucatan', 'jalisco', 'sonora', 'sinaloa', 'nayarit', 'zacatecas',
        'aguascalientes', 'guanajuato', 'queretaro', 'tampico', 'chilango', 'monterrey',
        'coahuila', 'durango', 'zamora', 'guadalajara', 'chihuahua', 'parral',
        'sinaloa', 'culiacan', 'hermosillo', 'juarez', 'tijuana', 'mexicali',
        'nuevo laredo', 'monclova', 'laguna', 'reynosa', 'matamoros', 'piedras negras',
        'saltillo', 'torreon', 'monterrey', 'apodaca', 'san pedro', 'santa catarina',
        'guadalupe', 'nayarit', 'tepic', 'mazatlan', 'culiacan', 'los mochis',
        'hermosillo', 'ciudad obregon', 'juarez', 'oaxaca city', 'puebla city'
    ],
    'Asian': [
        'sushi', 'ramen', 'stir-fry', 'dim sum', 'sashimi', 'tempura', 'bao',
        'pho', 'bibimbap', 'pad thai', 'curry', 'satay', 'baozi', 'congee',
        'kimchi', 'sukiyaki', 'teriyaki', 'yakitori', 'kaiseki', 'miso soup',
        'goyza', 'udon', 'soba', 'takoyaki', 'matcha', 'nigiri', 'shabu shabu',
        'yuzu', 'wasabi', 'okonomiyaki', 'taiyaki', 'mochi', 'chirashi', 'unagi',
        'somen', 'shumai', 'pho bo', 'banh mi', 'bun cha', 'com tam', 'canh chua',
        'mi quang', 'ca kho to', 'bun thit nuong', 'cha gio', 'ca nuong',
        'com chien', 'cha ca', 'pho ga', 'goi cuon', 'hu tieu', 'nom hoa chuoi',
        'thit kho', 'bun bo hue', 'banh beo', 'banh xeo', 'che ba mau', 'che troi nuoc',
        'chao', 'mi hoanh thanh', 'ca phe', 'nuoc mia', 'ca phe sua da', 'nuoc chanh',
        'banh trang', 'goi', 'goi cuon', 'nuoc mam', 'goi du du', 'goi ngo sen',
        'goi tom', 'goi ga', 'cha lua', 'bo la lot', 'rau muong', 'com chay',
        'bun dau mam tom', 'nem ran', 'mi xao', 'bun mam', 'banh my', 'banh tet',
        'bun rieu', 'banh canh', 'banh bot loc', 'goi la', 'cari', 'hu tieu mi',
        'mi quang', 'bun bo nam bo', 'bun cha gio', 'bun thit nuong', 'ca ri ga',
        'banh xeo', 'banh trang tron', 'banh trang cuon', 'banh tam bi', 'oc xao dua'
    ],
    'Mediterranean': [
        'hummus', 'falafel', 'tabbouleh', 'shawarma', 'kebab', 'baba ganoush', 'spanakopita',
        'moussaka', 'baklava', 'tzatziki', 'souvlaki', 'dolma', 'kibbeh', 'manakish',
        'loukoumades', 'knafeh', 'fattoush', 'batata harra', 'kousa mahshi', 'foul medames',
        'muhammara', 'shanklish', 'mujadara', 'sambousek', 'zaatar', 'manti', 'börek',
        'lahmacun', 'mantu', 'kuymak', 'cacik', 'bamya', 'kısır', 'tarator', 'babaganoush',
        'maghmour', 'moutabal', 'turşu', 'kısır', 'acılı ezme', 'kumpir', 'ayran', 'çılbır',
        'duğun çorbası', 'hoşmerim', 'keşkül', 'lokma', 'menemen', 'midye', 'musakka',
        'pastirma', 'pide', 'serbet', 'simit', 'tavuk göğsü', 'taze fasulye', 'tutmac',
        'boza', 'iskembe', 'lakerda', 'mıhlama', 'tarator', 'biber dolması', 'ege usulu kozlenmis biber',
        'çılbır', 'soutzouk loukoum', 'taramosalata', 'yiouvetsi', 'fasolada', 'patsas', 'tsoureki',
        'rizogalo', 'melomakarona', 'pastitsio', 'galaktoboureko', 'kourabiedes', 'feta', 'olives', 'saganaki',
        'loukaniko', 'gemista', 'greek salad', 'avgolemono', 'tsatziki', 'souvlaki', 'spanakopita', 'baklava',
        'gyro', 'pastitsio', 'dolmades', 'melitzanosalata', 'kalamari', 'gemista', 'revithia', 'tirokafteri',
        'stifado', 'tzatziki', 'kleftiko', 'souzouk loukoum', 'choban salat', 'burek', 'crepes', 'kofta', 'pilaki',
        'mamaliga', 'karpouzopita', 'souvlaki', 'greek frappe', 'spanakorizo', 'kreatopita', 'kolokythokeftedes'
    ],
    'Turkish': [
        'doner kebab', 'kofte', 'pide', 'manti', 'borek', 'lentil soup', 'baklava', 'lokum', 'simit', 'kumpir',
        'hunkar begendi', 'iskender kebap', 'pilav', 'menemen', 'cig kofte', 'kuzu tandir', 'imam bayildi', 'biber dolma',
        'hamsi pilav', 'midye tava', 'balik ekmek', 'kabak cicegi dolmasi', 'tavuk kanat', 'gavurdaği salatasi',
        'tarator', 'acili ezme', 'mercimek kofte', 'sucuklu yumurta', 'mantar yahnisi', 'baliq murtu', 'peynirli pide',
        'kopoglu salat', 'sac kavurma', 'molehiya', 'ekmek kadayifi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik',
        'mantar kebap', 'bamya yemegi', 'mantar ciger', 'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma',
        'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir', 'kadin budu kofte', 'gullac',
        'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam',
        'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi',
        'perde pilavi', 'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir',
        'pogaca', 'kumpir', 'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote',
        'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma',
        'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva',
        'gullac', 'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme',
        'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'pide', 'sutlac',
        'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir', 'yogurt corbasi',
        'ayran', 'kabak cicegi dolmasi', 'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma',
        'kagit kebabi', 'mantar ciger', 'molehiya', 'pide', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi',
        'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi', 'soguk ayran',
        'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi', 'bezelye corbasi',
        'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi', 'tarator', 'patates kizartmasi',
        'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik', 'mantar kebap', 'bamya yemegi',
        'mantar ciger', 'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir',
        'kuzu tandir', 'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay',
        'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi',
        'perde pilavi', 'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir',
        'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap',
        'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi',
        'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva', 'gullac', 'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi',
        'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat',
        'pide', 'sutlac', 'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir', 'yogurt corbasi',
        'ayran', 'kabak cicegi dolmasi', 'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi',
        'mantar ciger', 'molehiya', 'pide', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi',
        'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi', 'soguk ayran', 'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi',
        'sakatat', 'perde pilavi', 'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi', 'tarator',
        'patates kizartmasi', 'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik', 'mantar kebap', 'bamya yemegi',
        'mantar ciger', 'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir',
        'kuzu tandir', 'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay', 'ayran',
        'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi',
        'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir', 'molehiya', 'pide',
        'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi',
        'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi',
        'pazili borek', 'lahmacun', 'kagit helva', 'gullac', 'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek',
        'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'pide', 'sutlac',
        'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir', 'yogurt corbasi', 'ayran', 'kabak cicegi dolmasi',
        'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi', 'mantar ciger', 'molehiya', 'pide',
        'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi',
        'kabak cicegi dolmasi', 'soguk ayran', 'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi',
        'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi', 'tarator', 'patates kizartmasi',
        'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik', 'mantar kebap', 'bamya yemegi', 'mantar ciger', 'peynirli borek',
        'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir', 'kadin budu kofte', 'gullac', 'sutlu nuriye',
        'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir',
        'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi', 'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir',
        'pogaca', 'kumpir', 'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi',
        'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva',
        'gullac', 'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran',
        'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'pide', 'sutlac', 'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir',
        'yogurt corbasi', 'ayran', 'kabak cicegi dolmasi', 'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi', 'mantar ciger',
        'molehiya', 'pide', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi',
        'soguk ayran', 'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi', 'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi',
        'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi', 'tarator', 'patates kizartmasi', 'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik',
        'mantar kebap', 'bamya yemegi', 'mantar ciger', 'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir',
        'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba',
        'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi', 'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir',
        'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte',
        'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva', 'gullac', 'cevizli sucuk',
        'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi',
        'corek otu salatasi', 'sakatat', 'pide', 'sutlac', 'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir', 'yogurt corbasi', 'ayran',
        'kabak cicegi dolmasi', 'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi', 'mantar ciger', 'molehiya', 'pide', 'sutlac',
        'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi', 'soguk ayran',
        'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi', 'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi',
        'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi', 'tarator', 'patates kizartmasi', 'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik',
        'mantar kebap', 'bamya yemegi', 'mantar ciger', 'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir',
        'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi', 'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba',
        'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi', 'kuzu tandir', 'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir',
        'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte',
        'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva', 'gullac', 'cevizli sucuk',
        'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi',
        'sakatat', 'pide', 'sutlac', 'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir', 'yogurt corbasi', 'ayran', 'kabak cicegi dolmasi',
        'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi', 'mantar ciger', 'molehiya', 'pide', 'sutlac', 'kaymak', 'sekerpare', 'lokma',
        'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi', 'soguk ayran', 'karnabahar kizartmasi', 'biber kizartma',
        'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi', 'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'ezogelin corbasi', 'yogurt corbasi',
        'tarator', 'patates kizartmasi', 'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik', 'mantar kebap', 'bamya yemegi', 'mantar ciger', 'peynirli borek',
        'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir', 'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi',
        'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi', 'kuzu tandir',
        'kagit helva', 'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir', 'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote',
        'kagit kebabi', 'iskender kebap', 'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi',
        'pazili borek', 'lahmacun', 'kagit helva', 'gullac', 'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi',
        'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'pide', 'sutlac', 'perde pilavi', 'kuzu tandir', 'tirit', 'tavuk sote', 'kagit kebabi', 'tavuk kanat', 'baharatli kuzu tandir',
        'yogurt corbasi', 'ayran', 'kabak cicegi dolmasi', 'baliq murtu', 'sakatat', 'kuzu tandir', 'bamya yemegi', 'kagit helva', 'soguk ayran', 'cigirtma', 'kagit kebabi', 'mantar ciger', 'molehiya', 'pide',
        'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap', 'lahmacun', 'pasa pilavi', 'balik ekmek', 'patates kizartmasi', 'kabak cicegi dolmasi', 'soguk ayran',
        'karnabahar kizartmasi', 'biber kizartma', 'kelle pacasi corbasi', 'corek otu salatasi', 'sakatat', 'perde pilavi', 'bezelye corbasi', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir',
        'ezogelin corbasi', 'yogurt corbasi', 'tarator', 'patates kizartmasi', 'zeytinyagli dolma', 'mercimek corbasi', 'kaygana', 'sogan kebap', 'kebapche', 'izgara balik', 'mantar kebap', 'bamya yemegi', 'mantar ciger',
        'peynirli borek', 'bulgur pilavi', 'patates salat', 'cigirtma', 'biber kizartma', 'pasa pilavi', 'baharatli kuzu tandir', 'kuzu tandir', 'kadin budu kofte', 'gullac', 'sutlu nuriye', 'sekerpare', 'kaymakli ekmek kadayifi',
        'sahlep', 'turk kahvesi', 'cay', 'ayran', 'salgam', 'karakoy gevrek', 'kagit helva', 'lokma', 'tulumba', 'kumpir', 'gevrek', 'tirit', 'tavuk sote', 'kagit kebabi', 'perde pilavi', 'kuzu tandir', 'kagit helva',
        'hunkar begendi', 'tarator', 'patates kizartmasi', 'kuzu tandir', 'pogaca', 'kumpir', 'molehiya', 'pide', 'doner', 'kuzu tandir', 'sutlac', 'kaymak', 'sekerpare', 'lokma', 'tavuk sote', 'kagit kebabi', 'iskender kebap',
        'karnabahar kizartmasi', 'pasa pilavi', 'cig kofte', 'mantar kebap', 'zeytinyagli dolma', 'mercimek corbasi', 'ezogelin corbasi', 'yogurt corbasi', 'turp otu salatasi', 'pazili borek', 'lahmacun', 'kagit helva', 'gullac',
        'cevizli sucuk', 'kabak cicegi dolmasi', 'mantar ciger', 'ali nazik kebabi', 'peynirli borek', 'boraniye', 'gozleme', 'perde pilavi', 'bezelye corbasi', 'soguk ayran', 'kelle pacasi corbasi', 'corek otu salatasi']
}
# Function to classify the titles into cuisine preferences
def classify_cuisine(title):
    for cuisine, keywords in cuisine_keywords.items():
        for keyword in keywords:
            if keyword in title.lower():
                return cuisine
    return 'other'  # Default value if no cuisine is matched

 # Apply the classification fu(nction to create the "Cuisine Preference" column

importent_data['title'] = importent_data['title'].astype(str)

importent_data['Cuisine Preference'] = importent_data['title'].apply(classify_cuisine)

# Print the resulting DataFrame
# print(merged_df)
importent_data['Cuisine Preference']

def dummy_function():
    # Print the resulting DataFrame
    # print(merged_df)
    grouped_data = importent_data.groupby('Cuisine Preference')
    Mexican = grouped_data.get_group('Mexican')
    Italian = grouped_data.get_group('Italian')
    Asian = grouped_data.get_group('Asian')
    Turkish = grouped_data.get_group('Turkish')
    Mediterranean =  grouped_data.get_group('Mediterranean')
    other = grouped_data.get_group('other')

    return Italian, Mexican, Asian, Turkish, Mediterranean, other