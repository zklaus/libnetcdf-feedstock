from netCDF4 import Dataset


def test_netcdf():
    nc = Dataset("test_netcdf4_python.nc", mode="w")
    nc.close()
    raise RuntimeError("Something is indeed going wrong (or right)")
