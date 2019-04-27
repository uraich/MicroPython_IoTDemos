#!/usr/bin/python3
red=(b'v1/7c70a330-69af-11e8-a76a-fdebb8d0010d/things/dae86710-4ae9-11e9-a6b5-e30ec853fbf2/cmd/2', b'uvtDurLwnJnpGqE,112')
green=(b'v1/7c70a330-69af-11e8-a76a-fdebb8d0010d/things/dae86710-4ae9-11e9-a6b5-e30ec853fbf2/cmd/3', b'qoyp13qyz3tznnp,163')
blue=(b'v1/7c70a330-69af-11e8-a76a-fdebb8d0010d/things/dae86710-4ae9-11e9-a6b5-e30ec853fbf2/cmd/4', b'HKupHKDqsz6o5Dt,150')
print(red[0])
channelIndex=red[0].index(b'cmd')+4
print(channelIndex)
channel = int(red[0][channelIndex:])
print("Channel: %d"%channel)
valueIndex=red[1].index(b',')+1
value=int(red[1][valueIndex:])
print("value: %d"%value)
print(green)
print(blue)

