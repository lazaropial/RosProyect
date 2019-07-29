# RosProyect

Notas importantes

Para La RaspBerry

SIEMPRE QUE LA RASPBERRY REBOOTE A UBIQUITY

Al instalar ubiquity se deben poner los **repositorios** de:
```
UNIVERSE: sudo add-apt-repository universe
MULTIVERSE:sudo add-apt-repository multiverse
RESTRICTED: sudo add-apt-repository restricted
```
Configurar locales usando los siguientes pasos:
```
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
```
Se abrirara una ventana, darle ok a esta misma ignorando todo lo demas

