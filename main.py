"""
Aplikasi deteksi gempa terkini
"""
import deteksi_gempa

if __name__ == "__main__":
    print("Aplikasi utama")
    result = deteksi_gempa.ekstraksi_data()
    deteksi_gempa.tampilkan_data(result)