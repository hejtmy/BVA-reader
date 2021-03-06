from bvareader import preprocessing
from bvareader.new_bva import reader as new_reader
import pandas as pd


# NEW BVA PREPROCESSING
def test_preprocessing_new_bva(bva_xml_data_path):
    pd_bva = new_reader.read_xml_bva(bva_xml_data_path)
    pd_bva = preprocessing.prepare_position(pd_bva)
    assert isinstance(pd_bva, pd.core.frame.DataFrame)
