# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('src/i18n/*.json', 'src/i18n'),
    ],
    hiddenimports=['customtkinter', 'psutil', 'PIL', 'platformdirs'],
    hookspath=[],
    cipher=None,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='SysBoost',
    debug=False,
    strip=True,
    upx=True,
    console=False,
    target_arch=None,
)
app = BUNDLE(
    exe,
    name='SysBoost.app',
    bundle_identifier='com.sysboost.app',
    info_plist={
        'CFBundleShortVersionString': '0.1.0',
        'NSHighResolutionCapable': True,
    },
)
