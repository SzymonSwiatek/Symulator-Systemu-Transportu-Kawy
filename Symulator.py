import snap7.client #as c
#import snap7
from snap7.util import *
from snap7.snap7types import *
import time


myplc = snap7.client.Client()
plc_IP = '192.168.10.56'
plc_RACK = 0
plc_SLOT = 1

try:
    myplc.connect(plc_IP, plc_RACK, plc_SLOT)
except ConnectionError:
    print("Upss...")


def get_process_outputs_bit(plc, byte, bit):
    result = plc.read_area(areas['PA'], 0, byte, S7WLBit)
    return get_bool(result, 0, bit)


def set_process_outputs_bit(plc, byte, bit, cmd):
    result = plc.read_area(areas['PA'], 0, byte, S7WLBit)
    set_bool(result, byte, bit, cmd)
    plc.write_area(areas['PA'], 0, byte, result)


def set_process_inputs_bit(plc, byte, bit, cmd):
    result = plc.read_area(areas['PE'], 0, byte, S7WLBit)
    set_bool(result, byte, bit, cmd)
    plc.write_area(areas['PE'], 0, byte, result)


def get_process_inputs_bit(plc, byte, bit):
    result = plc.read_area(areas['PE'], 0, byte, S7WLBit)
    return get_bool(result, 0, bit)


def get_merkers(plc, byte, bit, datatype):
    result = plc.read_area(areas['MK'], 0, byte, datatype)
    if datatype == S7WLBit:
        return get_bool(result, 0, bit)
    elif datatype == S7WLByte or datatype == S7WLWord:
        return get_int(result, 0)
    elif datatype == S7WLReal:
        return get_real(result, 0)
    elif datatype == S7WLDWord:
        return get_dword(result, 0)
    else:
        return None


def set_merkers(plc, byte, bit, datatype, value):
    result = plc.read_area(areas['MK'], 0, byte, datatype)
    if datatype == S7WLBit:
        set_bool(result, 0, bit, value)
    elif datatype == S7WLByte or datatype == S7WLWord:
        set_int(result, byte, value)
    elif datatype == S7WLReal:
        set_real(result, byte, value)
    elif datatype == S7WLDWord:
        set_dword(result, byte, value)
    plc.write_area(areas['MK'], 0, byte, result)

def set_marker(byte, bit, value):
    result = myplc.read_area(areas['MK'], 0, byte, S7WLBit)
    set_bool(result, 0, bit, value)
    myplc.write_area(areas['MK'], 0, byte, result)

def get_marker(byte, bit):
    result = myplc.read_area(areas['MK'], 0, byte, S7WLBit)
    return get_bool(result, 0, bit)


    

#wartość nieprawidłowa, żeby wyzwolić pierwsze nadpisanie markerów wejściowych po uruchomieniu
TKZq_Czyszczarka = 2
TKZq_Dmuchawa_1 = 2
TKZq_Dmuchawa_2 = 2
TKZq_Kubełkowy_1 = 2
TKZq_Kubełkowy_2 = 2
TKZq_Odkamieniacz = 2
TKZq_Śluza_1 = 2
TKZq_Śluza_2 = 2
TKZq_Zasuwa_150 = 2
TKZq_Zasuwa_151 = 2
TKZq_Zasuwa_152 = 2
TKZq_Zasuwa_153 = 2
TKZq_Zasuwa_154 = 2
TKZq_Zasuwa_155 = 2
TKZq_Zasuwa_156 = 2
TKZq_Zasuwa_157 = 2
TKZq_Zasuwa_158 = 2
TKZq_Zasuwa_159 = 2
TKZq_Zasuwa_160 = 2
TKZq_Zasuwa_BigBag = 2
TKZq_Zasuwa_nad_waga1 = 2
TKZq_Zasuwa_pod_waga1 = 2
TKZq_Zasuwa_pod_waga2 = 2
TKZq_Zwrotnica_bypass = 2
TKZq_Zwrotnica_NaBigBag = 2
TKZq_Zwrotnica_NaZwrot = 2
TKZq_Zwrotnica_obrotowa = 2

TKUq_Dmuchawa_3 = 2
TKUq_Kubełkowy_3 = 2
TKUq_Kubełkowy_4 = 2
TKUq_Odkamieniacz = 2
TKUq_Śluza_3 = 2
TKUq_Transporter_DodatkoweSilosy = 2
TKUq_Transporter_PodstawoweSilosy = 2
TKUq_Zasuwa_250 = 2
TKUq_Zasuwa_251 = 2
TKUq_Zasuwa_252 = 2
TKUq_Zasuwa_253 = 2
TKUq_Zasuwa_254 = 2
TKUq_Zasuwa_255 = 2
TKUq_Zasuwa_256 = 2
TKUq_Zasuwa_257 = 2
TKUq_Zasuwa_258 = 2
TKUq_Zasuwa_259 = 2
TKUq_Zasuwa_260 = 2
TKUq_Zasuwa_nad_waga3 = 2
TKUq_Zasuwa_pod_waga3 = 2
TKUq_Zasuwa_pod_waga4 = 2
TKUq_Zasuwa_pod_zb_zwrotu = 2
TKUq_ZsypNa250 = 2
TKUq_ZsypNa251 = 2
TKUq_ZsypNa252 = 2
TKUq_ZsypNa253 = 2
TKUq_ZsypNa254 = 2
TKUq_ZsypNa255 = 2
TKUq_ZsypNa256 = 2
TKUq_ZsypNa257 = 2
TKUq_ZsypNa258 = 2
TKUq_ZsypNa259 = 2
TKUq_ZsypNa260 = 2
TKUq_Zwrotnica_bypass = 2
TKUq_Zwrotnica_NaDodatkoweSilosy = 2
TKUq_Zwrotnica_NaKontener = 2
TKUq_Zwrotnica_NaMłyny2 = 2
TKUq_Zwrotnica_NaZwrot = 2

TKMq_Bączek1 = 2
TKMq_Bączek2 = 2
TKMq_Chłodnica1 = 2
TKMq_Chłodnica2 = 2
TKMq_Dmuchawa1 = 2
TKMq_Dmuchawa2 = 2
TKMq_Odsiewacz1 = 2
TKMq_Odsiewacz2 = 2
TKMq_Rekondycja1 = 2
TKMq_Rekondycja2 = 2
TKMq_Śluza1 = 2
TKMq_Śluza2 = 2
TKMq_Włącz_Młyn1 = 2
TKMq_Włącz_Młyn2 = 2
TKMq_Zasuwa_nad_młynem1 = 2
TKMq_Zasuwa_nad_młynem2 = 2
TKMq_Zwrotnica_401_402 = 2
TKMq_Zwrotnica_403_404 = 2
TKMq_Zwrotnica_405_406 = 2
TKMq_Zwrotnica_407_408 = 2
TKMq_Zwrotnica_409_410 = 2

gotowy = True
index = 0
waga1 = 0
waga2 = 0
waga3 = 0
waga4 = 0

set_marker(105,1, 1) # TKZin_Gotowość_Czyszczarka
set_marker(106,5, 1) # TKZin_Gotowość_Dmuchawa1
set_marker(112,1, 1) # TKZin_Gotowość_Dmuchawa2
set_marker(104,5, 1) # TKZin_Gotowosc_Kubełkowy1
set_marker(104,6, 1) # TKZin_Gotowość_Kubełkowy2
set_marker(105,4, 1) # TKZin_Gotowość_Odkamieniacz
set_marker(107,0, 1) # TKZin_Gotowość_Śluza1
set_marker(111,6, 1) # TKZin_Gotowość_Śluza2
set_marker(113,2, 1) # TKZin_Gotowość_Zwrotnica_obrotowa

set_marker(214,6, 1) # TKUin_Gotowość_Dmuchawa3
set_marker(200,5, 1) # TKUin_Gotowosc_Kubełkowy3
set_marker(201,2, 1) # TKUin_Gotowość_Kubełkowy4
set_marker(202,6, 1) # TKUin_Gotowość_Odkamieniacz
set_marker(215,3, 1) # TKUin_Gotowość_Śluza3
set_marker(209,2, 1) # TKUin_Gotowość_Transport_DodatkSilosy
set_marker(208,6, 1) # TKUin_Gotowość_Transport_PodstSilosy

set_marker(301,6, 1) # TKMin_Gotowość_Bączek1
set_marker(305,7, 1) # TKMin_Gotowość_Bączek2
set_marker(303,6, 1) # TKMin_Gotowość_Chłodnica1
set_marker(307,7, 1) # TKMin_Gotowość_Chłodnica2
set_marker(303,2, 1) # TKMin_Gotowość_Dmuchawa1
set_marker(307,3, 1) # TKMin_Gotowość_Dmuchawa2
set_marker(301,4, 1) # TKMin_Gotowość_Młyn1
set_marker(305,0, 1) # TKMin_Gotowość_Młyn2
set_marker(300,6, 1) # TKMin_Gotowość_Odsiewacz1
set_marker(305,3, 1) # TKMin_Gotowość_Odsiewacz2
set_marker(302,6, 1) # TKMin_Gotowość_Rekondycja1
set_marker(306,7, 1) # TKMin_Gotowość_Rekondycja2
set_marker(302,2, 1) # TKMin_Gotowość_Śluza1
set_marker(306,3, 1) # TKMin_Gotowość_Śluza2


