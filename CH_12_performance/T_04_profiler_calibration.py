import profile

if __name__ == '__main__':
    profiler = profile.Profile()
    for i in range(10):
        print(profiler.calibrate(100000))

##############################################################################

import profile


# The number here is bias calculated earlier
profile.Profile.bias = 9.809351906482531e-07

##############################################################################

import profile


profiler = profile.Profile(bias=9.809351906482531e-07)
