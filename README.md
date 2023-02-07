<div align="center">
    <h1>Deprem Backend</h1>
    <img src=https://user-images.githubusercontent.com/48323786/217369578-ea51f7b5-08ab-4fcb-aa3e-c6e3f6a2d1cf.png>
    <h3>Basit arayüzlü Deprem projesinin backendi.</h3>
</div>

<br>

# İçerikler
- [1. Kurulum](#kurulum)
- [2. Kullanışı](#kullanışı)
- [3. Lisans](#lisans)

#  Kurulum
```zsh
$ pip install -r requirements.txt
$ pre-commit install
```

#  Kullanışı
### /select_options

```zsh
$ curl --location --request GET 'https://api.depremproje.com/select_options'

>> {"konum_il":["Adıyaman ","Malatya","Kahramanmaraş","Hatay","Adana","Adıyaman","Osmaniye","Diyarbakır","Gaziantep","Şanlıurfa"],"konum_ilce":["Afşin","Yeşilyurt","Merkez","Dörtyol","Onikişubat","Antakya","merkez","Şahinbey","Yenişehir","Nurhak","Doğanşehir","Gölbaşı","Kırıkhan","Battalgazi","Elb

...

Caddesi","Müftülük Sokak","Şehit Bülent Yüce Sokak","51001 Sokak","Uğur Mumcu Caddesi","Dumlupınar Sk."]
```

### /get_user_parameters
```zsh
$ curl --location --request GET 'https://api.depremproje.com/get_user_parameters' \
--header 'Content-Type: application/json' \
--data-raw '{
    "konum_il": "Hatay",
    "konum_mahalle": "Ekinci Mahallesi"
}'

>> [
    {
        "_id": "63e24520f141caf529b4811d",
        "konum_il": "Hatay",
        "konum_ilce": "Antakya",
        "konum_mahalle": "Ekinci Mahallesi",
        "isimsoyisim": "fatih kales",
        "kisi_sayisi": "1",
        "telefon": "Bilgi yok",
        "adres": "şehit bilgin sokak no:1/33",
        "apartman": "Bilgi yok",
        "sokak": "Şehit Bilgin Sokak",
        "blok_no": "No: 1/33",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": 36.1837802,
        "lon": 36.1241276
    },
    ...
    {
        "_id": "63e24520f141caf529b4815c",
        "konum_il": "Hatay",
        "konum_ilce": "Antakya",
        "konum_mahalle": "Ekinci Mahallesi",
        "isimsoyisim": "Tolga Kartay Eşi ve Çocuğu",
        "kisi_sayisi": "2",
        "telefon": "Bilgi yok",
        "adres": "İnönü Bulvarı Elit Apartmanı no 94",
        "apartman": "Elit Apartmanı",
        "sokak": "İnönü Bulvar",
        "blok_no": "Bilgi yok",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": 36.2360758,
        "lon": 36.1457342
    }
]
```

### /get_users_lat_lon
```zsh
$ curl --location --request GET 'https://api.depremproje.com/get_users_lat_lon'

>> [
    {
        "_id": "63e24520f141caf529b480d1",
        "konum_il": "Hatay",
        "konum_ilce": "Antakya",
        "konum_mahalle": "Odabaşı Mahallesi",
        "isimsoyisim": "Müfit-Çimen-İbrahim İkbal Bayramoğlu",
        "kisi_sayisi": "4",
        "telefon": "05357643753",
        "adres": "Uğur Mumcu Cd. No:66 Eskiocak Eczanesi Binası",
        "apartman": "Eskiocak Eczanesi Binası",
        "sokak": "Uğur Mumcu Caddesi",
        "blok_no": "66",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": 36.23186099999999,
        "lon": 36.16499640000001
    },
    ...
    {
        "_id": "63e24520f141caf529b480d3",
        "konum_il": "Hatay",
        "konum_ilce": "Antakya",
        "konum_mahalle": "Ürgen Paşa Mahallesi",
        "isimsoyisim": "Ayhan yapıcı ",
        "kisi_sayisi": "1",
        "telefon": "Bilgi yok",
        "adres": "Ürgenpaşa mah. 75. Yıl bulvarı 31030 akparti başkanlığı Ogün sor apt  Gündüz eczanesinin binası",
        "apartman": "Ogün Sor Apartmanı",
        "sokak": "75. Yıl Bulvar",
        "blok_no": "31030",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": 36.2236581,
        "lon": 36.1587816
    }
]
```

### /get_users
```zsh
$ curl --location --request GET 'https://api.depremproje.com/get_users'


>> [
    {
        "_id": "63e24520f141caf529b480d1",
        "konum_il": "Hatay",
        "konum_ilce": "Antakya",
        "konum_mahalle": "Odabaşı Mahallesi",
        "isimsoyisim": "Müfit-Çimen-İbrahim İkbal Bayramoğlu",
        "kisi_sayisi": "4",
        "telefon": "05357643753",
        "adres": "Uğur Mumcu Cd. No:66 Eskiocak Eczanesi Binası",
        "apartman": "Eskiocak Eczanesi Binası",
        "sokak": "Uğur Mumcu Caddesi",
        "blok_no": "66",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": 36.23186099999999,
        "lon": 36.16499640000001
    },
    ...
    {
        "_id": "63e24520f141caf529b480d2",
        "konum_il": "Adana",
        "konum_ilce": "Çukurova",
        "konum_mahalle": "Yurt Mahallesi",
        "isimsoyisim": "Tansel, Nisa , Oya Erginkoç",
        "kisi_sayisi": "3",
        "telefon": "Bilgi yok",
        "adres": "Murat Ekin Sitesi B blok",
        "apartman": "Ekin Sitesi",
        "sokak": "Bilgi yok",
        "blok_no": "B Blok",
        "ic_kapi_no": "Bilgi yok",
        "kat": "Bilgi yok",
        "kaynak": "Bilgi yok",
        "lat": "",
        "lon": ""
    }
]

# Lisans
[GNU](LICENSE)
