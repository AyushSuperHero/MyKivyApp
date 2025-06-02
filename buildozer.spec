[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 0

[app.android]
android.api = 31
android.ndk = 25b
android.archs = armeabi-v7a,arm64-v8a
android.minapi = 21
android.build_tools_version = 34.0.0
