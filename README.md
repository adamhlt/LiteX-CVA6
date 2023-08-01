```
                            __    _ __      _  __    _______    _____   _____ 
                           / /   (_) /____ | |/ /   / ____/ |  / /   | / ___/
                          / /   / / __/ _ \|   /   / /    | | / / /| |/ __ \ 
                         / /___/ / /_/  __/   |   / /___  | |/ / ___ / /_/ /
                        /_____/_/\__/\___/_/|_|   \____/  |___/_/  |_\____/
                                                                          
                                                                        
                                            LiteX CVA6 
                       Fixed integration of the CPU into LiteX SoC generator
```
<p align="center">
    <img src="https://img.shields.io/badge/Library-LiteX-red.svg?style=for-the-badge&logo=appveyor" alt="LiteX">
    <img src="https://img.shields.io/badge/CPU-CVA6-yellow.svg?style=for-the-badge&logo=appveyor" alt="CVA6">
</p> 

## :book: Project Overview :

This project is a fixed version of the existing CVA6 pythondata-cpu-cva6 necessary for LiteX SoC generation.
Most of the work was done by the team in charge of the CPU integration in LiteX.

## :rocket: Getting Started :

#### Clone the project 

Clone the project into your LiteX installation's root folder.

```console
git clone https://github.com/adamhlt/LiteX-CVA6.git pythondata-cpu-cva6
python3 -m pip install --editable pythondata-cpu-cva6
```

You can now try to run the simulation.

```console
litex_sim --cpu-type=cva6
```

## 🧪 Demonstration :

LiteX Simulation of CVA6 CPU.

<img width="435" alt="Demo" src="https://user-images.githubusercontent.com/48086737/218577012-4533dbf2-bd4c-4f00-92cf-130594f23355.png">


## :crown: Credit :

- [LiteX](https://github.com/enjoy-digital/litex) : Very powerful SoC generator.
- [Original Repo](https://github.com/litex-hub/pythondata-cpu-cva6) : Initial repository of the CVA6 integration into LiteX.
- [CVA6 Repo](https://github.com/openhwgroup/cva6) : Official repository of CVA6 CPU.
