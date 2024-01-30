[app]

title = Test App
package.name = testapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3==3.8.0, kivy==2.3.0
p4a.branch = release-2022.12.20

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2
