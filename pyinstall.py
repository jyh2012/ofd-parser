import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['ofd_main.py','-F','-w']
    run(opts)
