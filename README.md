# PACKAGE: vittapi

interface pour une connexion entre vittascience et un raspberry pi

## Prérequis
update des paquets

``` sudo apt-get update ```

activation de l'I2C

``` sudo raspi-config ```

selectionner "3 Interface Options"
selectionner "I5 I2C"

``` sudo reboot ```

## Installation

``` sudo dpkg --build vittapi ```

``` sudo dpkg -i vittapi.deb ```

## Utilisation

l'installation du package .deb va créer un racourci dans le bureu de votre raspberry pi


