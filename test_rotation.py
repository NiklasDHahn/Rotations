from rotation import Rotation

r = Rotation()

omega = 91.7817837717502/200*180
phi = 44.26373573651592/200*180
kappa = 7.12546763027179/200*180

EtoBRotation = r.from_euler('xyz', [-omega, -phi, -kappa], degrees=True) 

print(EtoBRotation)