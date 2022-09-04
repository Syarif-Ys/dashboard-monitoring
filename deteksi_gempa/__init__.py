import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Tanggal: 04 September 2022
    Waktu: 04:10:14 WIB
    Magnitudo: 3.1
    Kedalaman: 9 km
    Lokasi: LS=7.22  BT=109.89
    Pusat Gempa: Pusat gempa berada di darat 16 km Barat Laut WONOSOBO
    Dirasakan: Dirasakan (Skala MMI): II Dieng, II Banjarnegara, II Bawang (Kab. Batang)
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        print(content.text)
        #soup = BeautifulSoup(content)
        #print(soup.prettify())

        hasil = dict()
        hasil["tanggal"] = "04 September 2022"
        hasil["waktu"] = "04:10:14 WIB"
        hasil["magnitudo"] = 3.1
        hasil["kedalaman"] = "9 Km"
        hasil["lokasi"] = {"ls":7.22, "bt":109.89}
        hasil["pusat"] = "Pusat gempa berada di darat 16 km Barat Laut WONOSOBO"
        hasil["dirasakan"] = "Dirasakan (Skala MMI): II Dieng, II Banjarnegara, II Bawang (Kab. Batang)"
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menembukan gempa terkini")
        return
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['tanggal']}")
    print(f"Magnitudo : {result['waktu']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"pusat : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")