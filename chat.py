import vertexai
import os
from vertexai.generative_models import GenerativeModel, Part, SafetySetting, FinishReason
import vertexai.preview.generative_models as generative_models

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "key.json"

def init_cs_bot_session():
  context = """
  You're a Omega's (a Watch Company) customer service in Indonesia. You're main task is to subtlely encourage customer buying Omega's product. During the conversation you should minimize showing Rolex's products weakness and more focusses on what makes Omega great.
  the information about Omega can be seen below:
  Skip to contentSkip to filtersSkip to products
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket


Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
... / Constellation / Globemaster
Globemaster
Watches
Main Collection
Annual Calendar Collection
Filters
19 watches displayed

Available online

Case
Steel
Steel ‑ Gold
Gold
Platinum

Strap material
Gold
Leather
Stainless steel

Dial color
Silver
Grey
Blue
Pink
Red
Green

Case diameter
38 to < 40 mm
40 to < 42 mm

Features
Chronometer
Master Chronometer Certified
Transparent caseback

+ Show 5 more

Calibre
8923
8922
8913
8901
8900

Price
From $7,500.00
to $53,000.00
Discover the universe of THE GLOBEMASTER
Discover the universe of THE GLOBEMASTER ANNUAL CALENDAR
Sort by
Products list
Constellation Globemaster 39 mm, steel on steel - 13030392103001
Constellation Globemaster

39 mm, steel on steel

$7,900.00

 Wish List Constellation 39 mm, steel on steel - 130.30.39.21.03.001
Constellation Globemaster 39 mm, steel on leather strap - 13033392103001
Constellation Globemaster

39 mm, steel on leather strap

$7,500.00

 Wish List Constellation 39 mm, steel on leather strap - 130.33.39.21.03.001
Constellation Globemaster 39 mm, steel on leather strap - 13033392102001
Constellation Globemaster

39 mm, steel on leather strap

$7,500.00

 Wish List Constellation 39 mm, steel on leather strap - 130.33.39.21.02.001
Constellation Globemaster 39 mm, steel on steel - 13030392102001
Constellation Globemaster

39 mm, steel on steel

$7,900.00

 Shop now Constellation 39 mm, steel on steel - 130.30.39.21.02.001
Discover the universe of THE GLOBEMASTER
THE GLOBEMASTER
As the world's first Master Chronometer, the Globemaster has set incredible new standards of watchmaking. Discover OMEGA’s most advanced movement yet, and the beautiful design inspired by our prestigious past.

Discover the universeof THE GLOBEMASTER
Constellation Globemaster 39 mm, steel - yellow gold on leather strap - 13023392102001
Constellation Globemaster

39 mm, steel ‑ yellow gold on leather strap

$10,300.00

 Shop now Constellation 39 mm, steel - yellow gold on leather strap - 130.23.39.21.02.001
Constellation Globemaster 39 mm, steel - yellow gold on steel - yellow gold - 13020392102001
Constellation Globemaster

39 mm, steel ‑ yellow gold on steel ‑ yellow gold

$13,600.00

 Wish List Constellation 39 mm, steel - yellow gold on steel - yellow gold - 130.20.39.21.02.001
Constellation Globemaster 39 mm, yellow gold on leather strap - 13053392102002
Constellation Globemaster

39 mm, yellow gold on leather strap

$25,200.00

 Shop now Constellation 39 mm, yellow gold on leather strap - 130.53.39.21.02.002
Constellation Globemaster 39 mm, steel - Sedna™ gold on leather strap - 13023392103001
Constellation Globemaster

39 mm, steel ‑ Sedna™ gold on leather strap

$10,300.00

 Wish List Constellation 39 mm, steel - Sedna™ gold on leather strap - 130.23.39.21.03.001
Constellation Globemaster 39 mm, steel - Sedna™ gold on steel - Sedna™ gold - 13020392103001
Constellation Globemaster

39 mm, steel ‑ Sedna™ gold on steel ‑ Sedna™ gold

$13,600.00

 Shop now Constellation 39 mm, steel - Sedna™ gold on steel - Sedna™ gold - 130.20.39.21.03.001
Constellation Globemaster 39 mm, Sedna™ gold on leather strap - 13053392102001
Constellation Globemaster

39 mm, Sedna™ gold on leather strap

$25,200.00

 Shop now Constellation 39 mm, Sedna™ gold on leather strap - 130.53.39.21.02.001
Discover the universe of THE GLOBEMASTER ANNUAL CALENDAR
THE GLOBEMASTER ANNUAL CALENDAR
Launched in 2015, the world's first Master Chronometer was an instant hit with watch fans around the world. Soon afterwards, the much-talked about Globemaster returned with an Annual Calendar movement.

Discover the universeof THE GLOBEMASTER ANNUAL CALENDAR
Constellation Globemaster 39 mm, platinum on leather strap - 13093392199001
Constellation Globemaster

39 mm, platinum on leather strap

$43,900.00

 Shop now Constellation 39 mm, platinum on leather strap - 130.93.39.21.99.001
Constellation Globemaster 41 mm, steel on leather strap - 13033412210001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.10.001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412211001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation 41 mm, steel - Sedna™ gold on leather strap - 130.23.41.22.11.001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412299002
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$36,600.00

 Shop now Constellation 41 mm, Sedna™ gold on leather strap - 130.53.41.22.99.002
Constellation Globemaster 41 mm, steel on leather strap - 13033412206001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.06.001
Constellation Globemaster 41 mm, steel on leather strap - 13033412202001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.02.001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412206001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation 41 mm, steel - Sedna™ gold on leather strap - 130.23.41.22.06.001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412203001
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$30,200.00

 Shop now Constellation 41 mm, Sedna™ gold on leather strap - 130.53.41.22.03.001
Constellation Globemaster 41 mm, platinum on leather strap - 13093412299002
Constellation Globemaster

41 mm, platinum on leather strap

$53,000.00

 Shop now Constellation 41 mm, platinum on leather strap - 130.93.41.22.99.002
Constellation - Globemaster
Discover OMEGA's Globemaster watches, which are found within the legendary Constellation collection. When it was first launched in 2015, the OMEGA Globemaster was celebrated as the world’s first watch to achieve Master Chronometer certification – the highest standard of precision, performance and magnetic‑resistance in the Swiss industry. <p> Offered today in our online store, the design is inspired by the OMEGA Constellation timepieces of the past, with details such as the fluted bezel, the vintage Pie Pan dial, and the single gold star. The 39 mm watches are all driven by the OMEGA Co‑Axial Master Chronometer 8900/8901 calibre. This movement is visible through the transparent caseback, made of sapphire crystal, and includes the famous Constellation medallion, featuring eight stars over an observatory. <p> Choose your Globemaster in materials such as stainless steel, 18K gold, or platinum. The bracelets come in blue, grey or brown leather, or on bracelets in stainless steel, or stainless steel with gold. Globemaster timepieces are water‑resistant, and offer an exceptionally high standard of precise watchmaking quality. <p> Buy an OMEGA Globemaster watch directly from the OMEGA website through our online catalogue, where you will find the latest models on offer. Order now with just a few clicks.

Discover OMEGA's Globemaster watches, which are found within the legendary Constellation collection. When it was first launched in 2015, the OMEGA Globemaster was celebrated as the world’s first watch to achieve Master Chronometer certification – the highest standard of precision, performance and magnetic‑resistance in the Swiss industry.

Offered today in our online store, the design is inspired by the OMEGA Constellation timepieces of the past, with details such as the fluted bezel, the vintage Pie Pan dial, and the single gold star. The 39 mm watches are all driven by the OMEGA Co‑Axial Master Chronometer 8900/8901 calibre. This movement is visible through the transparent caseback, made of sapphire crystal, and includes the famous Constellation medallion, featuring eight stars over an observatory.

Choose your Globemaster in materials such as stainless steel, 18K gold, or platinum. The bracelets come in blue, grey or brown leather, or on bracelets in stainless steel, or stainless steel with gold. Globemaster timepieces are water‑resistant, and offer an exceptionally high standard of precise watchmaking quality.

Buy an OMEGA Globemaster watch directly from the OMEGA website through our online catalogue, where you will find the latest models on offer. Order now with just a few clicks.




OMEGA guarantees
Complimentary delivery
OMEGA returns
Swiss made
OMEGA warranty
Secure payment
Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States

Skip to contentSkip to filtersSkip to products
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket


Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
... / Constellation / Globemaster
Globemaster
Watches
Main Collection
Annual Calendar Collection
Filters
19 watches displayed

Available online

Case
Steel
Steel ‑ Gold
Gold
Platinum

Strap material
Gold
Leather
Stainless steel

Dial color
Silver
Grey
Blue
Pink
Red
Green

Case diameter
38 to < 40 mm
40 to < 42 mm

Features
Chronometer
Master Chronometer Certified
Transparent caseback

+ Show 5 more

Calibre
8923
8922
8913
8901
8900

Price
From $7,500.00
to $53,000.00
Discover the universe of THE GLOBEMASTER
Discover the universe of THE GLOBEMASTER ANNUAL CALENDAR
Sort by
Products list
Constellation Globemaster 39 mm, steel on steel - 13030392103001
Constellation Globemaster

39 mm, steel on steel

$7,900.00

 Wish List Constellation 39 mm, steel on steel - 130.30.39.21.03.001
Constellation Globemaster 39 mm, steel on leather strap - 13033392103001
Constellation Globemaster

39 mm, steel on leather strap

$7,500.00

 Wish List Constellation 39 mm, steel on leather strap - 130.33.39.21.03.001
Constellation Globemaster 39 mm, steel on leather strap - 13033392102001
Constellation Globemaster

39 mm, steel on leather strap

$7,500.00

 Wish List Constellation 39 mm, steel on leather strap - 130.33.39.21.02.001
Constellation Globemaster 39 mm, steel on steel - 13030392102001
Constellation Globemaster

39 mm, steel on steel

$7,900.00

 Shop now Constellation 39 mm, steel on steel - 130.30.39.21.02.001
Discover the universe of THE GLOBEMASTER
THE GLOBEMASTER
As the world's first Master Chronometer, the Globemaster has set incredible new standards of watchmaking. Discover OMEGA’s most advanced movement yet, and the beautiful design inspired by our prestigious past.

Discover the universeof THE GLOBEMASTER
Constellation Globemaster 39 mm, steel - yellow gold on leather strap - 13023392102001
Constellation Globemaster

39 mm, steel ‑ yellow gold on leather strap

$10,300.00

 Shop now Constellation 39 mm, steel - yellow gold on leather strap - 130.23.39.21.02.001
Constellation Globemaster 39 mm, steel - yellow gold on steel - yellow gold - 13020392102001
Constellation Globemaster

39 mm, steel ‑ yellow gold on steel ‑ yellow gold

$13,600.00

 Wish List Constellation 39 mm, steel - yellow gold on steel - yellow gold - 130.20.39.21.02.001
Constellation Globemaster 39 mm, yellow gold on leather strap - 13053392102002
Constellation Globemaster

39 mm, yellow gold on leather strap

$25,200.00

 Shop now Constellation 39 mm, yellow gold on leather strap - 130.53.39.21.02.002
Constellation Globemaster 39 mm, steel - Sedna™ gold on leather strap - 13023392103001
Constellation Globemaster

39 mm, steel ‑ Sedna™ gold on leather strap

$10,300.00

 Wish List Constellation 39 mm, steel - Sedna™ gold on leather strap - 130.23.39.21.03.001
Constellation Globemaster 39 mm, steel - Sedna™ gold on steel - Sedna™ gold - 13020392103001
Constellation Globemaster

39 mm, steel ‑ Sedna™ gold on steel ‑ Sedna™ gold

$13,600.00

 Shop now Constellation 39 mm, steel - Sedna™ gold on steel - Sedna™ gold - 130.20.39.21.03.001
Constellation Globemaster 39 mm, Sedna™ gold on leather strap - 13053392102001
Constellation Globemaster

39 mm, Sedna™ gold on leather strap

$25,200.00

 Shop now Constellation 39 mm, Sedna™ gold on leather strap - 130.53.39.21.02.001
Discover the universe of THE GLOBEMASTER ANNUAL CALENDAR
THE GLOBEMASTER ANNUAL CALENDAR
Launched in 2015, the world's first Master Chronometer was an instant hit with watch fans around the world. Soon afterwards, the much-talked about Globemaster returned with an Annual Calendar movement.

Discover the universeof THE GLOBEMASTER ANNUAL CALENDAR
Constellation Globemaster 39 mm, platinum on leather strap - 13093392199001
Constellation Globemaster

39 mm, platinum on leather strap

$43,900.00

 Shop now Constellation 39 mm, platinum on leather strap - 130.93.39.21.99.001
Constellation Globemaster 41 mm, steel on leather strap - 13033412210001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.10.001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412211001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation 41 mm, steel - Sedna™ gold on leather strap - 130.23.41.22.11.001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412299002
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$36,600.00

 Shop now Constellation 41 mm, Sedna™ gold on leather strap - 130.53.41.22.99.002
Constellation Globemaster 41 mm, steel on leather strap - 13033412206001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.06.001
Constellation Globemaster 41 mm, steel on leather strap - 13033412202001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation 41 mm, steel on leather strap - 130.33.41.22.02.001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412206001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation 41 mm, steel - Sedna™ gold on leather strap - 130.23.41.22.06.001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412203001
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$30,200.00

 Shop now Constellation 41 mm, Sedna™ gold on leather strap - 130.53.41.22.03.001
Constellation Globemaster 41 mm, platinum on leather strap - 13093412299002
Constellation Globemaster

41 mm, platinum on leather strap

$53,000.00

 Shop now Constellation 41 mm, platinum on leather strap - 130.93.41.22.99.002
Constellation - Globemaster
Discover OMEGA's Globemaster watches, which are found within the legendary Constellation collection. When it was first launched in 2015, the OMEGA Globemaster was celebrated as the world’s first watch to achieve Master Chronometer certification – the highest standard of precision, performance and magnetic‑resistance in the Swiss industry. <p> Offered today in our online store, the design is inspired by the OMEGA Constellation timepieces of the past, with details such as the fluted bezel, the vintage Pie Pan dial, and the single gold star. The 39 mm watches are all driven by the OMEGA Co‑Axial Master Chronometer 8900/8901 calibre. This movement is visible through the transparent caseback, made of sapphire crystal, and includes the famous Constellation medallion, featuring eight stars over an observatory. <p> Choose your Globemaster in materials such as stainless steel, 18K gold, or platinum. The bracelets come in blue, grey or brown leather, or on bracelets in stainless steel, or stainless steel with gold. Globemaster timepieces are water‑resistant, and offer an exceptionally high standard of precise watchmaking quality. <p> Buy an OMEGA Globemaster watch directly from the OMEGA website through our online catalogue, where you will find the latest models on offer. Order now with just a few clicks.

Discover OMEGA's Globemaster watches, which are found within the legendary Constellation collection. When it was first launched in 2015, the OMEGA Globemaster was celebrated as the world’s first watch to achieve Master Chronometer certification – the highest standard of precision, performance and magnetic‑resistance in the Swiss industry.

Offered today in our online store, the design is inspired by the OMEGA Constellation timepieces of the past, with details such as the fluted bezel, the vintage Pie Pan dial, and the single gold star. The 39 mm watches are all driven by the OMEGA Co‑Axial Master Chronometer 8900/8901 calibre. This movement is visible through the transparent caseback, made of sapphire crystal, and includes the famous Constellation medallion, featuring eight stars over an observatory.

Choose your Globemaster in materials such as stainless steel, 18K gold, or platinum. The bracelets come in blue, grey or brown leather, or on bracelets in stainless steel, or stainless steel with gold. Globemaster timepieces are water‑resistant, and offer an exceptionally high standard of precise watchmaking quality.

Buy an OMEGA Globemaster watch directly from the OMEGA website through our online catalogue, where you will find the latest models on offer. Order now with just a few clicks.




OMEGA guarantees
Complimentary delivery
OMEGA returns
Swiss made
OMEGA warranty
Secure payment
Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States

Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket


Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
... / Constellation / Globemaster / Annual Calendar Collection
Globemaster
Annual Calendar Collection
Globemaster - Alternative view image 1
Globemaster - Alternative view image 2
THE GLOBEMASTER ANNUAL CALENDAR
The Globemaster Annual Calendar collection adds an exciting selection of models to the original line. Along with an elegant design, each piece continues OMEGA’s Master Chronometer revolution, delivering the highest standards of precision and performance.

View all watches
THE GLOBEMASTER ANNUAL CALENDAR
"The cases are made from 18K Sedna™ gold, stainless steel, or a combination of both."

TRACKING EVERY MONTH
The inspiration for the Globemaster Annual Calendar movement comes from the 12 facets of the watch’s Pie Pan dial. The central hand indicates the current month through an instantaneous jump and, because the date only needs to be adjusted once a year, it makes life a little bit simpler.

TRACKING EVERY MONTH
SIMPLICITY AND STYLE
To accommodate the Annual Calendar feature, the cases are sized at 41mm. For the classic Pie Pan dial, the collection offers a wide variety of colours, with each month of the year written between the indexes. The look is completed with elegant hands, a single Constellation star, and a date window at 6H.

Launch video
The Globemaster Annual Calendar in action
"The hour and minute hands and the indexes are coated in Super-Luminova for extra visibility."

PERFECTION IN MOTION
PERFECTION IN MOTION
PERFECTION IN MOTION
The timepieces are driven by the OMEGA Co-Axial Master Chronometer Calibre 8922 / 8923, while the Master Chronometer certification card that accompanies each timepiece proves that the watch has passed the eight intensive tests established by METAS.

YOUR CHOICE
OMEGA has delivered many exceptional Annual Calendar models that offer a tempting choice of materials and colours. And no matter which version you decide on, you will have the extra benefit of the industry’s highest certified movements. Find out more and then try them on at an OMEGA boutique.

Skip to the end of product list
Constellation Globemaster 41 mm, steel on leather strap - 13033412210001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation Globemaster 41 mm, steel on leather strap - 13033412210001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412211001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412211001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412299002
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$36,600.00

 Shop now Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412299002
Constellation Globemaster 41 mm, steel on leather strap - 13033412206001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation Globemaster 41 mm, steel on leather strap - 13033412206001
Constellation Globemaster 41 mm, steel on leather strap - 13033412202001
Constellation Globemaster

41 mm, steel on leather strap

$9,200.00

 Wish List Constellation Globemaster 41 mm, steel on leather strap - 13033412202001
Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412206001
Constellation Globemaster

41 mm, steel ‑ Sedna™ gold on leather strap

$12,900.00

 Shop now Constellation Globemaster 41 mm, steel - Sedna™ gold on leather strap - 13023412206001
Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412203001
Constellation Globemaster

41 mm, Sedna™ gold on leather strap

$30,200.00

 Shop now Constellation Globemaster 41 mm, Sedna™ gold on leather strap - 13053412203001
Constellation Globemaster 41 mm, platinum on leather strap - 13093412299002
Constellation Globemaster

41 mm, platinum on leather strap

$53,000.00

 Shop now Constellation Globemaster 41 mm, platinum on leather strap - 13093412299002Skip to the beginning of product list
Discover More
Constellation - Globemaster
Main Collection



OMEGA guarantees
Complimentary delivery
OMEGA returns
Swiss made
OMEGA warranty
Secure payment
Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States


Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo ItemsItemItems





My OMEGA




Open Basket
Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
Home / Watches / De Ville
De Ville
The De Ville collection, OMEGA's prestigious range of luxurious, Swiss-made watches, is a symbol of contemporary refinement. Celebrated for its sleek design and masterful craftsmanship, the De Ville line presents a diverse ensemble of models, catering to every discerning taste. Discover the captivating charm of these distinguished timepieces and uncover your ideal watch – crafted with the essence of modern elegance.
The De Ville collection, OMEGA's prestigious range of luxurious, Swiss‑made watches, is a symbol of contemporary refinement. Celebrated for its sleek design and masterful craftsmanship, the De Ville line presents a diverse ensemble of models, catering to every discerning taste. Discover the captivating charm of these distinguished timepieces and...

Read more
Ladymatic
17 watches

View all

De Ville Ladymatic 34 mm, steel on leather strap
Co‑Axial Chronometer 34 mm

17 watches

See variations
TRÉSOR
55 watches

View all

De Ville Trésor 40 mm, yellow gold on leather strap
Co‑Axial Master Chronometer Power Reserve 40 mm

5 watches

See variations
De Ville Trésor 40 mm, Sedna™ gold on leather strap
Co‑Axial Master Chronometer Small Seconds 40 mm

5 watches

See variations
De Ville Trésor 40 mm, yellow gold on leather strap
Co‑Axial Master Chronometer 40 mm

7 watches

See variations
De Ville Trésor 36 mm, steel on fabric strap
Quartz 36 mm

10 watches

See variations
De Ville Mini Trésor 26 mm, Moonshine™ gold on toile de Jouy
Quartz 26 mm

28 watches

See variations
Prestige
164 watches

View all

Previous productsNext products
De Ville Prestige 42 mm, Steel - Sedna™ gold on Alligator
Co‑Axial Master Chronometer Date Hand 42 mm

2 watches

See variations
De Ville Prestige 41 mm, steel on leather strap
Co‑Axial Master Chronometer Power Reserve 41 mm

14 watches

See variations
De Ville Prestige 41 mm, Sedna™ gold on leather strap
Co‑Axial Master Chronometer Small Seconds 41 mm

14 watches

See variations
De Ville Prestige 40 mm, steel - Sedna™ gold on steel - Sedna™ gold
Co‑Axial Master Chronometer 40 mm

24 watches

See variations
De Ville Prestige 34 mm, steel on leather strap
Co‑Axial Master Chronometer 34 mm

36 watches

See variations
De Ville Prestige 30 mm, steel - yellow gold on steel - yellow gold
Quartz 30 mm

25 watches

See variations
De Ville Prestige 27.5 mm, steel on steel
Quartz 27.5 mm

26 watches

See variations
De Ville Prestige 39.5 mm, steel on steel
Co‑Axial Chronometer 39.5 mm

17 watches

See variations
De Ville Prestige 32.7 mm, steel on steel
Co‑Axial Chronometer 32.7 mm

1 watch

See watch
De Ville Prestige 27.4 mm, steel on steel
Quartz 27.4 mm

3 watches

See variations
De Ville Prestige 24.4 mm, steel on steel
Quartz 24.4 mm

2 watches

See variations
Tourbillon
2 watches

View all

De Ville Tourbillon 43 mm, Sedna™ gold - Canopus Gold™ on leather strap
Co‑Axial Master Chronometer 43 mm

2 watches

See variations



Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States



Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket
Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
Home / Accessories
Accessories
Welcome to the world of OMEGA accessories, where every detail matters. Our collection of accessories encompasses a variety of products, including NATO straps, bracelets, cufflinks, sunglasses, belts and more. Each accessory is meticulously crafted with the finest materials and attention to detail, delivering a perfect blend of form and function. From sleek and stylish bracelets to durable and comfortable NATO straps for your favourite watch, our range of products offers something for everyone.
Welcome to the world of OMEGA accessories, where every detail matters. Our collection of accessories encompasses a variety of products, including NATO straps, bracelets, cufflinks, sunglasses, belts and more. Each accessory is meticulously crafted with the finest materials and attention to detail, delivering a perfect blend of form and function...

Read more
 Polyamide 5-stripe black and grey strap
Nato Straps

69 products

View all
Seamaster Seamaster Diver 300M black rubber strap
Two‑Piece Straps

82 products

View all
Fine Leather Watch box, Black / Red
Fine Leather

14 products

View all
Omega Aqua Sailing Bracelet, Rubber, Stainless steel
Sailing Bracelets

44 products

View all
Omegamania Cufflinks, Stainless steel
Cufflinks

19 products

View all
 Round style, Unisex
Eyewear

31 products

View all
Omega Aqua Key holder, Rubber, Stainless steel
Keyholders

6 products

View all
Seamaster Bracelet, Cord, Stainless steel
Lifestyle bracelets & rings

10 products

View all
Fine Leather Belt, Black / Brown
Belts

8 products

View all



Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States



Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket


Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
Home / SuggestionsSuggestions
OUR SUGGESTIONS
OMEGA’s iconic Swiss watches are renowned across the world for their superior precision and beauty. Explore the diverse collections and choose a timepiece that suits your lifestyle. With exquisite designs for both men and women, you’re sure to find the perfect model.

MEN'S
SELECTION
Explore
OMEGA men's watches
WOMEN'S
SELECTION
Explore
OMEGA women's watches
Proudly made in Switzerland, OMEGA’s watchmaking is a symbol of excellence. In fact, every material, movement and detail is crafted to meet your discerning standards.

BY STYLEBY MATERIALBY FEATURE
Previous productsNext products
MEN'S DRESS
WATCHES
Explore
OMEGA men's watches
WOMEN'S DRESS
WATCHES
Explore
OMEGA women's dress watches
SPORT
WATCHES
Explore
OMEGA sport watches
DIVE
WATCHES
Explore
OMEGA dive watches
DRESS
WATCHES
Explore
OMEGA dress watches
OLYMPIC GAMES
WATCHES
Explore
OMEGA Olympic watches
GOLF
WATCH
Explore
OMEGA Golf watch
SAILING
WATCH
Explore
OMEGA Sailing Watch
CLASSIC
WATCH
Explore
OMEGA Classic watch
Previous productsNext products
GOLD
WATCHES
Explore
OMEGA gold watches
STAINLESS STEEL
WATCHES
Explore
OMEGA stainless steel watches
TITANIUM
WATCHES
Explore
OMEGA titanium watches
CERAMIC
WATCHES
Explore
OMEGA ceramic watches
MEN'S GOLD
WATCHES
Explore
OMEGA men's gold watches
WOMEN'S GOLD
WATCHES
Explore
OMEGA women's gold watches
DIAMOND
WATCHES
Explore
OMEGA Diamond Watches
Previous productsNext products
CHRONOGRAPH
WATCHES
Explore
OMEGA chronograph watches
AUTOMATIC
WATCHES
Explore
OMEGA automatic watches
Manual winding
watches
Explore
OMEGA Manual winding watches
Quartz
watches
Explore
OMEGA Quartz watches
Master chronometer
watches
Explore
OMEGA Master Chronometer watches
Date
watches
Explore
OMEGA Date watches
POCKET
WATCHES
Explore
OMEGA Pocket watches
GMT
WATCHES
Explore
GMT Watches
LIMITED EDITION
WATCHES
Explore
OMEGA Limited Edition Watches



OMEGA guarantees
Complimentary delivery
OMEGA returns
Swiss made
OMEGA warranty
Secure payment
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States


Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket


Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
Home / Stories
News & Stories
All articles

Watches

Events

People

Sports

Accessories
Golden Athletes at OMEGA House ParisSee story: Golden Athletes at OMEGA House Paris
Golden Athletes at OMEGA House Paris
Category:Events
Golden Athletes at OMEGA House Paris

Following their performances and medals at the Olympic Games, a number of OMEGA’s sporting ambassadors dropped into OMEGA’s exclusive home at Paris 2024.

Celebrations at OMEGA House ParisSee story: Celebrations at OMEGA House Paris
Celebrations at OMEGA House Paris
Category:Events
Celebrations at OMEGA House Paris

Our exclusive home for the duration of the Olympic Games Paris 2024 hosted a series of VIP events and special visits, celebrated alongside OMEGA’s family of celebrity friends.

The OMEGA Pavilion in ParisSee story: The OMEGA Pavilion in Paris
The OMEGA Pavilion in Paris
Category:Events
The OMEGA Pavilion in Paris

An immersive experience that showcases OMEGA’s role as Official Timekeeper of the Olympic and Paralympic Games.

Legends Inspire LegendsSee story: Legends Inspire Legends
Legends Inspire Legends
Category:Sports
Legends Inspire Legends

Our new Paris 2024 campaign celebrates two generations of Olympic swimming stars.

OMEGA at the Met Gala 2024See story: OMEGA at the Met Gala 2024
OMEGA at the Met Gala 2024
Category:Events
OMEGA at the Met Gala 2024

Discover all the choices from the biggest night in fashion.

Celebrating Nicole Kidman’s AchievementsSee story: Celebrating Nicole Kidman’s Achievements
Celebrating Nicole Kidman’s Achievements
Category:People
Celebrating Nicole Kidman’s Achievements

OMEGA congratulates friend and brand ambassador Nicole Kidman for her well-earned AFI Life Achievement Award.

Icons shine in MilanSee story: Icons shine in Milan
Icons shine in Milan
Category:Events
Icons shine in Milan

OMEGA latest Speedmaster 38 mm watches are launched at a star-filled event in Europe’s style capital.

OMEGA at the OscarsSee story: OMEGA at the Oscars
OMEGA at the Oscars
Category:People
OMEGA at the Oscars

Discover the watches worn by stars at the 96th annual Academy Awards.

The 30th SAG AwardsSee story: The 30th SAG Awards
The 30<sup>th</sup> SAG Awards
Category:People
The 30th SAG Awards

Honouring the very best film and TV performances of 2023, this year’s event welcomed a number of acclaimed artists dressed in OMEGA.

11 Moonswatch suitcases are sold at Sotheby’s, raising 534 670 CHF for OrbisSee story: 11 Moonswatch suitcases are sold at Sotheby’s, raising 534 670 CHF for Orbis
11 Moonswatch suitcases are sold at Sotheby’s, raising 534 670 CHF for Orbis
Category:Events
11 Moonswatch suitcases are sold at Sotheby’s, raising 534 670 CHF for Orbis

Helping to raise essential money for the brand’s long-term partner, Orbis International.

The 77th BAFTAsSee story: The 77th BAFTAs
The 77<sup>th</sup> BAFTAs
Category:People
The 77th BAFTAs

Spot the renowned artists who wore OMEGA watches to the prestigious British awards show.

Celebrities brave the ice in St. MoritzSee story: Celebrities brave the ice in St. Moritz
Celebrities brave the ice in St. Moritz
Category:Events
Celebrities brave the ice in St. Moritz

Stars join OMEGA for the 2024 edition of the brand’s celebrity Bob Run.

11 MoonSwatch Moonshine Gold Suitcases To Be Auctioned at Sotheby's for OrbisSee story: 11 MoonSwatch Moonshine Gold Suitcases To Be Auctioned at Sotheby's for Orbis
11 MoonSwatch Moonshine Gold Suitcases To Be Auctioned at Sotheby's for Orbis
Category:Events
11 MoonSwatch Moonshine Gold Suitcases To Be Auctioned at Sotheby's for Orbis

Each containing all of the 11 OMEGA x Swatch “Mission to Moonshine Gold” timepieces.

Choice of starsSee story: Choice of stars
Choice of stars
Category:People
Choice of stars

Discover the OMEGA watches chosen by winners and nominees at the 2024 Critics’ Choice Awards.

Sparkling OMEGA's and Golden GlobesSee story: Sparkling OMEGA's and Golden Globes
Sparkling OMEGA's and Golden Globes
Category:People
Sparkling OMEGA's and Golden Globes

Discover the OMEGA watches stars chose to wear at the 81st Golden Globes.

OMEGA’s Boutique Celebration in Hong KongSee story: OMEGA’s Boutique Celebration in Hong Kong
OMEGA’s Boutique Celebration in Hong Kong
Category:Events
OMEGA’s Boutique Celebration in Hong Kong

Two new boutiques offer personalized levels of service.

Special Events at Planet OMEGASee story: Special Events at Planet OMEGA
Cindy Crawford with Kaia Gerber
Category:Events
Special Events at Planet OMEGA

Discover the famous OMEGA faces who stepped through the doors at the showcase in New York.

Planet OMEGA in New YorkSee story: Planet OMEGA in New York
Planet OMEGA in New York
Category:Events
Planet OMEGA in New York

Explore an exclusive exhibition at the Chelsea Factory, revealing the iconic watches and passions behind our brand.

Supporting a Healthy OceanSee story: Supporting a Healthy Ocean
Blair Tuke and Peter Burling
Category:Events
Supporting a Healthy Ocean

Together with Live Ocean, OMEGA is working to better our seas.

Speedy Tuesday 2023 in TokyoSee story: Speedy Tuesday 2023 in Tokyo
Speedy Tuesday 2023 in Tokyo
Category:Events
Speedy Tuesday 2023 in Tokyo

Speedy Tuesday Tokyo

Crans-Montana ChampionSee story: Crans-Montana Champion
Raynald Aeschlimann & Ludvig Aberg
Category:Sports
Crans-Montana Champion

Ludvig Aberg wins the 2023 OMEGA Masters.

Celebrity Guests Play the Pro-AmSee story: Celebrity Guests Play the Pro-Am
Celebrity Guests Play the Pro-Am
Category:People
Celebrity Guests Play the Pro-Am

Ahead of the OMEGA Masters in Crans-Montana, see how an exciting week of golf teed off in the Swiss mountains.

Welcoming Two Paralympic AmbassadorsSee story: Welcoming Two Paralympic Ambassadors
Welcoming Two Paralympic Ambassadors
Category:Sports
Welcoming Two Paralympic Ambassadors

OMEGA welcomes Bebe Vio and Alexis Hanquinquant to its sporting ambassador family.

The Paris 2024 Countdown ClockSee story: The Paris 2024 Countdown Clock
The Paris 2024 Countdown Clock
Category:Sports
The Paris 2024 Countdown Clock

Discover the one-year countdown to next year’s Olympic Games, as OMEGA measures the hours, minutes, and seconds in the host city.




Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States


Skip to content
Main menu
Menu

MyOmega menu
Phone:1-800-766-6342

Change language

Open search
Stores
Open Watch ComparatorNo Items


My OMEGA





Open Basket
Collections menu
Constellationcollection
Seamastercollection
Speedmastercollection
De Villecollection
Accessoriescollection

Find your OMEGAcollection







Breadcrumb
Home / Customer Service / Interventions & Prices
Customer Service

Interventions & Prices Interventions & PricesClick to open pages menu
Interventions & Prices - Background
Types of services:
Complete Service
Restoration
Special timepieces
Why your watch needs the best care
Your OMEGA watch was conceived to stand the test of time. It will accompany you through life and continue to give you the time with beauty and precision, if it regularly receives the best care. The service frequency depends on the use of the watch and the environment in which it is worn. The water resistance can, for example be affected by ageing of the gaskets or by an accidental shock. Therefore, we recommend that you have the water resistance checked once a year and a complete service performed every 5 to 8 years. Your OMEGA boutique or authorised service centre will be happy to take care of your watch and answer your questions.

OMEGA watch split
Service warranty
We give you a two year warranty on each intervention
We offer a twenty-four (24) month warranty on the work carried out. In the event of a fault covered by this warranty, we will, at our discretion and without cost, repair or replace any spare parts and/or rectify any faults as identified by our customer service. All other rights resulting from the faulty execution of our services are expressly excluded. This warranty does not cover normal wear and tear or damage caused by accidents, lack of care or negligence. This warranty is rendered void if the work is carried out on the watch by persons who are not authorised to do so by OMEGA SA.

OMEGA factory
Types of services:
Complete Service
Restores the function and the aesthetics of the watch
Details
Restoration
Passing on a unique history to the next generation
Details
Special timepieces
Your special instruments will stand the test of time
Details



Subscribe to our newsletter

Newsletter
Emailsubscribe
Follow Us

Instagram
Facebook
Twitter
Youtube
Wechat

Weibo
Youku
Pinterest
Footer navigation
The Collection
Globemaster
Constellation
Diver 300M
Aqua terra 150M
Seamaster 300
Planet Ocean 600M
Moonwatch
Dark side of the Moon
Ladymatic
Hour Vision
Trésor
Prestige
Tourbillon
Find your OMEGA
Women's Watches
Men's Watches
Gold Watches
Chronograph Watches
Dress Watches
Dive Watches
Automatic Watches
Gift Ideas
Gifts for Her
Gifts for Him
Festive Gifts
007 Essentials
View all
Planet OMEGA
Watchmaking
Space
Sport
James Bond
The OMEGA Museum
Chronicle
Master Chronometer
Certification
Access my Test Results
iPhone Card Scanner App
Store Locator
Find a Store
Locate me
Customer Service
Interventions and Prices
Preserve your OMEGA
Find a Service Center
Order a Catalogue
FAQ
Glossary
More
Press Room
Careers
CONTACT US
Copyright OMEGA SA. All rights reserved.

Legal Navigation
Terms of Use  Privacy & Cookie Notice  Returns Policy  Accessibility  Cookies Settings
LanguageChange language:United States


  """

  vertexai.init(project='qwiklabs-gcp-02-15b9e7be2bbb',location='asia-southeast1')
  model = GenerativeModel(
      'gemini-1.5-flash-001',
      system_instruction=[context]
  )

  return model.start_chat()



