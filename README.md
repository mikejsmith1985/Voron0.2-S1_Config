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
  - Display Serial ID: usb-Klipper_stm32f042x6_1D0029000B43564E32313720-if00

Continue with Klipper configuration from LDO Docs here: https://docs.ldomotors.com/en/voron/voron02/wiring_guide_rev_a
- this will create and preparethe basic config file
- Setup automated backup of config to github via Eric Z's document
    - here:https://docs.vorondesign.com/community/howto/EricZimmerman/BackupConfigToGithub.html

Move on to initial setup via voron docs here: https://docs.vorondesign.com/build/startup/
