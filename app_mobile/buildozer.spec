[app]
# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py is located
source.include_exts = py,png,jpg,kv,atlas

# (list) Permissions
android.permissions = INTERNET, USE_DEVICE_ADMIN

# (str) Path to the Android NDK
ndk_path = /path/to/android-ndk-r19c

# (str) Path to the Android SDK
sdk_path = /path/to/android-sdk

# (str) Path to a custom Java file that should be compiled into your APK
android.add_src = /full/path/to/MyDeviceAdminReceiver.java

# (list) Activities to add to the Android manifest.
android.manifest.activity = com.yourpackage.MyDeviceAdminReceiver

# (list) Custom Java classes to compile
android.add_src = /full/path/to/MyDeviceAdminReceiver.java
