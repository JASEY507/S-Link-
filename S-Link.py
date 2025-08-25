import os
import sys
import time
import subprocess

# Otomatik modül yükleme fonksiyonu
def auto_install(lib):
    try:
        __import__(lib)
    except ImportError:
        print(f" {lib} yükleniyor...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", lib, "--break-system-packages"]
            )
        except subprocess.CalledProcessError:
            print(f"⚠ {lib} yüklenemedi, tekrar dene!")
            sys.exit(1)

# Gerekli kütüphaneler
for lib in ["requests", "pyperclip"]:
    auto_install(lib)

import requests
import pyperclip


# Animasyonlu yazı
def animated_text(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# URL kısaltma
def make_tiny(url):
    try:
        api_url = "http://tinyurl.com/api-create.php"
        response = requests.get(api_url, params={'url': url})
        if response.status_code == 200:
            return response.text
        else:
            return " Başarısız!"
    except Exception as e:
        return f" Hata: {e}"


# Panoya kopyala
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(" Link  kopyalandı!")


# Ana fonksiyon
def main():
    os.system("cls" if os.name == "nt" else "clear")
    animated_text(" Slink - Link Kısaltıcı ", 0.05)
    print("📌 Instagram: soytariomer.17\n")

    long_url = input("🔹 Kısaltmak istediğiniz linki girin: ")
    short_url = make_tiny(long_url)
    print(f"\n Kısaltılmış link: {short_url}\n")

    print("3'e basınca link panoya kopyalanacak...")
    choice = input(">> ")
    if choice.strip() == "3":
        copy_to_clipboard(short_url)


if __name__ == "__main__":
    main()
