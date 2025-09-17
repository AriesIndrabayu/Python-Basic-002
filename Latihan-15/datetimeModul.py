import datetime
from zoneinfo import ZoneInfo

# Waktu sekarang
now = datetime.datetime.now()
print("Sekarang: ", now)

# Tanggal Spesifik
ulang_tahun = datetime.date(2025, 11, 8)
print("Tanggal ulang tahun: ", ulang_tahun)

# Selisih waktu
selisih = ulang_tahun - datetime.date.today()
print("Menuju ulang tahun: ", selisih.days, "hari")

"""
1. Objek utama dari datetime
- datetime.date -> hanya tanggal saja (tahun, bulan, tanggal)
- datetime.time -> hanya waktu saja (jam, menit, detik, mikro detik)
- datetime.datetime -> gabungan tanggal dan waktu
- datetime.timedelta -> selisih waktu (durasi)
- datetime.timezone -> untuk informasi zona waktu

2. untuk mendapatkan waktu sekarang
- datetime.datetime.now()
- datetime.datetime.utcnow()
- datetime.date.today()

"""
utc = datetime.timezone.utc
dt_utc = datetime.datetime.now(utc)
print("UTC:", dt_utc)

wib = datetime.timezone(datetime.timedelta(hours=7))
dt_wib = datetime.datetime.now(wib)
print("WIB:", dt_wib)
wita = datetime.timezone(datetime.timedelta(hours=8))
# wita = ZoneInfo("Asia/Makasar")
# dt_wita = datetime.datetime.now(wita)
dt_wita = datetime.datetime.now(ZoneInfo("Asia/Jakarta"))
print("WITA:", dt_wita)

"""
pip install tzdata
"""
