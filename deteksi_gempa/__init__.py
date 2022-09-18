import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    try:
        content = requests.get('https://bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        title = soup.find('title')
        print("==============================================================")

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            #print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i== 5:
                dirasakan = res.text
            i = i + 1

        print(title.text)
        hasil = dict()
        hasil["tanggal"] = tanggal  # "04 September 2022"
        hasil["waktu"] = waktu  # "04:10:14 WIB"
        hasil["magnitudo"] = magnitudo #3.1
        hasil["kedalaman"] = kedalaman #"9 Km"
        hasil["koordinat"] = {"ls": ls, "bt": bt}
        hasil["lokasi"] = lokasi #"Pusat gempa berada di laut 75 km barat daya Kab. Sukabumi"
        hasil["dirasakan"] = dirasakan #"Dirasakan (Skala MMI): II Dieng, II Banjarnegara, II Bawang (Kab. Batang)"
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("Tidak bisa menembukan gempa terkini")
        return
    print("Gempa Terakhir berdasarkan BMKG")
    print("==============================================================")
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"koordinat : LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Dirasakan : {result['dirasakan']}")
    print("==============================================================")
