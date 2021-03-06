from bvareader import reader
from bvareader import plotter
from bvareader import preprocessing

pd_bva = reader.read_positions("tests/test_data/new_bva/example_bva.xml")
plotter.plot_triangle(pd_bva, 1000)

pd_bva2 = preprocessing.prepare_position(pd_bva)

reader.save_csv(pd_bva2, "bva.csv")
reader.save_csv(pd_bva, "bva_full.csv")

pd_sync = reader.read_sync_file("tests/test_data/new_bva/exampl_sync.csv")
reader.save_csv(pd_sync, "sync.csv")


# Old

pd_bva = reader.read_positions("tests/test_data/old_bva/test.TR3")
pd_bva2 = preprocessing.prepare_position(pd_bva)
