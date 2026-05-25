[app]
# Uygulama bilgileri
title = InaAsistan
package.name = inaasistan
package.domain = org.ina
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# Kütüphaneler (pyjnius Android ile konuşmak için şart)
requirements = python3,kivy,pyjnius

# Android ayarları
android.archs = armeabi-v7a
android.api = 31
android.minapi = 21
android.permissions = INTERNET
orientation = portrait
fullscreen = 0

# Buildozer ayarları
[buildozer]
log_level = 2
warn_on_root = 1
# SDK ve NDK otomatik indirilecek
