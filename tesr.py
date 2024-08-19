# gender = 1
# distance = 1000
# style = 1
# points = 1

import math


def get_coefficient(distance, gender, style):
    a = b = c = d = 0
    if distance == 1000 and gender == 1 and style == 1:
        a = -0.00000000040332837490
        b = 0.00000030276556792696
        c = 0.00288739845070762335
        d = 4.76587148076811217834
    elif distance == 1000 and gender == 1 and style == 2:
        a = -0.00000000031080456901
        b = 0.00000008985181435689
        c = 0.00269615578518922483
        d = 4.69994681935375524517
    elif distance == 1000 and gender == 2 and style == 1:
        a = -0.00000000032321443172
        b = 0.00000022435516849428
        c = 0.00254234328059577130
        d = 4.23852563576750185348
    elif distance == 1000 and gender == 2 and style == 2:
        a = -0.00000000028841342866
        b = 0.00000016643462803626
        c = 0.00224768782652651211
        d = 4.14945310729575567166
    # 2 км
    elif distance == 2000 and gender == 1 and style == 1:
        a = -0.00000000040129473910
        b = 0.00000029825033524920
        c = 0.00289041699739422953
        d = 4.71029300939881068189
    elif distance == 2000 and gender == 1 and style == 2:
        a = -0.00000000028436987599
        b = 0.00000003080397229676
        c = 0.00271889154265259059
        d = 4.63323612430616549318
    elif distance == 2000 and gender == 2 and style == 1:
        a = -0.00000000032785870831
        b = 0.00000023684182806562
        c = 0.00253493978719299129
        d = 4.18716218559119113252
    elif distance == 2000 and gender == 2 and style == 2:
        a = -0.00000000029313980354
        b = 0.00000018044580507603
        c = 0.00223879330415588385
        d = 4.08402614940763442064
    # 3 км
    elif distance == 3000 and gender == 1 and style == 1:
        a = -0.00000000039903779781
        b = 0.00000029129680475647
        c = 0.00289689421811423209
        d = 4.65956756772604308026
    elif distance == 3000 and gender == 1 and style == 2:
        a = -0.00000000028462540785
        b = 0.00000003142598577329
        c = 0.00272053842935515711
        d = 4.57192157001939847305
    elif distance == 3000 and gender == 2 and style == 1:
        a = -0.00000000032600162677
        b = 0.00000023179128840986
        c = 0.00253908450966000565
        d = 4.13900261678982417379
    elif distance == 3000 and gender == 2 and style == 2:
        a = -0.00000000028850376090
        b = 0.00000016818269430959
        c = 0.00224806185303005890
        d = 4.02182209652085020934
    # 5 км
    elif distance == 5000 and gender == 1 and style == 1:
        a = -0.00000000039976675655
        b = 0.00000029339679535976
        c = 0.00289765649115225621
        d = 4.56947023427287035702
    elif distance == 5000 and gender == 1 and style == 2:
        a = -0.00000000028234857141
        b = 0.00000002621634973064
        c = 0.00272565129701041187
        d = 4.46404558868374579106
    elif distance == 5000 and gender == 2 and style == 1:
        a = -0.00000000032703291611
        b = 0.00000023445978268415
        c = 0.00253950097178390344
        d = 4.05418097062892002214
    elif distance == 5000 and gender == 2 and style == 2:
        a = -0.00000000028987057733
        b = 0.00000017204087917277
        c = 0.00224799329285263472
        d = 3.91359351925925125215
    # 7.5 км
    elif distance == 7500 and gender == 1 and style == 1:
        a = -3.9752051005 * 10 ** -10
        b = 2.8817732014119 * 10 ** -7
        c = 0.00290264860321243212
        d = 4.47405824283225683757
    elif distance == 7500 and gender == 1 and style == 2:
        a = -2.8223479713 * 10 ** -10
        b = 2.617998852601 * 10 ** -7
        c = 0.00272849261697549750
        d = 4.34973429655212839862
    elif distance == 7500 and gender == 2 and style == 1:
        a = -3.2575530776 * 10 ** -10
        b = 2.3127059432435 * 10 ** -7
        c = 0.00254354935040268515
        d = 3.96381789138685292073
    elif distance == 7500 and gender == 2 and style == 2:
        a = -2.8908196858 * 10 ** -10
        b = 1.7016271233088 * 10 ** -7
        c = 0.00225196380146308606
        d = 3.79863359052491489365
    # 10 км
    elif distance == 10000 and gender == 1 and style == 1:
        a = -0.00000000039737049290
        b = 0.00000028796292011503
        c = 0.00290459678419474621
        d = 4.39330355391371085716
    elif distance == 10000 and gender == 1 and style == 2:
        a = -0.00000000031051904584
        b = 0.00000009247423586383
        c = 0.00270061692503253958
        d = 4.25469528407158747996
    elif distance == 10000 and gender == 2 and style == 1:
        a = -0.00000000032549068534
        b = 0.00000023064396415299
        c = 0.00254586813695900638
        d = 3.88747805345123254028
    elif distance == 10000 and gender == 2 and style == 2:
        a = -0.00000000028850755463
        b = 0.00000016886434031789
        c = 0.00225507058916807335
        d = 3.70207154009131045314
    # 15 km
    elif distance == 15000 and gender == 1 and style == 1:
        a = -0.00000000039724905749
        b = 0.00000028809305777783
        c = 0.00290746480602765978
        d = 4.26423417629504797333
    elif distance == 15000 and gender == 1 and style == 2:
        a = -0.00000000031071120914
        b = 0.00000009308373543314
        c = 0.00270423642565731370
        d = 4.10098797919077640017
    elif distance == 15000 and gender == 2 and style == 1:
        a = -0.00000000032480986728
        b = 0.00000022916137252908
        c = 0.00254976696830766514
        d = 3.76544670683006188483
    elif distance == 15000 and gender == 2 and style == 2:
        a = -0.00000000028821221717
        b = 0.00000016815684697534
        c = 0.00225936097079526554
        d = 3.54859250694988759278
    # 20 km
    elif distance == 20000 and gender == 1 and style == 1:
        a = -0.00000000039661899505
        b = 0.00000028644653265585
        c = 0.00291119176152010439
        d = 4.16518926507960429717
    elif distance == 20000 and gender == 1 and style == 2:
        a = -0.00000000028446647127
        b = 0.00000003256527443801
        c = 0.00273423712804121699
        d = 3.98274160496863771641
    elif distance == 20000 and gender == 2 and style == 1:
        a = -0.00000000032477567130
        b = 0.00000022912757417608
        c = 0.00255213057555958578
        d = 3.67228493554890178530
    elif distance == 20000 and gender == 2 and style == 2:
        a = -0.00000000028749187352
        b = 0.00000016653250197243
        c = 0.00226323217961654777
        d = 3.43198474109668438814
    # 30 km
    elif distance == 30000 and gender == 1 and style == 1:
        a = -0.00000000039575426311
        b = 0.00000028432395321140
        c = 0.00291607771391255710
        d = 4.02383491795778525102
    elif distance == 30000 and gender == 1 and style == 2:
        a = -0.00000000028515752610
        b = 0.00000003460398610732
        c = 0.00273736597569840256
        d = 3.81622588549436159155
    elif distance == 30000 and gender == 2 and style == 1:
        a = -0.00000000032414981226
        b = 0.00000022768544783542
        c = 0.00255630791066163710
        d = 3.53915182202850076010
    elif distance == 30000 and gender == 2 and style == 2:
        a = -0.00000000028389724121
        b = 0.00000015743411225784
        c = 0.00227260027321174451
        d = 3.26632608359584253321
    # 50 km
    elif distance == 50000 and gender == 1 and style == 1:
        a = -0.00000000039481251535
        b = 0.00000028218361058365
        c = 0.00292148393059599165
        d = 3.85804698607691420875
    elif distance == 50000 and gender == 1 and style == 2:
        a = -0.00000000031094403319
        b = 0.00000009504921010288
        c = 0.00271489794842039167
        d = 3.62310833196227122244
    elif distance == 50000 and gender == 2 and style == 1:
        a = -0.00000000032327614282
        b = 0.00000022571976289920
        c = 0.00256135257831924257
        d = 3.38317087457944865037
    elif distance == 50000 and gender == 2 and style == 2:
        a = -0.00000000028584347479
        b = 0.00000016279624805268
        c = 0.00227439967691156486
        d = 3.07455877006840694321
    # 70 km
    elif distance == 70000 and gender == 1 and style == 1:
        a = -0.00000000039387537747
        b = 0.00000027985768585956
        c = 0.00292518513522166401
        d = 3.76389646883168893510
    elif distance == 70000 and gender == 1 and style == 2:
        a = -0.00000000028667088554
        b = 0.00000003899195610987
        c = 0.00274271706750939259
        d = 3.51225745934733879494
    elif distance == 70000 and gender == 2 and style == 1:
        a = -0.00000000053509319726
        b = 0.00000078615292200472
        c = 0.00241406415917755357
        d = 2.70878710791764376609
    elif distance == 70000 and gender == 2 and style == 2:
        a = -0.00000000044983202396
        b = 0.00000059957474567835
        c = 0.00218044142963358389
        d = 2.45653985628075588465

    return a, b, c, d


distance_list = [1000, 2000, 3000, 5000, 7500, 10000, 15000, 20000, 30000, 50000, 70000]


from data import *


def add_measurement_data(cursor,point_value, distance_value, gender_id, style_id, value1, value2):

    cursor.execute('''
    INSERT INTO MeasurementsData (PointValue, DistanceValue, GenderID, StyleID, Speed, Time)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (point_value, distance_value, gender_id, style_id, value1, value2))

import logging

def calc():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    for i in range(123,2200+1):
        for distance in distance_list:
            for gender in range(1, 3):
                for style in range(1, 3):
                    a, b, c, d = get_coefficient(distance, gender, style)
                    speed = a * math.pow(i, 3) + b * math.pow(i, 2) + c * i + d
                    time = distance/speed
                    add_measurement_data(cursor,i, distance, gender, style, round(speed, 2), round(time, 4))
        db.commit()
        logging.info(f"{i}")
    db.close()
    print("Успех!")

def get():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    a = cursor.execute("SELECT ID,PointValue,DistanceValue,GenderID,StyleID,Speed,Time FROM MeasurementsData WHERE GenderID = 1 AND styleID = 1 AND DistanceValue = 1000 AND Time = 359").fetchall()
    print(a)
    db.close()


get()