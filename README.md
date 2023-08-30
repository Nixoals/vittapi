# VittaPi: Raspberry Pi Interface for VittaScience

VittaPi est une interface qui facilite la communication entre VittaScience et un Raspberry Pi. Ce package est spécialement conçu pour être utilisé sur le système d'exploitation Raspberry Pi OS Bullseye.

---

## Table des matières

- [VittaPi: Raspberry Pi Interface for VittaScience](#vittapi-raspberry-pi-interface-for-vittascience)
  - [Table des matières](#table-des-matières)
  - [Configuration du système](#configuration-du-système)
  - [Prérequis](#prérequis)
    - [Mettre à jour les paquets système](#mettre-à-jour-les-paquets-système)
    - [Activer la communication I2C pour les modules Grove](#activer-la-communication-i2c-pour-les-modules-grove)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
  - [Fonctionnement](#fonctionnement)
  - [Disclaimer](#disclaimer)

---

## Configuration du système

**Système d'exploitation pris en charge :** Bullseye

---

## Prérequis

### Mettre à jour les paquets système

Exécutez la commande suivante pour mettre à jour vos paquets :

```bash
sudo apt-get update
```

### Activer la communication I2C pour les modules Grove

Si vous utilisez des modules Grove qui nécessitent une communication I2C (par exemple, LCD16x2), suivez ces étapes :

1. Accédez à la configuration du Raspberry Pi :

    ```bash
    sudo raspi-config
    ```

2. Sélectionnez "3 Interface Options".

3. Sélectionnez "I5 I2C".

4. Redémarrez le système pour que les modifications prennent effet :

    ```bash
    sudo reboot
    ```

---

## Installation

Pour installer VittaPi, suivez les étapes ci-dessous :

1. Créer le package :

    ```bash
    sudo dpkg --build vittapi
    ```

2. Installer le package :

    ```bash
    sudo dpkg -i vittapi.deb
    ```

---

## Utilisation

Après l'installation, un raccourci sera créé sur le bureau de votre Raspberry Pi. Vous pouvez soit :

- Cliquer sur ce raccourci, ce qui ouvrira une fenêtre de terminal et lancera l'interface graphique ainsi que le programme.
  
  **OU**
  
- Lancer le programme directement depuis un terminal en utilisant la commande :

    ```bash
    vittapi.sh
    ```

---

## Fonctionnement

Pour téléverser du code, il est nécessaire de spécifier le nom d'hôte de votre Raspberry Pi en utilisant un bloc `[raspberry]`. Vous pouvez également utiliser l'adresse IP de votre Raspberry Pi.

---

## Disclaimer

Ce package est en cours de développement. Des bugs peuvent être présents. Si vous en trouvez, veuillez créer une issue sur notre dépôt GitHub.

**Note de sécurité :** La communication entre vittascience.com et le Raspberry Pi est gérée via un serveur web Flask. Une connexion Internet est donc nécessaire. Veuillez noter que le protocole de communication utilise HTTP et non HTTPS. Il est recommandé de n'utiliser ce package que sur un réseau privé et sécurisé.

---

Pour toute autre question ou retour d'expérience, n'hésitez pas à nous contacter.