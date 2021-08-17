from .result_data import *

default_add_list = [
    set_country,
    set_object,
    # set_fields, todo:  сделать
    create_addin,
    set_brand,
    set_complplectation,
    set_tnved,
    set_mater_st,
    set_mater_cif,
    set_mater_corp,
    set_mater_br,
    set_mater_izd,
    set_shir_up,
    set_gl_up,
    set_vis_up,
    set_description,
    set_keys,
    set_kod_tovara,
    # sub_mech, todo:доделать
    set_pol,
    set_color_cir,
    # sub_forma,  todo:доделать
    set_vodo,
    set_gar,
    # set_nomenclatures,  todo:доделать
    # set_nomenclatures_color,  todo:доделать
    set_dop_opt,
]
default_update_list = [

]


class HService:
    _handlers_list = []

    def __init__(self, handlers_list=None):
        if handlers_list:
            self._handlers_list = handlers_list

    def apply(self, data, result_data):
        for handler in self._handlers_list:
            handler(result_data, data)
