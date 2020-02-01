import fv3.utils.gt4py_utils as utils
from .translate import TranslateFortranData2Py
import fv3.stencils.ytp_v as ytpv
from fv3._config import grid


class TranslateYTP_V(TranslateFortranData2Py):
    def __init__(self, grid):
        super().__init__(grid)
        c_info = self.grid.compute_dict_buffer_2d()
        c_info['serialname'] = 'vb'
        flux_info = self.grid.compute_dict_buffer_2d()
        flux_info['serialname'] = 'ub'
        self.in_vars['data_vars'] = {'c': c_info,
                                     'u': {}, 'v': {},
                                     'flux': flux_info}
        self.in_vars['parameters'] = []
        self.out_vars = {'flux': flux_info}

    def compute(self, inputs):
        self.make_storage_data_input_vars(inputs)
        ytpv.compute(**inputs)
        return self.slice_output(inputs)