set_marker(105,2, 1) # TKZin_Termik_Czyszczarka
set_marker(106,6, 1) # TKZin_Termik_Dmuchawa1
set_marker(112,2, 1) # TKZin_Termik_Dmuchawa2
set_marker(104,3, 1) # TKZin_Termik_Kubełkowy1
set_marker(104,7, 1) # TKZin_Termik_Kubełkowy2
set_marker(105,5, 1) # TKZin_Termik_Odkamieniacz
set_marker(107,1, 1) # TKZin_Termik_Śluza1
set_marker(111,7, 1) # TKZin_Termik_Śluza2
set_marker(113,3, 1) # TKZin_Termik_Zwrotnica_obrotowa

set_marker(214,7, 1) # TKUin_Termik_Dmuchawa3
set_marker(200,6, 1) # TKUin_Termik_Kubełkowy3
set_marker(201,3, 1) # TKUin_Termik_Kubełkowy4
set_marker(202,7, 1) # TKUin_Termik_Odkamieniacz
set_marker(215,4, 1) # TKUin_Termik_Śluza3
set_marker(209,3, 1) # TKUin_Termik_Transport_DodatkSilosy
set_marker(208,7, 1) # TKUin_Termik_Transport_PodstSilosy

set_marker(301,7, 1) # TKMin_Termik_Bączek1
set_marker(306,0, 1) # TKMin_Termik_Bączek2
set_marker(303,7, 1) # TKMin_Termik_Chłodnica1
set_marker(308,0, 1) # TKMin_Termik_Chłodnica2
set_marker(303,3, 1) # TKMin_Termik_Dmuchawa1
set_marker(307,4, 1) # TKMin_Termik_Dmuchawa2
set_marker(300,7, 1) # TKMin_Termik_Odsiewacz1
set_marker(305,4, 1) # TKMin_Termik_Odsiewacz2
set_marker(302,7, 1) # TKMin_Termik_Rekondycja1
set_marker(307,0, 1) # TKMin_Termik_Rekondycja2
set_marker(302,3, 1) # TKMin_Termik_Śluza1
set_marker(306,4, 1) # TKMin_Termik_Śluza2
set_marker(301,3, 1) # TKMin_Awaria_Młyn1
set_marker(305,1, 1) # TKMin_Awaria_Młyn2

print('Inicjalizacja zmiennych zakonczona')

while True:
    #start = time.clock()
    #TKZ
    TKZq_Czyszczarka_old = TKZq_Czyszczarka
    TKZq_Dmuchawa_1_old = TKZq_Dmuchawa_1
    TKZq_Dmuchawa_2_old = TKZq_Dmuchawa_2
    TKZq_Kubełkowy_1_old = TKZq_Kubełkowy_1
    TKZq_Kubełkowy_2_old = TKZq_Kubełkowy_2
    TKZq_Odkamieniacz_old = TKZq_Odkamieniacz
    TKZq_Śluza_1_old = TKZq_Śluza_1
    TKZq_Śluza_2_old = TKZq_Śluza_2
    TKZq_Zasuwa_150_old = TKZq_Zasuwa_150
    TKZq_Zasuwa_151_old = TKZq_Zasuwa_151
    TKZq_Zasuwa_152_old = TKZq_Zasuwa_152
    TKZq_Zasuwa_153_old = TKZq_Zasuwa_153
    TKZq_Zasuwa_154_old = TKZq_Zasuwa_154
    TKZq_Zasuwa_155_old = TKZq_Zasuwa_155
    TKZq_Zasuwa_156_old = TKZq_Zasuwa_156
    TKZq_Zasuwa_157_old = TKZq_Zasuwa_157
    TKZq_Zasuwa_158_old = TKZq_Zasuwa_158
    TKZq_Zasuwa_159_old = TKZq_Zasuwa_159
    TKZq_Zasuwa_160_old = TKZq_Zasuwa_160
    TKZq_Zasuwa_BigBag_old = TKZq_Zasuwa_BigBag
    TKZq_Zasuwa_nad_waga1_old = TKZq_Zasuwa_nad_waga1
    TKZq_Zasuwa_pod_waga1_old = TKZq_Zasuwa_pod_waga1
    TKZq_Zasuwa_pod_waga2_old = TKZq_Zasuwa_pod_waga2
    TKZq_Zwrotnica_bypass_old = TKZq_Zwrotnica_bypass
    TKZq_Zwrotnica_NaBigBag_old = TKZq_Zwrotnica_NaBigBag
    TKZq_Zwrotnica_NaZwrot_old = TKZq_Zwrotnica_NaZwrot
    TKZq_Zwrotnica_obrotowa_old = TKZq_Zwrotnica_obrotowa
    
    TKZq_Czyszczarka = get_marker(100,5)
    TKZq_Dmuchawa_1 = get_marker(101,4)
    TKZq_Dmuchawa_2 = get_marker(103,6)
    TKZq_Kubełkowy_1 = get_marker(100,1)
    TKZq_Kubełkowy_2 = get_marker(100,3)
    TKZq_Odkamieniacz = get_marker(100,6)
    TKZq_Śluza_1 = get_marker(101,6)
    TKZq_Śluza_2 = get_marker(103,5)
    TKZq_Zasuwa_150 = get_marker(102,0)
    TKZq_Zasuwa_151 = get_marker(102,1)
    TKZq_Zasuwa_152 = get_marker(102,2)
    TKZq_Zasuwa_153 = get_marker(102,3)
    TKZq_Zasuwa_154 = get_marker(102,4)
    TKZq_Zasuwa_155 = get_marker(102,5)
    TKZq_Zasuwa_156 = get_marker(102,6)
    TKZq_Zasuwa_157 = get_marker(102,7)
    TKZq_Zasuwa_158 = get_marker(103,0)
    TKZq_Zasuwa_159 = get_marker(103,1)
    TKZq_Zasuwa_160 = get_marker(103,2)
    TKZq_Zasuwa_BigBag = get_marker(104,2)
    TKZq_Zasuwa_nad_waga1 = get_marker(101,1)
    TKZq_Zasuwa_pod_waga1 = get_marker(101,2)
    TKZq_Zasuwa_pod_waga2 = get_marker(103,3)
    TKZq_Zwrotnica_bypass = get_marker(100,7)
    TKZq_Zwrotnica_NaBigBag = get_marker(104,1)
    TKZq_Zwrotnica_NaZwrot = get_marker(104,0)
    TKZq_Zwrotnica_obrotowa = get_marker(101,7)

