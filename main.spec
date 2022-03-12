# -*- mode: python -*-

block_cipher = None


a = Analysis(['rotation.py'],
             pathex=['C:\\Users\\dwink\\coding_projects\\getrotated\\dist'],
             binaries=[],
             datas=[],
             hiddenimports=['pywintypes'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('rotated.jpg','C:\\Users\\dwink\\coding_projects\\getrotated\\images\\rotated.jpg', "DATA"),('woo.mp3','C:\\Users\\dwink\\coding_projects\\getrotated\\sounds\\woo.mp3',"DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Starfinder',
          debug=False,
          strip=False,
          upx=True,
          console=False)
