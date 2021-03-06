#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FloatValue class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Spin(BlockModel):

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.extension = "gtk"
        self.label = "Spin"
        self.color = "250:150:150:150"
        self.group = "Form"
        self.ports = [
                {
                "type": "mosaicode_lib_c_base.extensions.ports.float",
                "name": "float_value",
                "conn_type": "Input",
                "label": "Float Value"
                },{
                "type":"mosaicode_lib_c_base.extensions.ports.float",
                "label":"Click",
                "conn_type":"Output",
                "name":"click"
                }]

        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "value": "0"
                            },
                            {"name": "value",
                            "label": "Value",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "min",
                            "label": "Min",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 0
                            },
                            {"name": "max",
                            "label": "Max",
                            "type": MOSAICODE_FLOAT,
                            "lower": -20000,
                            "upper": 20000,
                            "step": 1,
                            "value": 200000
                            },
                            {"name": "step",
                            "label": "Step",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "digits",
                            "label": "Digits",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 20000,
                            "step": 1,
                            "value": 1
                            }
                           ]

        self.codes["declaration"] = """
GtkWidget *spin_$id$;
float_callback * $port[click]$;
int $port[click]$_size = 0;

void $port[float_value]$(float value){
    gtk_spin_button_set_value(GTK_SPIN_BUTTON(spin_$id$), value);
}

void spin$id$_callback(GtkSpinButton *widget, gboolean state, void * data){
    float result = (float)gtk_spin_button_get_value(widget);
    for(int i = 0 ; i < $port[click]$_size ; i++){
        (*($port[click]$[i]))(result);
   }
}
"""

        self.codes["setup"] = """
    spin_$id$ = gtk_spin_button_new_with_range(
                $prop[min]$,
                $prop[max]$,
                $prop[step]$);
    gtk_spin_button_set_digits(GTK_SPIN_BUTTON(spin_$id$), $prop[digits]$);
    gtk_spin_button_set_value(GTK_SPIN_BUTTON(spin_$id$), $prop[value]$);
    g_signal_connect(
                G_OBJECT(spin_$id$),
                "value-changed",
                G_CALLBACK(spin$id$_callback),
                NULL
                );
    gtk_fixed_put(GTK_FIXED(fixed_layout), spin_$id$, $prop[x]$, $prop[y]$);
"""