#TKU
    TKUq_Dmuchawa_3_old = TKUq_Dmuchawa_3
    TKUq_Kubełkowy_3_old = TKUq_Kubełkowy_3
    TKUq_Kubełkowy_4_old = TKUq_Kubełkowy_4
    TKUq_Odkamieniacz_old = TKUq_Odkamieniacz
    TKUq_Śluza_3_old = TKUq_Śluza_3
    TKUq_Transporter_DodatkoweSilosy_old = TKUq_Transporter_DodatkoweSilosy
    TKUq_Transporter_PodstawoweSilosy_old = TKUq_Transporter_PodstawoweSilosy
    TKUq_Zasuwa_250_old = TKUq_Zasuwa_250
    TKUq_Zasuwa_251_old = TKUq_Zasuwa_251
    TKUq_Zasuwa_252_old = TKUq_Zasuwa_252
    TKUq_Zasuwa_253_old = TKUq_Zasuwa_253
    TKUq_Zasuwa_254_old = TKUq_Zasuwa_254
    TKUq_Zasuwa_255_old = TKUq_Zasuwa_255
    TKUq_Zasuwa_256_old = TKUq_Zasuwa_256
    TKUq_Zasuwa_257_old = TKUq_Zasuwa_257
    TKUq_Zasuwa_258_old = TKUq_Zasuwa_258
    TKUq_Zasuwa_259_old = TKUq_Zasuwa_259
    TKUq_Zasuwa_260_old = TKUq_Zasuwa_260
    TKUq_Zasuwa_nad_waga3_old = TKUq_Zasuwa_nad_waga3
    TKUq_Zasuwa_pod_waga3_old = TKUq_Zasuwa_pod_waga3
    TKUq_Zasuwa_pod_waga4_old = TKUq_Zasuwa_pod_waga4
    TKUq_Zasuwa_pod_zb_zwrotu_old = TKUq_Zasuwa_pod_zb_zwrotu
    TKUq_ZsypNa250_old = TKUq_ZsypNa250
    TKUq_ZsypNa251_old = TKUq_ZsypNa251
    TKUq_ZsypNa252_old = TKUq_ZsypNa252
    TKUq_ZsypNa253_old = TKUq_ZsypNa253
    TKUq_ZsypNa254_old = TKUq_ZsypNa254
    TKUq_ZsypNa255_old = TKUq_ZsypNa255
    TKUq_ZsypNa256_old = TKUq_ZsypNa256
    TKUq_ZsypNa257_old = TKUq_ZsypNa257
    TKUq_ZsypNa258_old = TKUq_ZsypNa258
    TKUq_ZsypNa259_old = TKUq_ZsypNa259
    TKUq_ZsypNa260_old = TKUq_ZsypNa260
    TKUq_Zwrotnica_bypass_old = TKUq_Zwrotnica_bypass
    TKUq_Zwrotnica_NaDodatkoweSilosy_old = TKUq_Zwrotnica_NaDodatkoweSilosy
    TKUq_Zwrotnica_NaKontener_old = TKUq_Zwrotnica_NaKontener
    TKUq_Zwrotnica_NaMłyny2_old = TKUq_Zwrotnica_NaMłyny2
    TKUq_Zwrotnica_NaZwrot_old = TKUq_Zwrotnica_NaZwrot


    TKUq_Dmuchawa_3 = get_marker(214,5)
    TKUq_Kubełkowy_3 = get_marker(200,4)
    TKUq_Kubełkowy_4 = get_marker(201,1)
    TKUq_Odkamieniacz = get_marker(202,5)
    TKUq_Śluza_3 = get_marker(215,2)
    TKUq_Transporter_DodatkoweSilosy = get_marker(209,1)
    TKUq_Transporter_PodstawoweSilosy = get_marker(208,5)
    TKUq_Zasuwa_250 = get_marker(209,5)
    TKUq_Zasuwa_251 = get_marker(209,6)
    TKUq_Zasuwa_252 = get_marker(209,7)
    TKUq_Zasuwa_253 = get_marker(210,0)
    TKUq_Zasuwa_254 = get_marker(210,1)
    TKUq_Zasuwa_255 = get_marker(210,2)
    TKUq_Zasuwa_256 = get_marker(210,3)
    TKUq_Zasuwa_257 = get_marker(210,4)
    TKUq_Zasuwa_258 = get_marker(210,5)
    TKUq_Zasuwa_259 = get_marker(210,6)
    TKUq_Zasuwa_260 = get_marker(210,7)
    TKUq_Zasuwa_nad_waga3 = get_marker(201,6)
    TKUq_Zasuwa_pod_waga3 = get_marker(202,1)
    TKUq_Zasuwa_pod_waga4 = get_marker(211,0)
    TKUq_Zasuwa_pod_zb_zwrotu = get_marker(203,5)
    TKUq_ZsypNa250 = get_marker(204,4)
    TKUq_ZsypNa251 = get_marker(204,5)
    TKUq_ZsypNa252 = get_marker(204,6)
    TKUq_ZsypNa253 = get_marker(204,7)
    TKUq_ZsypNa254 = get_marker(205,0)
    TKUq_ZsypNa255 = get_marker(205,1)
    TKUq_ZsypNa256 = get_marker(205,2)
    TKUq_ZsypNa257 = get_marker(205,3)
    TKUq_ZsypNa258 = get_marker(205,4)
    TKUq_ZsypNa259 = get_marker(205,5)
    TKUq_ZsypNa260 = get_marker(205,6)
    TKUq_Zwrotnica_bypass = get_marker(203,1)
    TKUq_Zwrotnica_NaDodatkoweSilosy = get_marker(204,1)
    TKUq_Zwrotnica_NaKontener = get_marker(214,2)
    TKUq_Zwrotnica_NaMłyny2 = get_marker(215,7)
    TKUq_Zwrotnica_NaZwrot = get_marker(216,3)



#TKM
    TKMq_Bączek1_old = TKMq_Bączek1
    TKMq_Bączek2_old = TKMq_Bączek2
    TKMq_Chłodnica1_old = TKMq_Chłodnica1
    TKMq_Chłodnica2_old = TKMq_Chłodnica2
    TKMq_Dmuchawa1_old = TKMq_Dmuchawa1
    TKMq_Dmuchawa2_old = TKMq_Dmuchawa2
    TKMq_Odsiewacz1_old = TKMq_Odsiewacz1
    TKMq_Odsiewacz2_old = TKMq_Odsiewacz2
    TKMq_Rekondycja1_old = TKMq_Rekondycja1
    TKMq_Rekondycja2_old = TKMq_Rekondycja2
    TKMq_Śluza1_old = TKMq_Śluza1
    TKMq_Śluza2_old = TKMq_Śluza2
    TKMq_Włącz_Młyn1_old = TKMq_Włącz_Młyn1
    TKMq_Włącz_Młyn2_old = TKMq_Włącz_Młyn2
    TKMq_Zasuwa_nad_młynem1_old = TKMq_Zasuwa_nad_młynem1
    TKMq_Zasuwa_nad_młynem2_old = TKMq_Zasuwa_nad_młynem2
    TKMq_Zwrotnica_401_402_old = TKMq_Zwrotnica_401_402
    TKMq_Zwrotnica_403_404_old = TKMq_Zwrotnica_403_404
    TKMq_Zwrotnica_405_406_old = TKMq_Zwrotnica_405_406
    TKMq_Zwrotnica_407_408_old = TKMq_Zwrotnica_407_408
    TKMq_Zwrotnica_409_410_old = TKMq_Zwrotnica_409_410

    TKMq_Bączek1 = get_marker(301,5)
    TKMq_Bączek2 = get_marker(305,6)
    TKMq_Chłodnica1 = get_marker(303,5)
    TKMq_Chłodnica2 = get_marker(307,6)
    TKMq_Dmuchawa1 = get_marker(303,1)
    TKMq_Dmuchawa2 = get_marker(307,2)
    TKMq_Odsiewacz1 = get_marker(300,5)
    TKMq_Odsiewacz2 = get_marker(305,2)
    TKMq_Rekondycja1 = get_marker(302,5)
    TKMq_Rekondycja2 = get_marker(306,6)
    TKMq_Śluza1 = get_marker(302,1)
    TKMq_Śluza2 = get_marker(306,2)
    TKMq_Włącz_Młyn1 = get_marker(301,1)
    TKMq_Włącz_Młyn2 = get_marker(304,6)
    TKMq_Zasuwa_nad_młynem1 = get_marker(300,2)
    TKMq_Zasuwa_nad_młynem2 = get_marker(304,3)
    TKMq_Zwrotnica_401_402 = get_marker(308,2)
    TKMq_Zwrotnica_403_404 = get_marker(308,5)
    TKMq_Zwrotnica_405_406 = get_marker(309,0)
    TKMq_Zwrotnica_407_408 = get_marker(309,3)
    TKMq_Zwrotnica_409_410 = get_marker(309,6)





