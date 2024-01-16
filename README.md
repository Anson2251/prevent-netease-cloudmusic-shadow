# prevent-netease-cloudmusic-shadow

Prevent the shadow created by netease cloud music (`cloudmusic.exe`) running in the wine environment

The script is modified from my previous project: [`prevent-wechat-shadow`](https://github.com/Anson2251/prevent-wechat-shadow)

### **Notice**: 
- This script can effectively prevent the shadow on my computer (manjaro, xfce4, X11, Python 3.11.6, wine 8.21) with Netease Cloud Music 2.10. I can not assure it will work on other desktop environments with other versions of cloud music.

### **Suggested adjustments for wine**
- Disable the `allow window manager to decorate the controls` option in `winecfg`. 

    - The script won't be affected by this option, but in my `xfce` desktop environment, the window manager will add the title bar, which would cover the content at the top of he window.

- Install component `msctf` with `winetricks`

### Usage

example:
```bash
wine "cloudmusic.exe" & python prevent-netease-cloudmusic-shadow.py
```