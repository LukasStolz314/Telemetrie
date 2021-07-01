# Dashboard

## Repository

[LukasStolz314/Telemetrie](https://github.com/LukasStolz314/Telemetrie.git)

## Projektvision

Das Computerspielgenre "Rennspiel" lebt von Realismus und einer guten Simulation des Fahrverhaltens. Um einen größeren Spielspaß zu entwickeln, kaufen sich die Spieler ein Lenkrad, anstatt weiter einen Controller zu benutzen. Jedoch können Lenkräder, die einen eingebauten Display (Dashboard) besitzen, schnell einen Preis von über 1000 € haben.

Unser "Racing Dashboard" bietet den Spielern einen erhöhten Realismus und damit eine Chance, sich in Rennspielen weiterzuentwickeln und besser zu werden. Indem Funktionen des Spiels F1 2020 uns ermöglichen, die aktuellen Daten wie Informationen über Wagen, Strecke, Session und Wetter abzugreifen, sind wir in der Lage, dem Spieler mit Live-Daten zu versorgen, um so den Realismus zu steigern.

Das Dashboard ist ein externes Gerät, welches dem Display eines echten Formel 1 Lenkrad ähnelt und die gleichen Funktionen zur Verfügung stellt.

## Projektbeschreibung

Die Komponenten des Dashboardes sind ein Raspberry 3 oder 4 und ein dazu passender Display. Für unser Projekt haben wir dieses Display benutzt: [https://www.amazon.de/gp/product/B07XFYXD2V/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1](https://www.amazon.de/gp/product/B07XFYXD2V/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)

Mit Hilfe eines Python-Programms verbindet sich der Rapsberry über eine UDP-Verbindung mit dem Spiel. Hierbei muss der Raspberry lediglig im selben Netzwerk sein. Daraufhin sendet das Computer die Datenpakete an das Dashboard. Dieser Datenstrom wird kodiert Diese Informationen beinhalten die Daten der aktuellen Spielsession. 

## Installation

Die Repository clonen:

```bash
git clone https://github.com/LukasStolz314/Telemetrie --recurse-submodules
```

### Voraussetzungen

- Python3
    - pygame version 2.0.1
    - f1_2020_telemetry
    - pynput

### Lokale installation

In F1 2020

- Telemetrieeinstellungen → UDP-Broadcasting: AUS
- Telemetrieeinstellungen → UDP-Addresse: 127.0.0.1

Start des Programms

```bash
python3 main.py -i 127.0.0.1 -p 20777
```

## Raspberry Pi installation

In F1 2020

- Telemetrieeinstellungen → UDP-Broadcasting: AUS
- Telemetrieeinstellungen → UDP-Addresse: Lokale IP des Raspberry Pi's im Netzwerk

Start des Programms

```bash
python3 main.py -i 0.0.0.0 -p 20777
```

## Dokumentaion

Für eine ausführliche Dokumentation des Projekts besuchen sie die [Wiki](https://github.com/isd-nunkesser/sd-2021-bolti/wiki)