#TKZ
    if TKZq_Czyszczarka_old != TKZq_Czyszczarka:
        if TKZq_Czyszczarka:
            set_marker(105,3, 1) #TKZin_Potw_Czyszczarka
        else:
            set_marker(105,3, 0) #TKZin_Potw_Czyszczarka
    

    if TKZq_Dmuchawa_1_old != TKZq_Dmuchawa_1:            
        if TKZq_Dmuchawa_1:
            set_marker(106,7, 1) #TKZin_Potw_Dmuchawa1
        else:
            set_marker(106,7, 0) #TKZin_Potw_Dmuchawa1

    if TKZq_Dmuchawa_2_old != TKZq_Dmuchawa_2:        
        if TKZq_Dmuchawa_2:
            set_marker(112,3, 1) #TKZin_Potw_Dmuchawa2
        else:
            set_marker(112,3, 0) #TKZin_Potw_Dmuchawa2

    if TKZq_Kubełkowy_1_old != TKZq_Kubełkowy_1:        
        if TKZq_Kubełkowy_1:
            set_marker(104,4, 1) #TKZin_Potw_Kubełkowy1
        else:
            set_marker(104,4, 0) #TKZin_Potw_Kubełkowy1

    if TKZq_Kubełkowy_2_old != TKZq_Kubełkowy_2:        
        if TKZq_Kubełkowy_2:
            set_marker(105,0, 1) #TKZin_Potw_Kubełkowy2
        else:
            set_marker(105,0, 0) #TKZin_Potw_Kubełkowy2  

    if TKZq_Odkamieniacz_old != TKZq_Odkamieniacz:        
        if TKZq_Odkamieniacz:
            set_marker(105,6, 1) #TKZin_Potw_Odkamieniacz
        else:
            set_marker(105,6, 0) #TKZin_Potw_Odkamieniacz  

    if TKZq_Śluza_1_old != TKZq_Śluza_1:        
        if TKZq_Śluza_1:
            set_marker(107,2, 1) #TKZin_Potw_Śluza1
        else:
            set_marker(107,2, 0) #TKZin_Potw_Śluza1  

    if TKZq_Śluza_2_old != TKZq_Śluza_2:        
        if TKZq_Śluza_2:
            set_marker(112,0, 1) #TKZin_Potw_Śluza2
        else:
            set_marker(112,0, 0) #TKZin_Potw_Śluza2 

    if TKZq_Zasuwa_150_old != TKZq_Zasuwa_150:        
        if TKZq_Zasuwa_150:
            set_marker(108,7, 0) #TKZin_Zasuwa_150_zamknięta
            time.sleep(1)
            set_marker(108,6, 1) #TKZin_Zasuwa_150_otwarta
            TKZin_Zasuwa_150_otwarta = True
        else:
            set_marker(108,6, 0) #TKZin_Zasuwa_150_otwarta
            TKZin_Zasuwa_150_otwarta = False
            time.sleep(1)
            set_marker(108,7, 1) #TKZin_Zasuwa_150_zamknięta

    if TKZq_Zasuwa_151_old != TKZq_Zasuwa_151:        
        if TKZq_Zasuwa_151:
            set_marker(109,1, 0) #TKZin_Zasuwa_151_zamknięta
            time.sleep(1)
            set_marker(109,0, 1) #TKZin_Zasuwa_151_otwarta
            TKZin_Zasuwa_151_otwarta = True
        else:
            set_marker(109,0, 0) #TKZin_Zasuwa_151_otwarta
            TKZin_Zasuwa_151_otwarta = False
            time.sleep(1)
            set_marker(109,1, 1) #TKZin_Zasuwa_151_zamknięta

    if TKZq_Zasuwa_152_old != TKZq_Zasuwa_152:        
        if TKZq_Zasuwa_152:
            set_marker(109,3, 0) #TKZin_Zasuwa_152_zamknięta
            time.sleep(1)
            set_marker(109,2, 1) #TKZin_Zasuwa_152_otwarta
            TKZin_Zasuwa_152_otwarta = True
        else:
            set_marker(109,2, 0) #TKZin_Zasuwa_152_otwarta
            TKZin_Zasuwa_152_otwarta = False
            time.sleep(1)
            set_marker(109,3, 1) #TKZin_Zasuwa_152_zamknięta 

    if TKZq_Zasuwa_153_old != TKZq_Zasuwa_153:        
        if TKZq_Zasuwa_153:
            set_marker(109,5, 0) #TKZin_Zasuwa_153_zamknięta
            time.sleep(1)
            set_marker(109,4, 1) #TKZin_Zasuwa_153_otwarta
            TKZin_Zasuwa_153_otwarta = True
        else:
            set_marker(109,4, 0) #TKZin_Zasuwa_153_otwarta
            TKZin_Zasuwa_153_otwarta = False
            time.sleep(1)
            set_marker(109,5, 1) #TKZin_Zasuwa_153_zamknięta

    if TKZq_Zasuwa_154_old != TKZq_Zasuwa_154:        
        if TKZq_Zasuwa_154:
            set_marker(109,7, 0) #TKZin_Zasuwa_154_zamknięta
            time.sleep(1)
            set_marker(109,6, 1) #TKZin_Zasuwa_154_otwarta
            TKZin_Zasuwa_154_otwarta = True
        else:
            set_marker(109,6, 0) #TKZin_Zasuwa_154_otwarta
            TKZin_Zasuwa_154_otwarta = False
            time.sleep(1)
            set_marker(109,7, 1) #TKZin_Zasuwa_154_zamknięta              

    if TKZq_Zasuwa_155_old != TKZq_Zasuwa_155:        
        if TKZq_Zasuwa_155:
            set_marker(110,1, 0) #TKZin_Zasuwa_155_zamknięta
            time.sleep(1)
            set_marker(110,0, 1) #TKZin_Zasuwa_155_otwarta
            TKZin_Zasuwa_155_otwarta = True
        else:
            set_marker(110,0, 0) #TKZin_Zasuwa_155_otwarta
            TKZin_Zasuwa_155_otwarta = False
            time.sleep(1)
            set_marker(110,1, 1) #TKZin_Zasuwa_155_zamknięta              

    if TKZq_Zasuwa_156_old != TKZq_Zasuwa_156:        
        if TKZq_Zasuwa_156:
            set_marker(110,3, 0) #TKZin_Zasuwa_156_zamknięta
            time.sleep(1)
            set_marker(110,2, 1) #TKZin_Zasuwa_156_otwarta
            TKZin_Zasuwa_156_otwarta = True
        else:
            set_marker(110,2, 0) #TKZin_Zasuwa_156_otwarta
            TKZin_Zasuwa_156_otwarta = False
            time.sleep(1)
            set_marker(110,3, 1) #TKZin_Zasuwa_156_zamknięta        

    if TKZq_Zasuwa_157_old != TKZq_Zasuwa_157:        
        if TKZq_Zasuwa_157:
            set_marker(110,5, 0) #TKZin_Zasuwa_157_zamknięta
            time.sleep(1)
            set_marker(110,4, 1) #TKZin_Zasuwa_157_otwarta
            TKZin_Zasuwa_157_otwarta = True
        else:
            set_marker(110,4, 0) #TKZin_Zasuwa_157_otwarta
            TKZin_Zasuwa_157_otwarta = False
            time.sleep(1)
            set_marker(110,5, 1) #TKZin_Zasuwa_157_zamknięta             

    if TKZq_Zasuwa_158_old != TKZq_Zasuwa_158:        
        if TKZq_Zasuwa_158:
            set_marker(110,7, 0) #TKZin_Zasuwa_158_zamknięta
            time.sleep(1)
            set_marker(110,6, 1) #TKZin_Zasuwa_158_otwarta
            TKZin_Zasuwa_158_otwarta = True
        else:
            set_marker(110,6, 0) #TKZin_Zasuwa_158_otwarta
            TKZin_Zasuwa_158_otwarta = False
            time.sleep(1)
            set_marker(110,7, 1) #TKZin_Zasuwa_158_zamknięta       

    if TKZq_Zasuwa_159_old != TKZq_Zasuwa_159:        
        if TKZq_Zasuwa_159:
            set_marker(111,1, 0) #TKZin_Zasuwa_159_zamknięta
            time.sleep(1)
            set_marker(111,0, 1) #TKZin_Zasuwa_159_otwarta
            TKZin_Zasuwa_159_otwarta = True
        else:
            set_marker(111,0, 0) #TKZin_Zasuwa_159_otwarta
            TKZin_Zasuwa_159_otwarta = False
            time.sleep(1)
            set_marker(111,1, 1) #TKZin_Zasuwa_159_zamknięta       
    
    if TKZq_Zasuwa_160_old != TKZq_Zasuwa_160:          
        if TKZq_Zasuwa_160:
            set_marker(111,3, 0) #TKZin_Zasuwa_160_zamknięta
            time.sleep(1)
            set_marker(111,2, 1) #TKZin_Zasuwa_160_otwarta
            TKZin_Zasuwa_160_otwarta = True
        else:
            set_marker(111,2, 0) #TKZin_Zasuwa_160_otwarta
            TKZin_Zasuwa_160_otwarta = False
            time.sleep(1)
            set_marker(111,3, 1) #TKZin_Zasuwa_160_zamknięta
            
    if TKZq_Zasuwa_BigBag_old != TKZq_Zasuwa_BigBag:          
        if TKZq_Zasuwa_BigBag:
            set_marker(113,1, 0) #TKZin_Zasuwa_BigBag_zamknięta
            time.sleep(1)
            set_marker(113,0, 1) #TKZin_Zasuwa_BigBag_otwarta     
        else:
            set_marker(113,0, 0) #TKZin_Zasuwa_BigBag_otwarta
            time.sleep(1)
            set_marker(113,1, 1) #TKZin_Zasuwa_BigBag_zamknięta
            
    if TKZq_Zasuwa_nad_waga1_old != TKZq_Zasuwa_nad_waga1:          
        if TKZq_Zasuwa_nad_waga1:
            set_marker(106,2, 0) #TKZin_Zasuwa_nad_waga1_zamknięta
            time.sleep(1)
            set_marker(106,1, 1) #TKZin_Zasuwa_nad_waga1_otwarta
            TKZin_Zasuwa_nad_waga1_otwarta = True
        else:
            set_marker(106,1, 0) #TKZin_Zasuwa_nad_waga1_otwarta
            TKZin_Zasuwa_nad_waga1_otwarta = False
            time.sleep(1)
            set_marker(106,2, 1) #TKZin_Zasuwa_nad_waga1_zamknięta
            
    if TKZq_Zasuwa_pod_waga1_old != TKZq_Zasuwa_pod_waga1:          
        if TKZq_Zasuwa_pod_waga1:
            set_marker(106,4, 0) #TKZin_Zasuwa_pod_waga1_zamknięta
            time.sleep(1)
            set_marker(106,3, 1) #TKZin_Zasuwa_pod_waga1_otwarta
            TKZin_Zasuwa_pod_waga1_otwarta = True
        else:
            set_marker(106,3, 0) #TKZin_Zasuwa_pod_waga1_otwarta
            TKZin_Zasuwa_pod_waga1_otwarta = False
            time.sleep(1)
            set_marker(106,4, 1) #TKZin_Zasuwa_pod_waga1_zamknięta
            
    if TKZq_Zasuwa_pod_waga2_old != TKZq_Zasuwa_pod_waga2:          
        if TKZq_Zasuwa_pod_waga2:
            set_marker(111,5, 0) #TKZin_Zasuwa_pod_waga2_zamknięta
            time.sleep(1)
            set_marker(111,4, 1) #TKZin_Zasuwa_pod_waga2_otwarta
            TKZin_Zasuwa_pod_waga2_otwarta = True
        else:
            set_marker(111,4, 0) #TKZin_Zasuwa_pod_waga2_otwarta
            TKZin_Zasuwa_pod_waga2_otwarta = False
            time.sleep(1)
            set_marker(111,5, 1) #TKZin_Zasuwa_pod_waga2_zamknięta
            
    if TKZq_Zwrotnica_bypass_old != TKZq_Zwrotnica_bypass:         
        if TKZq_Zwrotnica_bypass:
            set_marker(106,0, 0) #TKZin_Zwrotnica_na_odkamieniacz
            time.sleep(1)
            set_marker(105,7, 1) #TKZin_Zwrotnica_na_Bypass       
        else:
            set_marker(105,7, 0) #TKZin_Zwrotnica_na_Bypass
            time.sleep(1)
            set_marker(106,0, 1) #TKZin_Zwrotnica_na_odkamieniacz
            
    if TKZq_Zwrotnica_NaBigBag_old != TKZq_Zwrotnica_NaBigBag:          
        if TKZq_Zwrotnica_NaBigBag:
            set_marker(112,7, 0) #TKZin_Zwrotnica_NaPiec
            time.sleep(1)
            set_marker(112,6, 1) #TKZin_Zwrotnica_NaBigBag       
        else:
            set_marker(112,6, 0) #TKZin_Zwrotnica_NaBigBag
            time.sleep(1)
            set_marker(112,7, 1) #TKZin_Zwrotnica_NaPiec
            
    if TKZq_Zwrotnica_NaZwrot_old != TKZq_Zwrotnica_NaZwrot:          
        if TKZq_Zwrotnica_NaZwrot:
            set_marker(112,5, 0) #TKZin_Zwrotnica_NaNastępZwrotnice
            time.sleep(1)
            set_marker(112,4, 1) #TKZin_Zwrotnica_NaZwrot         
        else:
            set_marker(112,4, 0) #TKZin_Zwrotnica_NaZwrot
            time.sleep(1)
            set_marker(112,5, 1) #TKZin_Zwrotnica_NaNastępZwrotnice
            
    if TKZq_Zwrotnica_obrotowa_old != TKZq_Zwrotnica_obrotowa:          
        if TKZq_Zwrotnica_obrotowa:
            set_marker(113,4, 1) #TKZin_Potw_Zwrotnica_obrotowa
        
        else:
            set_marker(113,4, 0) #TKZin_Potw_Zwrotnica_obrotowa
       
    if TKZq_Zwrotnica_obrotowa:
        if index == 0:
            set_marker(107,3, 1) #TKZin_Silos150
        elif index == 1:
            set_marker(107,3, 0) #TKZin_Silos150
        elif index == 2:    
            set_marker(107,4, 1) #TKZin_Silos151
        elif index == 3:
            set_marker(107,4, 0) #TKZin_Silos151
        elif index == 4:
            set_marker(107,5, 1) #TKZin_Silos152
        elif index == 5:
            set_marker(107,5, 0) #TKZin_Silos152
        elif index == 6:
            set_marker(107,6, 1) #TKZin_Silos153
        elif index == 7:
            set_marker(107,6, 0) #TKZin_Silos153
        elif index == 8:
            set_marker(107,7, 1) #TKZin_Silos154
        elif index == 9:
            set_marker(107,7, 0) #TKZin_Silos154
        elif index == 10:
            set_marker(108,0, 1) #TKZin_Silos155
        elif index == 11:
            set_marker(108,0, 0) #TKZin_Silos155
        elif index == 12:
            set_marker(108,1, 1) #TKZin_Silos156
        elif index == 13:
            set_marker(108,1, 0) #TKZin_Silos156
        elif index == 14:
            set_marker(108,2, 1) #TKZin_Silos157
        elif index == 15:
            set_marker(108,2, 0) #TKZin_Silos157
        elif index == 16:
            set_marker(108,3, 1) #TKZin_Silos158
        elif index == 17:
            set_marker(108,3, 0) #TKZin_Silos158
        elif index == 18:
            set_marker(108,4, 1) #TKZin_Silos159
        elif index == 19:
            set_marker(108,4, 0) #TKZin_Silos159
        elif index == 20:
            set_marker(108,5, 1) #TKZin_Silos160
        elif index == 21:
            set_marker(108,5, 0) #TKZin_Silos160
        
        index+=1
        if index == 22: 
            index = 0
    
    #TKU
    if TKUq_Dmuchawa_3_old != TKUq_Dmuchawa_3:        
        if TKUq_Dmuchawa_3:
            set_marker(215,0, 1) #TKUin_Potw_Dmuchawa3
        else:
            set_marker(215,0, 0) #TKUin_Potw_Dmuchawa3
            
    if TKUq_Kubełkowy_3_old != TKUq_Kubełkowy_3:        
        if TKUq_Kubełkowy_3:
            set_marker(200,7, 1) #TKUin_Potw_Kubełkowy3
        else:
            set_marker(200,7, 0) #TKUin_Potw_Kubełkowy3
            
    if TKUq_Kubełkowy_4_old != TKUq_Kubełkowy_4:        
        if TKUq_Kubełkowy_4:
            set_marker(201,4, 1) #TKUin_Potw_Kubełkowy4
        else:
            set_marker(201,4, 0) #TKUin_Potw_Kubełkowy4
            
    if TKUq_Odkamieniacz_old != TKUq_Odkamieniacz:        
        if TKUq_Odkamieniacz:
            set_marker(203,0, 1) #TKUin_Potw_Odkamieniacz
        else:
            set_marker(203,0, 0) #TKUin_Potw_Odkamieniacz
            
    if TKUq_Śluza_3_old != TKUq_Śluza_3:        
        if TKUq_Śluza_3:
            set_marker(215,5, 1) #TKUin_Potw_Śluza3
        else:
            set_marker(215,5, 0) #TKUin_Potw_Śluza3
            
    if TKUq_Transporter_DodatkoweSilosy_old != TKUq_Transporter_DodatkoweSilosy:        
        if TKUq_Transporter_DodatkoweSilosy:
            set_marker(209,4, 1) #TKUin_Potw_Transport_DodatkSilosy
        else:
            set_marker(209,4, 0) #TKUin_Potw_Transport_DodatkSilosy
            
    if TKUq_Transporter_PodstawoweSilosy_old != TKUq_Transporter_PodstawoweSilosy:        
        if TKUq_Transporter_PodstawoweSilosy:
            set_marker(209,0, 1) #TKUin_Potw_Transport_PodstSilosy
        else:
            set_marker(209,0, 0) #TKUin_Potw_Transport_PodstSilosy
            
    if TKUq_Zasuwa_250_old != TKUq_Zasuwa_250:          
        if TKUq_Zasuwa_250:
            set_marker(211,3, 0) #TKUin_Zasuwa_250_zamknięta
            time.sleep(1)
            set_marker(211,2, 1) #TKUin_Zasuwa_250_otwarta
            TKUin_Zasuwa_250_otwarta = True
        else:
            set_marker(211,2, 0) #TKUin_Zasuwa_250_otwarta
            TKUin_Zasuwa_250_otwarta = False
            time.sleep(1)
            set_marker(211,3, 1) #TKUin_Zasuwa_250_zamknięta
            
    if TKUq_Zasuwa_251_old != TKUq_Zasuwa_251:          
        if TKUq_Zasuwa_251:
            set_marker(211,5, 0) #TKUin_Zasuwa_251_zamknięta
            time.sleep(1)
            set_marker(211,4, 1) #TKUin_Zasuwa_251_otwarta
            TKUin_Zasuwa_251_otwarta = True
        else:
            set_marker(211,4, 0) #TKUin_Zasuwa_251_otwarta
            TKUin_Zasuwa_251_otwarta = False
            time.sleep(1)
            set_marker(211,5, 1) #TKUin_Zasuwa_251_zamknięta
            
    if TKUq_Zasuwa_252_old != TKUq_Zasuwa_252:          
        if TKUq_Zasuwa_252:
            set_marker(211,7, 0) #TKUin_Zasuwa_252_zamknięta
            time.sleep(1)
            set_marker(211,6, 1) #TKUin_Zasuwa_252_otwarta
            TKUin_Zasuwa_252_otwarta = True
        else:
            set_marker(211,6, 0) #TKUin_Zasuwa_252_otwarta
            TKUin_Zasuwa_252_otwarta = False
            time.sleep(1)
            set_marker(211,7, 1) #TKUin_Zasuwa_252_zamknięta
            
    if TKUq_Zasuwa_253_old != TKUq_Zasuwa_253:          
        if TKUq_Zasuwa_253:
            set_marker(212,1, 0) #TKUin_Zasuwa_253_zamknięta
            time.sleep(1)
            set_marker(212,0, 1) #TKUin_Zasuwa_253_otwarta
            TKUin_Zasuwa_253_otwarta = True
        else:
            set_marker(212,0, 0) #TKUin_Zasuwa_253_otwarta
            TKUin_Zasuwa_253_otwarta = False
            time.sleep(1)
            set_marker(212,1, 1) #TKUin_Zasuwa_253_zamknięta
            
    if TKUq_Zasuwa_254_old != TKUq_Zasuwa_254:          
        if TKUq_Zasuwa_254:
            set_marker(212,3, 0) #TKUin_Zasuwa_254_zamknięta
            time.sleep(1)
            set_marker(212,2, 1) #TKUin_Zasuwa_254_otwarta
            TKUin_Zasuwa_254_otwarta = True
        else:
            set_marker(212,2, 0) #TKUin_Zasuwa_254_otwarta
            TKUin_Zasuwa_254_otwarta = False
            time.sleep(1)
            set_marker(212,3, 1) #TKUin_Zasuwa_254_zamknięta
            
    if TKUq_Zasuwa_255_old != TKUq_Zasuwa_255:          
        if TKUq_Zasuwa_255:
            set_marker(212,5, 0) #TKUin_Zasuwa_255_zamknięta
            time.sleep(1)
            set_marker(212,4, 1) #TKUin_Zasuwa_255_otwarta
            TKUin_Zasuwa_255_otwarta = True
        else:
            set_marker(212,4, 0) #TKUin_Zasuwa_255_otwarta
            TKUin_Zasuwa_255_otwarta = False
            time.sleep(1)
            set_marker(212,5, 1) #TKUin_Zasuwa_255_zamknięta
            
    if TKUq_Zasuwa_256_old != TKUq_Zasuwa_256:          
        if TKUq_Zasuwa_256:
            set_marker(212,7, 0) #TKUin_Zasuwa_256_zamknięta
            time.sleep(1)
            set_marker(212,6, 1) #TKUin_Zasuwa_256_otwarta
            TKUin_Zasuwa_256_otwarta = True
        else:
            set_marker(212,6, 0) #TKUin_Zasuwa_256_otwarta
            TKUin_Zasuwa_256_otwarta = False
            time.sleep(1)
            set_marker(212,7, 1) #TKUin_Zasuwa_256_zamknięta
            
    if TKUq_Zasuwa_257_old != TKUq_Zasuwa_257:          
        if TKUq_Zasuwa_257:
            set_marker(213,1, 0) #TKUin_Zasuwa_257_zamknięta
            time.sleep(1)
            set_marker(213,0, 1) #TKUin_Zasuwa_257_otwarta
            TKUin_Zasuwa_257_otwarta = True
        else:
            set_marker(213,0, 0) #TKUin_Zasuwa_257_otwarta
            TKUin_Zasuwa_257_otwarta = False
            time.sleep(1)
            set_marker(213,1, 1) #TKUin_Zasuwa_257_zamknięta
            
    if TKUq_Zasuwa_258_old != TKUq_Zasuwa_258:          
        if TKUq_Zasuwa_258:
            set_marker(213,3, 0) #TKUin_Zasuwa_258_zamknięta
            time.sleep(1)
            set_marker(213,2, 1) #TKUin_Zasuwa_258_otwarta
            TKUin_Zasuwa_258_otwarta = True
        else:
            set_marker(213,2, 0) #TKUin_Zasuwa_258_otwarta
            TKUin_Zasuwa_258_otwarta = False
            time.sleep(1)
            set_marker(213,3, 1) #TKUin_Zasuwa_258_zamknięta
            
    if TKUq_Zasuwa_259_old != TKUq_Zasuwa_259:          
        if TKUq_Zasuwa_259:
            set_marker(213,5, 0) #TKUin_Zasuwa_259_zamknięta
            time.sleep(1)
            set_marker(213,4, 1) #TKUin_Zasuwa_259_otwarta
            TKUin_Zasuwa_259_otwarta = True
        else:
            set_marker(213,4, 0) #TKUin_Zasuwa_259_otwarta
            TKUin_Zasuwa_259_otwarta = False
            time.sleep(1)
            set_marker(213,5, 1) #TKUin_Zasuwa_259_zamknięta
            
    if TKUq_Zasuwa_260_old != TKUq_Zasuwa_260:          
        if TKUq_Zasuwa_260:
            set_marker(213,7, 0) #TKUin_Zasuwa_260_zamknięta
            time.sleep(1)
            set_marker(213,6, 1) #TKUin_Zasuwa_260_otwarta
            TKUin_Zasuwa_260_otwarta = True
        else:
            set_marker(213,6, 0) #TKUin_Zasuwa_260_otwarta
            TKUin_Zasuwa_260_otwarta = False
            time.sleep(1)
            set_marker(213,7, 1) #TKUin_Zasuwa_260_zamknięta
            
    if TKUq_Zasuwa_nad_waga3_old != TKUq_Zasuwa_nad_waga3:          
        if TKUq_Zasuwa_nad_waga3:
            set_marker(202,0, 0) #TKUin_Zasuwa_nad_waga3_zamknięta
            time.sleep(1)
            set_marker(201,7, 1) #TKUin_Zasuwa_nad_waga3_otwarta
            TKUin_Zasuwa_nad_waga3_otwarta = True
        else:
            set_marker(201,7, 0) #TKUin_Zasuwa_nad_waga3_otwarta
            TKUin_Zasuwa_nad_waga3_otwarta = False
            time.sleep(1)
            set_marker(202,0, 1) #TKUin_Zasuwa_nad_waga3_zamknięta
            
    if TKUq_Zasuwa_pod_waga3_old != TKUq_Zasuwa_pod_waga3:          
        if TKUq_Zasuwa_pod_waga3:
            set_marker(202,3, 0) #TKUin_Zasuwa_pod_waga3_zamknięta
            time.sleep(1)
            set_marker(202,2, 1) #TKUin_Zasuwa_pod_waga3_otwarta
            TKUin_Zasuwa_pod_waga3_otwarta = True
        else:
            set_marker(202,2, 0) #TKUin_Zasuwa_pod_waga3_otwarta
            TKUin_Zasuwa_pod_waga3_otwarta = False
            time.sleep(1)
            set_marker(202,3, 1) #TKUin_Zasuwa_pod_waga3_zamknięta
            
    if TKUq_Zasuwa_pod_waga4_old != TKUq_Zasuwa_pod_waga4:          
        if TKUq_Zasuwa_pod_waga4:
            set_marker(214,1, 0) #TKUin_Zasuwa_pod_waga4_zamknięta
            time.sleep(1)
            set_marker(214,0, 1) #TKUin_Zasuwa_pod_waga4_otwarta
            TKUin_Zasuwa_pod_waga4_otwarta = True
        else:
            set_marker(214,0, 0) #TKUin_Zasuwa_pod_waga4_otwarta
            TKUin_Zasuwa_pod_waga4_otwarta = False
            time.sleep(1)
            set_marker(214,1, 1) #TKUin_Zasuwa_pod_waga4_zamknięta
            
    if TKUq_Zasuwa_pod_zb_zwrotu_old != TKUq_Zasuwa_pod_zb_zwrotu:          
        if TKUq_Zasuwa_pod_zb_zwrotu:
            set_marker(203,7, 0) #TKUin_Zasuwa_pod_zb_zwrotu_zamknięta
            time.sleep(1)
            set_marker(203,6, 1) #TKUin_Zasuwa_pod_zb_zwrotu_otwarta       
        else:
            set_marker(203,6, 0) #TKUin_Zasuwa_pod_zb_zwrotu_otwarta
            time.sleep(1)
            set_marker(203,7, 1) #TKUin_Zasuwa_pod_zb_zwrotu_zamknięta
            
    if TKUq_ZsypNa250_old != TKUq_ZsypNa250:          
        if TKUq_ZsypNa250:
            set_marker(207,2, 0) #TKUin_ZsypNa250_Schowany
            time.sleep(1)
            set_marker(205,7, 1) #TKUin_ZsypNa250       
        else:
            set_marker(205,7, 0) #TKUin_ZsypNa250
            time.sleep(1)
            set_marker(207,2, 1) #TKUin_ZsypNa250_Schowany
            
    if TKUq_ZsypNa251_old != TKUq_ZsypNa251:          
        if TKUq_ZsypNa251:
            set_marker(207,3, 0) #TKUin_ZsypNa251_Schowany
            time.sleep(1)
            set_marker(206,0, 1) #TKUin_ZsypNa251       
        else:
            set_marker(206,0, 0) #TKUin_ZsypNa251
            time.sleep(1)
            set_marker(207,3, 1) #TKUin_ZsypNa251_Schowany
            
    if TKUq_ZsypNa252_old != TKUq_ZsypNa252:          
        if TKUq_ZsypNa252:
            set_marker(207,4, 0) #TKUin_ZsypNa252_Schowany
            time.sleep(1)
            set_marker(206,1, 1) #TKUin_ZsypNa252       
        else:
            set_marker(206,1, 0) #TKUin_ZsypNa252
            time.sleep(1)
            set_marker(207,4, 1) #TKUin_ZsypNa252_Schowany
            
    if TKUq_ZsypNa253_old != TKUq_ZsypNa253:          
        if TKUq_ZsypNa253:
            set_marker(207,5, 0) #TKUin_ZsypNa253_Schowany
            time.sleep(1)
            set_marker(206,2, 1) #TKUin_ZsypNa253       
        else:
            set_marker(206,2, 0) #TKUin_ZsypNa253
            time.sleep(1)
            set_marker(207,5, 1) #TKUin_ZsypNa253_Schowany
            
    if TKUq_ZsypNa254_old != TKUq_ZsypNa254:          
        if TKUq_ZsypNa254:
            set_marker(207,6, 0) #TKUin_ZsypNa254_Schowany
            time.sleep(1)
            set_marker(206,3, 1) #TKUin_ZsypNa254       
        else:
            set_marker(206,3, 0) #TKUin_ZsypNa254
            time.sleep(1)
            set_marker(207,6, 1) #TKUin_ZsypNa254_Schowany
            
    if TKUq_ZsypNa255_old != TKUq_ZsypNa255:          
        if TKUq_ZsypNa255:
            set_marker(207,7, 0) #TKUin_ZsypNa255_Schowany
            time.sleep(1)
            set_marker(206,4, 1) #TKUin_ZsypNa255       
        else:
            set_marker(206,4, 0) #TKUin_ZsypNa255
            time.sleep(1)
            set_marker(207,7, 1) #TKUin_ZsypNa255_Schowany
            
    if TKUq_ZsypNa256_old != TKUq_ZsypNa256:          
        if TKUq_ZsypNa256:
            set_marker(208,0, 0) #TKUin_ZsypNa256_Schowany
            time.sleep(1)
            set_marker(206,5, 1) #TKUin_ZsypNa256       
        else:
            set_marker(206,5, 0) #TKUin_ZsypNa256
            time.sleep(1)
            set_marker(208,0, 1) #TKUin_ZsypNa256_Schowany
            
    if TKUq_ZsypNa257_old != TKUq_ZsypNa257:          
        if TKUq_ZsypNa257:
            set_marker(208,1, 0) #TKUin_ZsypNa257_Schowany
            time.sleep(1)
            set_marker(206,6, 1) #TKUin_ZsypNa257       
        else:
            set_marker(206,6, 0) #TKUin_ZsypNa257
            time.sleep(1)
            set_marker(208,1, 1) #TKUin_ZsypNa257_Schowany
            
    if TKUq_ZsypNa258_old != TKUq_ZsypNa258:          
        if TKUq_ZsypNa258:
            set_marker(208,2, 0) #TKUin_ZsypNa258_Schowany
            time.sleep(1)
            set_marker(206,7, 1) #TKUin_ZsypNa258       
        else:
            set_marker(206,7, 0) #TKUin_ZsypNa258
            time.sleep(1)
            set_marker(208,2, 1) #TKUin_ZsypNa258_Schowany
            
    if TKUq_ZsypNa259_old != TKUq_ZsypNa259:          
        if TKUq_ZsypNa259:
            set_marker(208,3, 0) #TKUin_ZsypNa259_Schowany
            time.sleep(1)
            set_marker(207,0, 1) #TKUin_ZsypNa259       
        else:
            set_marker(207,0, 0) #TKUin_ZsypNa259
            time.sleep(1)
            set_marker(208,3, 1) #TKUin_ZsypNa259_Schowany
            
    if TKUq_ZsypNa260_old != TKUq_ZsypNa260:          
        if TKUq_ZsypNa260:
            set_marker(208,4, 0) #TKUin_ZsypNa260_Schowany
            time.sleep(1)
            set_marker(207,1, 1) #TKUin_ZsypNa260       
        else:
            set_marker(207,1, 0) #TKUin_ZsypNa260
            time.sleep(1)
            set_marker(208,4, 1) #TKUin_ZsypNa260_Schowany
            
    if TKUq_Zwrotnica_bypass_old != TKUq_Zwrotnica_bypass:          
        if TKUq_Zwrotnica_bypass:
            set_marker(203,3, 0) #TKUin_Zwrotnica_na_odkamieniacz
            time.sleep(1)
            set_marker(203,4, 1) #TKUin_Zwrotnica_na_Bypass       
        else:
            set_marker(203,4, 0) #TKUin_Zwrotnica_na_Bypass
            time.sleep(1)
            set_marker(203,3, 1) #TKUin_Zwrotnica_na_odkamieniacz
            
    if TKUq_Zwrotnica_NaDodatkoweSilosy_old != TKUq_Zwrotnica_NaDodatkoweSilosy:          
        if TKUq_Zwrotnica_NaDodatkoweSilosy:
            set_marker(204,3, 0) #TKUin_Zwrotnica_PodstawoweSilosy
            time.sleep(1)
            set_marker(204,2, 1) #TKUin_Zwrotnica_DodatkoweSilosy       
        else:
            set_marker(204,2, 0) #TKUin_Zwrotnica_DodatkoweSilosy
            time.sleep(1)
            set_marker(204,3, 1) #TKUin_Zwrotnica_PodstawoweSilosy
            
    if TKUq_Zwrotnica_NaKontener_old != TKUq_Zwrotnica_NaKontener:          
        if TKUq_Zwrotnica_NaKontener:
            set_marker(214,4, 0) #TKUin_Zwrotnica_NaTransport_NaMłyny
            time.sleep(1)
            set_marker(214,3, 1) #TKUin_Zwrotnica_NaKontener       
        else:
            set_marker(214,3, 0) #TKUin_Zwrotnica_NaKontener
            time.sleep(1)
            set_marker(214,4, 1) #TKUin_Zwrotnica_NaTransport_NaMłyny
            
    if TKUq_Zwrotnica_NaMłyny2_old != TKUq_Zwrotnica_NaMłyny2:          
        if TKUq_Zwrotnica_NaMłyny2:
            set_marker(216,1, 0) #TKUin_Zwrotnica_NaMłyn1
            time.sleep(1)
            set_marker(216,2, 1) #TKUin_Zwrotnica_NaMłyn2       
        else:
            set_marker(216,2, 0) #TKUin_Zwrotnica_NaMłyn2
            time.sleep(1)
            set_marker(216,1, 1) #TKUin_Zwrotnica_NaMłyn1
            
    if TKUq_Zwrotnica_NaZwrot_old != TKUq_Zwrotnica_NaZwrot:          
        if TKUq_Zwrotnica_NaZwrot:
            set_marker(216,5, 0) #TKUin_Zwrotnica_NaNastępZwrotnice
            time.sleep(1)
            set_marker(216,4, 1) #TKUin_Zwrotnica_NaZwrot       
        else:
            set_marker(216,4, 0) #TKUin_Zwrotnica_NaZwrot
            time.sleep(1)
            set_marker(216,5, 1) #TKUin_Zwrotnica_NaNastępZwrotnice
            

            


    #TKM
    if TKMq_Bączek1_old != TKMq_Bączek1:        
        if TKMq_Bączek1:
            set_marker(302,0, 1) #TKMin_Potw_Bączek1
        else:
            set_marker(302,0, 0) #TKMin_Potw_Bączek1
            
    if TKMq_Bączek2_old != TKMq_Bączek2:        
        if TKMq_Bączek2:
            set_marker(306,1, 1) #TKMin_Potw_Bączek2
        else:
            set_marker(306,1, 0) #TKMin_Potw_Bączek2
            
    if TKMq_Chłodnica1_old != TKMq_Chłodnica1:        
        if TKMq_Chłodnica1:
            set_marker(304,0, 1) #TKMin_Potw_Chłodnica1
        else:
            set_marker(304,0, 0) #TKMin_Potw_Chłodnica1
            
    if TKMq_Chłodnica2_old != TKMq_Chłodnica2:        
        if TKMq_Chłodnica2:
            set_marker(308,1, 1) #TKMin_Potw_Chłodnica2
        else:
            set_marker(308,1, 0) #TKMin_Potw_Chłodnica1
            
    if TKMq_Dmuchawa1_old != TKMq_Dmuchawa1:        
        if TKMq_Dmuchawa1:
            set_marker(303,4, 1) #TKMin_Potw_Dmuchawa1
        else:
            set_marker(303,4, 0) #TKMin_Potw_Dmuchawa1
            
    if TKMq_Dmuchawa2_old != TKMq_Dmuchawa2:        
        if TKMq_Dmuchawa2:
            set_marker(307,5, 1) #TKMin_Potw_Dmuchawa2
        else:
            set_marker(307,5, 0) #TKMin_Potw_Dmuchawa2
            
    if TKMq_Odsiewacz1_old != TKMq_Odsiewacz1:        
        if TKMq_Odsiewacz1:
            set_marker(301,0, 1) #TKMin_Potw_Odsiewacz1
        else:
            set_marker(301,0, 0) #TKMin_Potw_Odsiewacz1
            
    if TKMq_Odsiewacz2_old != TKMq_Odsiewacz2:        
        if TKMq_Odsiewacz2:
            set_marker(305,5, 1) #TKMin_Potw_Odsiewacz2
        else:
            set_marker(305,5, 0) #TKMin_Potw_Odsiewacz2
            
    if TKMq_Rekondycja1_old != TKMq_Rekondycja1:        
        if TKMq_Rekondycja1:
            set_marker(303,0, 1) #TKMin_Potw_Rekondycja1
        else:
            set_marker(303,0, 0) #TKMin_Potw_Rekondycja1
            
    if TKMq_Rekondycja2_old != TKMq_Rekondycja2:        
        if TKMq_Rekondycja2:
            set_marker(307,1, 1) #TKMin_Potw_Rekondycja2
        else:
            set_marker(307,1, 0) #TKMin_Potw_Rekondycja2
            
    if TKMq_Śluza1_old != TKMq_Śluza1:        
        if TKMq_Śluza1:
            set_marker(302,4, 1) #TKMin_Potw_Śluza1
        else:
            set_marker(302,4, 0) #TKMin_Potw_Śluza1
            
    if TKMq_Śluza2_old != TKMq_Śluza2:        
        if TKMq_Śluza2:
            set_marker(306,5, 1) #TKMin_Potw_Śluza2
        else:
            set_marker(306,5, 0) #TKMin_Potw_Śluza2
            
    if TKMq_Włącz_Młyn1_old != TKMq_Włącz_Młyn1:        
        if TKMq_Włącz_Młyn1:
            set_marker(301,2, 1) #TKMin_Mielenie_Młyn1
        else:
            set_marker(301,2, 0) #TKMin_Mielenie_Młyn1
            
    if TKMq_Włącz_Młyn2_old != TKMq_Włącz_Młyn2:        
        if TKMq_Włącz_Młyn2:
            set_marker(304,7, 1) #TKMin_Mielenie_Młyn2
        else:
            set_marker(304,7, 0) #TKMin_Mielenie_Młyn2
            
    if TKMq_Zasuwa_nad_młynem1_old != TKMq_Zasuwa_nad_młynem1:          
        if TKMq_Zasuwa_nad_młynem1:
            set_marker(300,4, 0) #TKMin_Zasuwa_nad_młynem1_zamknięta
            time.sleep(1)
            set_marker(300,3, 1) #TKMin_Zasuwa_nad_młynem1_otwarta        
        else:
            set_marker(300,3, 0) #TKMin_Zasuwa_nad_młynem1_otwarta
            time.sleep(1)
            set_marker(300,4, 1) #TKMin_Zasuwa_nad_młynem1_zamknięta
            
    if TKMq_Zasuwa_nad_młynem2_old != TKMq_Zasuwa_nad_młynem2:          
        if TKMq_Zasuwa_nad_młynem2:
            set_marker(304,5, 0) #TKMin_Zasuwa_nad_młynem2_zamknięta
            time.sleep(1)
            set_marker(304,4, 1) #TKMin_Zasuwa_nad_młynem2_otwarta       
        else:
            set_marker(304,4, 0) #TKMin_Zasuwa_nad_młynem2_otwarta
            time.sleep(1)
            set_marker(304,5, 1) #TKMin_Zasuwa_nad_młynem2_zamknięta
            
    if TKMq_Zwrotnica_401_402_old != TKMq_Zwrotnica_401_402:          
        if TKMq_Zwrotnica_401_402:
            set_marker(308,3, 0) #TKMin_Zwrotnica_Na401
            time.sleep(1)
            set_marker(308,4, 1) #TKMin_Zwrotnica_Na402       
        else:
            set_marker(308,4, 0) #TKMin_Zwrotnica_Na402
            time.sleep(1)
            set_marker(308,3, 1) #TKMin_Zwrotnica_Na401
            
    if TKMq_Zwrotnica_403_404_old != TKMq_Zwrotnica_403_404:          
        if TKMq_Zwrotnica_403_404:
            set_marker(308,6, 0) #TKMin_Zwrotnica_Na403
            time.sleep(1)
            set_marker(308,7, 1) #TKMin_Zwrotnica_Na404       
        else:
            set_marker(308,7, 0) #TKMin_Zwrotnica_Na404
            time.sleep(1)
            set_marker(308,6, 1) #TKMin_Zwrotnica_Na403
            
    if TKMq_Zwrotnica_405_406_old != TKMq_Zwrotnica_405_406:          
        if TKMq_Zwrotnica_405_406:
            set_marker(309,1, 0) #TKMin_Zwrotnica_Na405
            time.sleep(1)
            set_marker(309,2, 1) #TKMin_Zwrotnica_Na406       
        else:
            set_marker(309,2, 0) #TKMin_Zwrotnica_Na406
            time.sleep(1)
            set_marker(309,1, 1) #TKMin_Zwrotnica_Na405
            
    if TKMq_Zwrotnica_407_408_old != TKMq_Zwrotnica_407_408:          
        if TKMq_Zwrotnica_407_408:
            set_marker(309,4, 0) #TKMin_Zwrotnica_Na407
            time.sleep(1)
            set_marker(309,5, 1) #TKMin_Zwrotnica_Na408       
        else:
            set_marker(309,5, 0) #TKMin_Zwrotnica_Na408
            time.sleep(1)
            set_marker(309,4, 1) #TKMin_Zwrotnica_Na407
            
    if TKMq_Zwrotnica_409_410_old != TKMq_Zwrotnica_409_410:          
        if TKMq_Zwrotnica_409_410:
            set_marker(309,7, 0) #TKMin_Zwrotnica_Na409
            time.sleep(1)
            set_marker(310,0, 1) #TKMin_Zwrotnica_Na410       
        else:
            set_marker(310,0, 0) #TKMin_Zwrotnica_Na410
            time.sleep(1)
            set_marker(309,7, 1) #TKMin_Zwrotnica_Na409
            
    
    #Symulacja wag
            
    waga1_old = waga1
    waga2_old = waga2
    waga3_old = waga3
    waga4_old = waga4
    
    
    if TKZin_Zasuwa_nad_waga1_otwarta and TKZq_Kubełkowy_2==1:
        waga1 += 5
    
    if TKZin_Zasuwa_pod_waga1_otwarta:
        if waga1 <= 0:
            waga1 = 0
        else:
            waga1 -= 5
        
        
    if TKZin_Zasuwa_150_otwarta or TKZin_Zasuwa_151_otwarta or TKZin_Zasuwa_152_otwarta or TKZin_Zasuwa_153_otwarta or TKZin_Zasuwa_154_otwarta or TKZin_Zasuwa_155_otwarta or TKZin_Zasuwa_156_otwarta or TKZin_Zasuwa_157_otwarta or TKZin_Zasuwa_158_otwarta or TKZin_Zasuwa_159_otwarta or TKZin_Zasuwa_160_otwarta:
        waga2 += 5
    
    if TKZin_Zasuwa_pod_waga2_otwarta:
        if waga2 <= 0:
            waga2 = 0
        else:
            waga2 -= 5
        
        
    if TKUin_Zasuwa_nad_waga3_otwarta:
        waga3 += 5
    
    if TKUin_Zasuwa_pod_waga3_otwarta:
        if waga3 <= 0:
            waga3 = 0
        else:
            waga3 -= 5
    
    
    if TKUin_Zasuwa_250_otwarta or TKUin_Zasuwa_251_otwarta or TKUin_Zasuwa_252_otwarta or TKUin_Zasuwa_253_otwarta or TKUin_Zasuwa_254_otwarta or TKUin_Zasuwa_255_otwarta or TKUin_Zasuwa_256_otwarta or TKUin_Zasuwa_257_otwarta or TKUin_Zasuwa_258_otwarta or TKUin_Zasuwa_259_otwarta or TKUin_Zasuwa_260_otwarta:
        waga4 += 5
    
    if TKUin_Zasuwa_pod_waga4_otwarta:
        if waga4 <= 0:
            waga4 = 0
        else:
            waga4 -= 5
    
    if waga1_old != waga1:
        set_merkers(myplc, 4, 0, S7WLWord, waga1) #MW8 Sym_Waga_1
    
    if waga2_old != waga2:
        set_merkers(myplc, 6, 0, S7WLWord, waga2) #MW10 Sym_Waga_2
        
    if waga3_old != waga3:
        set_merkers(myplc, 8, 0, S7WLWord, waga3) #MW12 Sym_Waga_3
        
    if waga4_old != waga4:
        set_merkers(myplc, 10, 0, S7WLWord, waga4)#MW14 Sym_Waga_4   
    
    
    
    
    if gotowy:
        print('Symulator gotowy do pracy')
        print('Ctrl+C aby przerwac symulacje')
        gotowy = False
        
    #set_merkers(myplc, 12, 0, S7WLWord, waga1)#MW16 Nr_Kawy
    
    
    #czas = time.clock()-start
    #print('Czas wykonywania petli: ',czas)
    #print('Iteracja')
    time.sleep(1)
