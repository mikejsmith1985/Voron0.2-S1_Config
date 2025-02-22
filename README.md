# Voron0.2-S1
Voron0.2-S1(R1)
serial confirmation: https://discord.com/channels/460117602945990666/461153633631731712/1342265827910615175

# Notes
Voron 0.2 r1 64bit install/setup notes
Follow Eric Z Rpi setup here: https://github.com/EricZimmerman/VoronTools/blob/main/OSUpgrade.md

Follow LDO and VoronDesign docs for setting up the Pico here: 
- (LDO) https://docs.ldomotors.com/en/voron/voron02/wiring_guide_rev_a
- (VoronDesign) https://docs.vorondesign.com/build/software/skrPico_klipper.html
  - SKR Pico Serial ID: usb-Klipper_rp2040_45474150540C061A-if00
  - Frame Pico Serial ID: usb-Klipper_rp2040_3252343738082B4E-if00
  
Continue with Klipper configuration from LDO Docs here: https://docs.ldomotors.com/en/voron/voron02/wiring_guide_rev_a
- this will create and prepare the basic config file
Sensorless Homing:
- Default Stepper_x endstop_pin: ^gpio4
- Default Stepper_y endstop_pin: ^gpio3
  
- Setup automated backup of config to github via Eric Z's document
    - here:https://docs.vorondesign.com/community/howto/EricZimmerman/BackupConfigToGithub.html
    - Link to my 64bit backup Repo:
      - https://github.com/mikejsmith1985/0.2LDO64Bit.git

Move on to initial setup via voron docs here: https://docs.vorondesign.com/build/startup/
Setup the V0 Display: https://github.com/VoronDesign/Voron-Hardware/blob/master/V0_Display/Documentation/Setup_and_Flashing_Guide.md
- Display Serial ID: usb-Klipper_stm32f042x6_1D0029000B43564E32313720-if00
    -  0483:df11
