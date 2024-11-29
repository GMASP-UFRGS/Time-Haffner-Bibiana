import plotly.graph_objects as go
import py_dss_interface
import numpy as np
import matplotlib.pyplot as plt
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import random


###################################### INICIALIZAÇÃO ######################################
dss = py_dss_interface.DSSDLL()
dss.dss_clear_all()

###################################### CIRCUITO ######################################
dss_file = r"C:\Users\affon\Documents\OpenDSS\0.Material_TCC\main.dss"
dss.text("compile [{}]".format(dss_file))
dss.text('New energymeter.M1 line.L0 1')
dss.text("Set Maxiterations=1000")
dss.text("set MaxControlIter=1000")
dss.text("Set tolerance = 0.0001")

###################################### CONECTAR REDES DE BT ######################################
dss.text("redirect main_bt.dss")

########## REDE RESIDENCIAL #########
# OBSERVACOES: TODOS OS TRAFOS TIVERAM SEUS TAPS AJUSTADOS PARA 13.2 kV / CAPACITOR NA BARRA 8
dss.text("new Transformer.104R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=104 conn=delta kv=13.2 kva=500 wdg=2 bus=104R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.105R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=105 conn=delta kv=13.2 kva=500 wdg=2 bus=105R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.108R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=108 conn=delta kv=13.2 kva=500 wdg=2 bus=108R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.111R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=111 conn=delta kv=13.2 kva=500 wdg=2 bus=111R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.114R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=114 conn=delta kv=13.2 kva=500 wdg=2 bus=114R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.117R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=117 conn=delta kv=13.2 kva=500 wdg=2 bus=117R1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.120R0R1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=120 conn=delta kv=13.2 kva=500 wdg=2 bus=120R1 conn=wye kv=0.380 kva=500")
#CAPACITOR AUTOMÁTICO (TEMPO) LIGADO À BARRA 8 (capacitor adaptado para nova configuração de circuito, frente à configuração da Mariana. Antes era 1200 kVar)
dss.text('New capacitor.C8  Bus1=108  phases=3 kV=13.8 kvar=600')
dss.text('New CapControl.capCA8  element=line.L6  capacitor=C8   type=time ONsetting=8 OFFsetting=23')


########## REDE INDUSTRIAL #########
# OBSERVACOES: SOMENTE AS BARRAS 3, 7 E 13 NÃO TIVERAM SEUS TAPS AJUSTADOS PARA 13.2 kV / CAPACITOR NA BARRA 16
dss.text("new Transformer.103I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=103 conn=delta kv=13.8 kva=500 wdg=2 bus=103I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.107I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=107 conn=delta kv=13.8 kva=500 wdg=2 bus=107I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.110I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=110 conn=delta kv=13.2 kva=500 wdg=2 bus=110I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.113I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=113 conn=delta kv=13.8 kva=500 wdg=2 bus=113I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.116I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=116 conn=delta kv=13.2 kva=500 wdg=2 bus=116I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.119I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=119 conn=delta kv=13.2 kva=500 wdg=2 bus=119I1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.122I0I1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=122 conn=delta kv=13.2 kva=500 wdg=2 bus=122I1 conn=wye kv=0.380 kva=500")
# CAPACITOR FIXO LIGADO À BARRA 16 (capacitor retirado em função de novo circuito)
#dss.text('New capacitor.C16 Bus1=116  phases=3 kV=13.8 kvar=600')

########## REDE COMERCIAL #########
# OBSERVACOES: TODOS OS TRAFOS TIVERAM SEUS TAPS AJUSTADOS PARA 13.2 kV / CAPACITORES NAS BARRAS 9 E 21
dss.text("new Transformer.102C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=102 conn=delta kv=13.2 kva=500 wdg=2 bus=102C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.106C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=106 conn=delta kv=13.2 kva=500 wdg=2 bus=106C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.109C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=109 conn=delta kv=13.2 kva=500 wdg=2 bus=109C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.112C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=112 conn=delta kv=13.2 kva=500 wdg=2 bus=112C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.115C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=115 conn=delta kv=13.2 kva=500 wdg=2 bus=115C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.118C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=118 conn=delta kv=13.2 kva=500 wdg=2 bus=118C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.121C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=121 conn=delta kv=13.2 kva=500 wdg=2 bus=121C1 conn=wye kv=0.380 kva=500")
dss.text("new Transformer.123C0C1 Phases=3 Windings=2 XHL=0.04 %r=0.01 wdg=1 bus=123 conn=delta kv=13.2 kva=500 wdg=2 bus=123C1 conn=wye kv=0.380 kva=500")
# CAPACITOR FIXO LIGADO À BARRA 9
dss.text('New capacitor.C9 Bus1=109  phases=3 kV=13.8 kvar=600')
# CAPACITOR AUTOMÁTICO (TEMPO) LIGADO À BARRA 21
dss.text('New capacitor.C21  Bus1=121  phases=3 kV=13.8 kvar=600')
dss.text('New CapControl.capCA21 element=line.L19 capacitor=C21  type=time ONsetting=10 OFFsetting=22')


###################################### SISTEMA FOTOVOLTAICO ######################################
dss.text("New XYCurve.MyPvsT npts=4  xarray=[0  25  75  100]  yarray=[1.2 1.0 0.8 0.6]")
dss.text("New XYCurve.MyEff npts=4  xarray=[.1  .2  .4  1.0]  yarray=[.86  .9  .93  .97]")
dss.text("New Tshape.MyTemp npts=24 interval=1 temp=[25, 25, 25, 25, 25, 25, 25, 25, 35, 40, 45, 50, 60, 60, 55, 40, 35, 30, 25, 25, 25, 25, 25, 25]")

dss.text("New Loadshape.MyIrrad npts=24 interval=1 mult=[0 0 0 0 0 0 0.0001 0.0542 0.2443 0.4639 0.6479 0.7785 0.8517 0.8720 0.8408 0.7564 0.6166 0.4275 0.2089 0.0409 0.0005 0 0 0 ]") # Mês típico de verão (Elevado em Novembro)
#dss.text("New Loadshape.MyIrrad npts=24 interval=1 mult=[0 0 0 0 0 0 0 0.006 0.1710 0.4097 0.6121 0.7526 0.8318 0.8533 0.8202 0.7333 0.5878 0.3872 0.1642 0.0097 0 0 0 0]") # Mês típico de inverno (Elevado em Março)

potencias_cargas = np.array([200,15,52,55,35,47,100,120,20,20,25,25,8,16,8])
nivel_penetracao = 0.25
potencia_fv = potencias_cargas * nivel_penetracao

dss.text(f"New PVSystem.FV_104R1 phases=3 bus1=104R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R1 phases=3 bus1=105R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R1 phases=3 bus1=108R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R1 phases=3 bus1=111R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R1 phases=3 bus1=114R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R1 phases=3 bus1=117R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R1 phases=3 bus1=120R1 kV=0.380 kVA={potencia_fv[0]} Pmpp={potencia_fv[0]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_104R11 phases=3 bus1=104R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R11 phases=3 bus1=105R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R11 phases=3 bus1=108R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R11 phases=3 bus1=111R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R11 phases=3 bus1=114R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R11 phases=3 bus1=117R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R11 phases=3 bus1=120R11 kV=0.380 kVA={potencia_fv[1]} Pmpp={potencia_fv[1]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_104R15 phases=3 bus1=104R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R15 phases=3 bus1=105R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R15 phases=3 bus1=108R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R15 phases=3 bus1=111R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R15 phases=3 bus1=114R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R15 phases=3 bus1=117R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R15 phases=3 bus1=120R15 kV=0.380 kVA={potencia_fv[2]} Pmpp={potencia_fv[2]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_104R16 phases=3 bus1=104R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R16 phases=3 bus1=105R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R16 phases=3 bus1=108R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R16 phases=3 bus1=111R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R16 phases=3 bus1=114R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R16 phases=3 bus1=117R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R16 phases=3 bus1=120R16 kV=0.380 kVA={potencia_fv[3]} Pmpp={potencia_fv[3]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_104R17 phases=3 bus1=104R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R17 phases=3 bus1=105R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R17 phases=3 bus1=108R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R17 phases=3 bus1=111R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R17 phases=3 bus1=114R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R17 phases=3 bus1=117R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R17 phases=3 bus1=120R17 kV=0.380 kVA={potencia_fv[4]} Pmpp={potencia_fv[4]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_104R18 phases=3 bus1=104R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_105R18 phases=3 bus1=105R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_108R18 phases=3 bus1=108R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_111R18 phases=3 bus1=111R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_114R18 phases=3 bus1=114R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_117R18 phases=3 bus1=117R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_120R18 phases=3 bus1=120R18 kV=0.380 kVA={potencia_fv[5]} Pmpp={potencia_fv[5]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_103I2 phases=3 bus1=103I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_107I2 phases=3 bus1=107I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_110I2 phases=3 bus1=110I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_113I2 phases=3 bus1=113I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_116I2 phases=3 bus1=116I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_119I2 phases=3 bus1=119I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_122I2 phases=3 bus1=122I2 kV=0.380 kVA={potencia_fv[6]} Pmpp={potencia_fv[6]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C1 phases=3 bus1=102C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C1 phases=3 bus1=106C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C1 phases=3 bus1=109C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C1 phases=3 bus1=112C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C1 phases=3 bus1=115C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C1 phases=3 bus1=118C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C1 phases=3 bus1=121C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C1 phases=3 bus1=123C1 kV=0.380 kVA={potencia_fv[7]} Pmpp={potencia_fv[7]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C12 phases=3 bus1=102C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C12 phases=3 bus1=106C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C12 phases=3 bus1=109C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C12 phases=3 bus1=112C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C12 phases=3 bus1=115C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C12 phases=3 bus1=118C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C12 phases=3 bus1=121C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C12 phases=3 bus1=123C12 kV=0.380 kVA={potencia_fv[8]} Pmpp={potencia_fv[8]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C13 phases=3 bus1=102C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C13 phases=3 bus1=106C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C13 phases=3 bus1=109C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C13 phases=3 bus1=112C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C13 phases=3 bus1=115C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C13 phases=3 bus1=118C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C13 phases=3 bus1=121C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C13 phases=3 bus1=123C13 kV=0.380 kVA={potencia_fv[9]} Pmpp={potencia_fv[9]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C14 phases=3 bus1=102C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C14 phases=3 bus1=106C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C14 phases=3 bus1=109C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C14 phases=3 bus1=112C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C14 phases=3 bus1=115C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C14 phases=3 bus1=118C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C14 phases=3 bus1=121C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C14 phases=3 bus1=123C14 kV=0.380 kVA={potencia_fv[10]} Pmpp={potencia_fv[10]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C17 phases=3 bus1=102C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C17 phases=3 bus1=106C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C17 phases=3 bus1=109C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C17 phases=3 bus1=112C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C17 phases=3 bus1=115C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C17 phases=3 bus1=118C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C17 phases=3 bus1=121C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C17 phases=3 bus1=123C17 kV=0.380 kVA={potencia_fv[11]} Pmpp={potencia_fv[11]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C18 phases=3 bus1=102C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C18 phases=3 bus1=106C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C18 phases=3 bus1=109C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C18 phases=3 bus1=112C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C18 phases=3 bus1=115C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C18 phases=3 bus1=118C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C18 phases=3 bus1=121C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C18 phases=3 bus1=123C18 kV=0.380 kVA={potencia_fv[12]} Pmpp={potencia_fv[12]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C19 phases=3 bus1=102C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C19 phases=3 bus1=106C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C19 phases=3 bus1=109C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C19 phases=3 bus1=112C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C19 phases=3 bus1=115C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C19 phases=3 bus1=118C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C19 phases=3 bus1=121C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C19 phases=3 bus1=123C19 kV=0.380 kVA={potencia_fv[13]} Pmpp={potencia_fv[13]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

dss.text(f"New PVSystem.FV_102C20 phases=3 bus1=102C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff  P-TCurve=MyPvsT Daily=MyIrrad  TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_106C20 phases=3 bus1=106C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_109C20 phases=3 bus1=109C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_112C20 phases=3 bus1=112C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_115C20 phases=3 bus1=115C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_118C20 phases=3 bus1=118C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_121C20 phases=3 bus1=121C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")
dss.text(f"New PVSystem.FV_123C20 phases=3 bus1=123C20 kV=0.380 kVA={potencia_fv[14]} Pmpp={potencia_fv[14]} %cutin=0.1 %cutout=0.1 effcurve=Myeff P-TCurve=MyPvsT Daily=MyIrrad TDaily=MyTemp varfollowinverter=false")

###################################### CONTROLE ######################################
# VOLT-WATT
#dss.text("New XYCurve.vwatt_curve npts=3 Yarray=(1,1,0) XArray=(0.5,1.03,1.06)")
#dss.text("New InvControl.InvPVCtrl mode=VOLTWATT voltwatt_curve=vwatt_curve voltage_curvex_ref=rated")

# VOLT-VAR
#dss.text("New XYCurve.vvar_curve npts=6 Xarray=(0.5,0.92,0.98,1.02,1.08,1.5) Yarray=(1,1,0,0,-1,-1)")
#dss.text("New InvControl.InvPVCtr mode=VOLTVAR voltage_curvex_ref=rated vvc_curve1=vvar_curve")

#dss.text("New InvControl.VV_VW Combimode=VV_VW voltage_curvex_ref=rated vvc_curve1=vvar_curve voltwatt_curve=vwatt_curve VoltwattYAxis=PMPPPU RefReactivePower=varmax")

###################################### SOLVER ######################################################
dss.text("Set VoltageBases = [13.8 0.380]")
dss.text("CalcVoltageBases")
dss.text("BusCoords coord_sistema.csv")
dss.text("New monitor.101_power element=Line.L0 terminal=1 mode=1")


def pegar_posicao_das_barras_com_carga():
    # Lista pré-informada de barras
    barras_MT = ['101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113','114', '115','116', '117', '118', '119', '120', '121', '122', '123']
    barras_com_carga = [
    "102c1", "102c12", "102c13", "102c14", "102c17", "102c18", "102c19", "102c20",
    "106c1", "106c12", "106c13", "106c14", "106c17", "106c18", "106c19", "106c20",
    "109c1", "109c12", "109c13", "109c14", "109c17", "109c18", "109c19", "109c20",
    "112c1", "112c12", "112c13", "112c14", "112c17", "112c18", "112c19", "112c20",
    "121c1", "121c12", "121c13", "121c14", "121c17", "121c18", "121c19", "121c20",
    "115c1", "115c12", "115c13", "115c14", "115c17", "115c18", "115c19", "115c20",
    "118c1", "118c12", "118c13", "118c14", "118c17", "118c18", "118c19", "118c20",
    "123c1", "123c12", "123c13", "123c14", "123c17", "123c18", "123c19", "123c20",
    "103i2", "107i2", "110i2", "122i2", "113i2", "116i2", "119i2",
    "104r1", "104r11", "104r15", "104r16", "104r17", "104r18",
    "105r1", "105r11", "105r15", "105r16", "105r17", "105r18",
    "108r1", "108r11", "108r15", "108r16", "108r17", "108r18",
    "111r1", "111r11", "111r15", "111r16", "111r17", "111r18",
    "120r1", "120r11", "120r15", "120r16", "120r17", "120r18",
    "114r1", "114r11", "114r15", "114r16", "114r17", "114r18",
    "117r1", "117r11", "117r15", "117r16", "117r17", "117r18"]


    # Retorna uma lista com o nome de todas as barras
    nome_barras = dss.circuit_all_bus_names()

    # Inicializa as listas
    indices_barras_MT = []
    indices_barras_com_carga = []

    # Retorna o índice de cada barra na matriz geral de nome de barras, com base nas matrizes informadas anteriormente
    for nome_barra in nome_barras:
        if nome_barra in barras_MT:
            indices_barras_MT.append(nome_barras.index(nome_barra))
        if nome_barra in barras_com_carga:
            indices_barras_com_carga.append(nome_barras.index(nome_barra))

    return indices_barras_MT, indices_barras_com_carga, barras_com_carga
indices_barras_MT, indices_barras_com_carga, barras_com_carga = pegar_posicao_das_barras_com_carga()

tensao_barras_com_carga_dict = {barra: [] for barra in barras_com_carga}
# Inicializa os dicionários para armazenar os registros de DRC e DRP
nlc_dict = {barra: [0] * 24 for barra in barras_com_carga}
nlp_dict = {barra: [0] * 24 for barra in barras_com_carga}
DRC = {barra: 0 for barra in barras_com_carga}
DRP = {barra: 0 for barra in barras_com_carga}
compensacao = {barra: 0 for barra in barras_com_carga}

def definir_variaveis():
    tensao_todas_barras = np.zeros((24,len(dss.circuit_all_bus_names())))  # Parametriza uma matriz inicial, com 24 linhas (horas do dia) e o número das barras
    tensao_todas_barras_com_carga = np.zeros((24,len(indices_barras_com_carga)))  # Parametriza uma matriz inicial, com 24 linhas (horas do dia) e o número das barras com carga

    power = np.zeros((24, 2))
    perdas = np.zeros((24, 1))

    # Para o cálculo de todas as barras
    z_loop_horario = np.zeros((24, len(dss.circuit_all_bus_names())))
    z_horario = np.zeros(24)
    z_total = {}

    # Para o cálculo por grupo de barras
    z_loop_horario_ = {}
    z_horario_ = {}
    z_total_dict = {}  # Inicializa um dicionário para armazenar z_total_102 a z_total_123

    # Inicialize z_total_102 a z_total_123
    for i in range(102, 124):
        z_total_dict[i] = {}

    # Indices das barras
    barras_bt_101 = [0]
    barras_bt_102 = [1, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]
    barras_bt_103 = [2, 309, 310]
    barras_bt_104 = [3, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
    barras_bt_105 = [4, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218]
    barras_bt_106 = [5, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]
    barras_bt_107 = [6, 311, 312]
    barras_bt_108 = [7, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236]
    barras_bt_109 = [15, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]
    barras_bt_110 = [16, 313, 314]
    barras_bt_111 = [17, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254]
    barras_bt_112 = [18, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]
    barras_bt_113 = [8, 315, 316]
    barras_bt_114 = [9, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272]
    barras_bt_115 = [10, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
    barras_bt_116 = [11, 317, 318]
    barras_bt_117 = [12, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290]
    barras_bt_118 = [13, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]
    barras_bt_119 = [14, 319, 320]
    barras_bt_120 = [19, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308]
    barras_bt_121 = [20, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]
    barras_bt_122 = [21, 321, 322]
    barras_bt_123 = [22, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182]
    # Dicionário criado, para chamar posteriormente
    agrupamento_de_barras = {
        "101": barras_bt_101,
        "102": barras_bt_102,
        "103": barras_bt_103,
        "104": barras_bt_104,
        "105": barras_bt_105,
        "106": barras_bt_106,
        "107": barras_bt_107,
        "108": barras_bt_108,
        "109": barras_bt_109,
        "110": barras_bt_110,
        "111": barras_bt_111,
        "112": barras_bt_112,
        "113": barras_bt_113,
        "114": barras_bt_114,
        "115": barras_bt_115,
        "116": barras_bt_116,
        "117": barras_bt_117,
        "118": barras_bt_118,
        "119": barras_bt_119,
        "120": barras_bt_120,
        "121": barras_bt_121,
        "122": barras_bt_122,
        "123": barras_bt_123
    }

    # Para armazenar o estado dos capacitores
    status_C9 = np.zeros(24)
    status_C21 = np.zeros(24)
    status_C16 = np.zeros(24)
    status_C8 = np.zeros(24)
    return (tensao_todas_barras, tensao_todas_barras_com_carga, power, z_loop_horario, z_horario,z_total, z_loop_horario_, z_horario_,agrupamento_de_barras, z_total_dict,perdas, status_C9, status_C8, status_C16, status_C21)
tensao_todas_barras, tensao_todas_barras_com_carga, power, z_loop_horario, z_horario,z_total, z_loop_horario_, z_horario_,agrupamento_de_barras, z_total_dict,perdas, status_C9, status_C8, status_C16, status_C21 = definir_variaveis()

data_pvsystem = []
pvsystem_data = {f"pvsystem_{i}": [] for i in range(113)}
kw_sum = []
kvar_sum = []
kw_alimentadora_total = 0.0
kvar_alimentadora_total = 0.0
kw_gd_total = 0.0
kvar_gd_total = 0.0

for hora in range(24): # índice começa em 0, mas o range é 24, no caso, a contagem vai de 0 a 23
    dss.text(f"Set mode=daily stepsize=1h number={hora+1}") #Neste caso, a contagem começa em 1 e vai até 24
    dss.solution_solve()

    # Para plotagem do gráfico das tensões de todas as cargas
    tensao = np.array(dss.circuit_all_node_vmag_pu_by_phase(1))  # plota todas as tensões desse loop, da fase 1
    tensao_todas_barras[hora, :] = tensao  # armazena as tensões de todos os loops

    # Para cálculo do Z
    tensao_barras_com_carga = tensao[indices_barras_com_carga]
    tensao_todas_barras_com_carga[hora, :] = tensao_barras_com_carga

    # Para plotagem da curva de potência da barra alimentadora
    power[hora,:]= dss.circuit_total_power()

    # Somando os valores da primeira coluna (kw_total)
    kw_alimentadora_total += power[hora, 0]
    # Somando os valores da segunda coluna (kvar_total)
    kvar_alimentadora_total += power[hora, 1]

    # Para cálculo do DRC e DRP
    # Para plotagem do gráfico das tensões das barras com cargas
    for i, indice in enumerate(indices_barras_com_carga):
        barras_nomes = dss.circuit_all_bus_names()
        barra = barras_nomes[indice]
        tensao_barras_com_carga_dict[barra].append(tensao[indice])

        """# Verificações de depuração
        if barra == "123c17":
            print(
                f"Hora: {hora}, Tensão: {tensao[180]}, Tensão: {tensao_barras_com_carga_dict[barra][hora]}")"""


        # Avaliação de DRC e DRP
        if tensao[indice] < 0.8711:
            nlc_dict[barra][hora] = 1
        elif 0.8711 <= tensao[indice] < 0.9211:
            nlp_dict[barra][hora] = 1
        elif 0.9211 <= tensao[indice] <= 1.05:
            nlc_dict[barra][hora] = 0
            nlp_dict[barra][hora] = 0
        elif 1.05 < tensao[indice] <= 1.0605:
            nlp_dict[barra][hora] = 1
        elif tensao[indice] > 1.0605:
            nlc_dict[barra][hora] = 1

    kw_total = 0.0
    kvar_total = 0.0

    dss.pvsystems_first()
    for pvsystem in range(113):
        name_pvsystem = dss.pvsystems_read_name()
        kw_pvsystem = dss.pvsystems_kw()
        kvar_pvsystem = dss.pvsystems_read_kvar()

        data_pvsystem.append([hora, name_pvsystem, kw_pvsystem, kvar_pvsystem])

        # Armazene os dados no dicionário
        pvsystem_data[f"pvsystem_{pvsystem}"].append([hora, name_pvsystem, kw_pvsystem, kvar_pvsystem])

        kw_total += kw_pvsystem
        kvar_total += kvar_pvsystem

        dss.pvsystems_next()

    kw_sum.append((hora, kw_total))
    kvar_sum.append((hora, kvar_total))

    # Somando os valores de KW e KVAR
    kw_gd_total = np.sum(kw_sum)
    kvar_gd_total = np.sum(kvar_sum)

    # Para cálculo das perdas horárias
    perdas[hora,:] = dss.meters_register_values()[12]
    perdas_horarias = perdas[1:] - perdas[:-1] # Subtrai o valor das perdas da hora anterior
    perdas_horarias = np.insert(perdas_horarias, 0, perdas[0]) # Insere o valor inicial das perdas, na hora 1

    # Para cálculo do desvio de tensão total (z) de todas as barras e por hora
    z_loop_horario[hora, :len(tensao_barras_com_carga)] = np.maximum.reduce([tensao_barras_com_carga - 1.05, 0.9211 - tensao_barras_com_carga, np.zeros(len(tensao_barras_com_carga))])
    z_horario[hora] = np.sum(z_loop_horario[hora, :len(tensao_barras_com_carga)])

    # Para cálculo do desvio de tensão total (z) por grupo de barras e por hora
    for grupo, barras in agrupamento_de_barras.items():  # Primeiro ele cria as matrizes para cada grupo de barras, para depois executar o cálculo
        if grupo not in z_loop_horario_:
            z_loop_horario_[grupo] = np.zeros((24,len(barras) - 1))  # Subtrai 1 para desconsiderar o primeiro elemento, ou seja, elimina as barras de MT do cálculo de Z
            z_horario_[grupo] = np.zeros(24)

        barras_sem_media_tensao = barras[1:]  # Exclui o primeiro elemento da lista
        z_loop_horario_[grupo][hora, :len(barras_sem_media_tensao)] = np.maximum.reduce([tensao[barras_sem_media_tensao] - 1.05, 0.9211 - tensao[barras_sem_media_tensao],np.zeros(len(barras_sem_media_tensao))])
        z_horario_[grupo][hora] = np.sum(z_loop_horario_[grupo][hora, :len(barras_sem_media_tensao)])

    # Pega o status dos capacitores
    def pega_status_capacitores():
        dss.capacitors_write_name('C9')
        status_C9[hora] = dss.capacitors_read_states()[0]
        dss.capacitors_write_name('C21')
        status_C21[hora] = dss.capacitors_read_states()[0]
        #dss.capacitors_write_name('C16')
        #status_C16[hora] = dss.capacitors_read_states()[0]
        dss.capacitors_write_name('C8')
        status_C8[hora] = dss.capacitors_read_states()[0]
    pega_status_capacitores()

consumo_por_barra = np.array([2223.174317, 166.7380738, 578.0253225, 611.3729373, 389.0555055, 522.4459646, 1265.742055, 1505.06422, 250.8440367, 250.8440367, 313.5550459, 313.5550459, 100.3376147, 200.6752294, 100.3376147])
consumo_mensal = 30 * consumo_por_barra


# Para cálculo do desvio de tensão total das barras com carga
z_total = np.mean(z_horario)
# Para cálculo do desvio de tensão total, por grupo de barras
for i in range(102, 124):
    grupo = str(i)
    z_total_dict[i] = np.mean(z_horario_[grupo])

# Calcula os valores de DRP e DRC para cada barra, considerando 24 amostras
for barra in barras_com_carga:
    DRC[barra] = (sum(nlc_dict[barra])/24)*100
    DRP[barra] = (sum(nlp_dict[barra])/24)*100

    if DRP[barra] <= 3:
        k1 = 0
    elif DRP[barra] > 3:
        k1 = 3

    if DRC[barra] <= 0.5:
        k2 = 0
    elif DRP[barra] > 0.5:
        k2 = 7

    compensacao[barra] = ((DRP[barra] - 3) / 100) * k1 + ((DRC[barra] - 0.5) / 100) * k2

def calculo_compensacoes():
    compensacoes = {}

    compensacoes['104r1'] = compensacao['104r1'] * consumo_mensal[0]
    compensacoes['104r11'] = compensacao['104r11'] * consumo_mensal[1]
    compensacoes['104r15'] = compensacao['104r15'] * consumo_mensal[2]
    compensacoes['104r16'] = compensacao['104r16'] * consumo_mensal[3]
    compensacoes['104r17'] = compensacao['104r17'] * consumo_mensal[4]
    compensacoes['104r18'] = compensacao['104r18'] * consumo_mensal[5]

    compensacoes['105r1'] = compensacao['105r1'] * consumo_mensal[0]
    compensacoes['105r11'] = compensacao['105r11'] * consumo_mensal[1]
    compensacoes['105r15'] = compensacao['105r15'] * consumo_mensal[2]
    compensacoes['105r16'] = compensacao['105r16'] * consumo_mensal[3]
    compensacoes['105r17'] = compensacao['105r17'] * consumo_mensal[4]
    compensacoes['105r18'] = compensacao['105r18'] * consumo_mensal[5]

    compensacoes['108r1'] = compensacao['108r1'] * consumo_mensal[0]
    compensacoes['108r11'] = compensacao['108r11'] * consumo_mensal[1]
    compensacoes['108r15'] = compensacao['108r15'] * consumo_mensal[2]
    compensacoes['108r16'] = compensacao['108r16'] * consumo_mensal[3]
    compensacoes['108r17'] = compensacao['108r17'] * consumo_mensal[4]
    compensacoes['108r18'] = compensacao['108r18'] * consumo_mensal[5]

    compensacoes['111r1'] = compensacao['111r1'] * consumo_mensal[0]
    compensacoes['111r11'] = compensacao['111r11'] * consumo_mensal[1]
    compensacoes['111r15'] = compensacao['111r15'] * consumo_mensal[2]
    compensacoes['111r16'] = compensacao['111r16'] * consumo_mensal[3]
    compensacoes['111r17'] = compensacao['111r17'] * consumo_mensal[4]
    compensacoes['111r18'] = compensacao['111r18'] * consumo_mensal[5]

    compensacoes['114r1'] = compensacao['114r1'] * consumo_mensal[0]
    compensacoes['114r11'] = compensacao['114r11'] * consumo_mensal[1]
    compensacoes['114r15'] = compensacao['114r15'] * consumo_mensal[2]
    compensacoes['114r16'] = compensacao['114r16'] * consumo_mensal[3]
    compensacoes['114r17'] = compensacao['114r17'] * consumo_mensal[4]
    compensacoes['114r18'] = compensacao['114r18'] * consumo_mensal[5]

    compensacoes['117r1'] = compensacao['117r1'] * consumo_mensal[0]
    compensacoes['117r11'] = compensacao['117r11'] * consumo_mensal[1]
    compensacoes['117r15'] = compensacao['117r15'] * consumo_mensal[2]
    compensacoes['117r16'] = compensacao['117r16'] * consumo_mensal[3]
    compensacoes['117r17'] = compensacao['117r17'] * consumo_mensal[4]
    compensacoes['117r18'] = compensacao['117r18'] * consumo_mensal[5]

    compensacoes['120r1'] = compensacao['120r1'] * consumo_mensal[0]
    compensacoes['120r11'] = compensacao['120r11'] * consumo_mensal[1]
    compensacoes['120r15'] = compensacao['120r15'] * consumo_mensal[2]
    compensacoes['120r16'] = compensacao['120r16'] * consumo_mensal[3]
    compensacoes['120r17'] = compensacao['120r17'] * consumo_mensal[4]
    compensacoes['120r18'] = compensacao['120r18'] * consumo_mensal[5]

    compensacoes['103i2'] = compensacao['103i2'] * consumo_mensal[6]
    compensacoes['107i2'] = compensacao['107i2'] * consumo_mensal[6]
    compensacoes['110i2'] = compensacao['110i2'] * consumo_mensal[6]
    compensacoes['113i2'] = compensacao['113i2'] * consumo_mensal[6]
    compensacoes['116i2'] = compensacao['116i2'] * consumo_mensal[6]
    compensacoes['119i2'] = compensacao['119i2'] * consumo_mensal[6]
    compensacoes['122i2'] = compensacao['122i2'] * consumo_mensal[6]

    compensacoes['102c1'] = compensacao['102c1'] * consumo_mensal[7]
    compensacoes['102c12'] = compensacao['102c12'] * consumo_mensal[8]
    compensacoes['102c13'] = compensacao['102c13'] * consumo_mensal[9]
    compensacoes['102c14'] = compensacao['102c14'] * consumo_mensal[10]
    compensacoes['102c17'] = compensacao['102c17'] * consumo_mensal[11]
    compensacoes['102c18'] = compensacao['102c18'] * consumo_mensal[12]
    compensacoes['102c19'] = compensacao['102c19'] * consumo_mensal[13]
    compensacoes['102c20'] = compensacao['102c20'] * consumo_mensal[14]

    compensacoes['106c1'] = compensacao['106c1'] * consumo_mensal[7]
    compensacoes['106c12'] = compensacao['106c12'] * consumo_mensal[8]
    compensacoes['106c13'] = compensacao['106c13'] * consumo_mensal[9]
    compensacoes['106c14'] = compensacao['106c14'] * consumo_mensal[10]
    compensacoes['106c17'] = compensacao['106c17'] * consumo_mensal[11]
    compensacoes['106c18'] = compensacao['106c18'] * consumo_mensal[12]
    compensacoes['106c19'] = compensacao['106c19'] * consumo_mensal[13]
    compensacoes['106c20'] = compensacao['106c20'] * consumo_mensal[14]

    compensacoes['109c1'] = compensacao['109c1'] * consumo_mensal[7]
    compensacoes['109c12'] = compensacao['109c12'] * consumo_mensal[8]
    compensacoes['109c13'] = compensacao['109c13'] * consumo_mensal[9]
    compensacoes['109c14'] = compensacao['109c14'] * consumo_mensal[10]
    compensacoes['109c17'] = compensacao['109c17'] * consumo_mensal[11]
    compensacoes['109c18'] = compensacao['109c18'] * consumo_mensal[12]
    compensacoes['109c19'] = compensacao['109c19'] * consumo_mensal[13]
    compensacoes['109c20'] = compensacao['109c20'] * consumo_mensal[14]

    compensacoes['112c1'] = compensacao['112c1'] * consumo_mensal[7]
    compensacoes['112c12'] = compensacao['112c12'] * consumo_mensal[8]
    compensacoes['112c13'] = compensacao['112c13'] * consumo_mensal[9]
    compensacoes['112c14'] = compensacao['112c14'] * consumo_mensal[10]
    compensacoes['112c17'] = compensacao['112c17'] * consumo_mensal[11]
    compensacoes['112c18'] = compensacao['112c18'] * consumo_mensal[12]
    compensacoes['112c19'] = compensacao['112c19'] * consumo_mensal[13]
    compensacoes['112c20'] = compensacao['112c20'] * consumo_mensal[14]

    compensacoes['115c1'] = compensacao['115c1'] * consumo_mensal[7]
    compensacoes['115c12'] = compensacao['115c12'] * consumo_mensal[8]
    compensacoes['115c13'] = compensacao['115c13'] * consumo_mensal[9]
    compensacoes['115c14'] = compensacao['115c14'] * consumo_mensal[10]
    compensacoes['115c17'] = compensacao['115c17'] * consumo_mensal[11]
    compensacoes['115c18'] = compensacao['115c18'] * consumo_mensal[12]
    compensacoes['115c19'] = compensacao['115c19'] * consumo_mensal[13]
    compensacoes['115c20'] = compensacao['115c20'] * consumo_mensal[14]

    compensacoes['118c1'] = compensacao['118c1'] * consumo_mensal[7]
    compensacoes['118c12'] = compensacao['118c12'] * consumo_mensal[8]
    compensacoes['118c13'] = compensacao['118c13'] * consumo_mensal[9]
    compensacoes['118c14'] = compensacao['118c14'] * consumo_mensal[10]
    compensacoes['118c17'] = compensacao['118c17'] * consumo_mensal[11]
    compensacoes['118c18'] = compensacao['118c18'] * consumo_mensal[12]
    compensacoes['118c19'] = compensacao['118c19'] * consumo_mensal[13]
    compensacoes['118c20'] = compensacao['118c20'] * consumo_mensal[14]

    compensacoes['121c1'] = compensacao['121c1'] * consumo_mensal[7]
    compensacoes['121c12'] = compensacao['121c12'] * consumo_mensal[8]
    compensacoes['121c13'] = compensacao['121c13'] * consumo_mensal[9]
    compensacoes['121c14'] = compensacao['121c14'] * consumo_mensal[10]
    compensacoes['121c17'] = compensacao['121c17'] * consumo_mensal[11]
    compensacoes['121c18'] = compensacao['121c18'] * consumo_mensal[12]
    compensacoes['121c19'] = compensacao['121c19'] * consumo_mensal[13]
    compensacoes['121c20'] = compensacao['121c20'] * consumo_mensal[14]

    compensacoes['123c1'] = compensacao['123c1'] * consumo_mensal[7]
    compensacoes['123c12'] = compensacao['123c12'] * consumo_mensal[8]
    compensacoes['123c13'] = compensacao['123c13'] * consumo_mensal[9]
    compensacoes['123c14'] = compensacao['123c14'] * consumo_mensal[10]
    compensacoes['123c17'] = compensacao['123c17'] * consumo_mensal[11]
    compensacoes['123c18'] = compensacao['123c18'] * consumo_mensal[12]
    compensacoes['123c19'] = compensacao['123c19'] * consumo_mensal[13]
    compensacoes['123c20'] = compensacao['123c20'] * consumo_mensal[14]

    return compensacoes
compensacoes = calculo_compensacoes()



###################################### IMPRIMIR ######################################
#dss.text("plot monitor object=101_power")
#dss.text("Plot Profile Phases=ALL labels=y")
#dss.text("plot circuit Max=1000 labels=y")
#print("Perdas totais = {} kWh".format(perdas[23]))
#print(f"Total de KW da alimentadora: {kw_alimentadora_total}")
#print(f"Total de KVAR da alimentadora: {kvar_alimentadora_total}")
#print(f"Soma total de KW: {kw_gd_total}")
#print(f"\nSoma total de KVAR: {kvar_gd_total}")
#print(dss.circuit_all_bus_names().index("115c1"))

def imprimir_compensacoes(compensacoes):
    # Filtrar apenas as barras com compensação diferente de zero e ordenar decrescentemente
    compensacoes_filtradas = {k: v for k, v in compensacoes.items() if v != 0}
    compensacoes_ordenadas = dict(sorted(compensacoes_filtradas.items(), key=lambda item: item[1], reverse=True))

    # Calcular o valor total de compensações
    total_compensacoes = sum(compensacoes_ordenadas.values())

    # Preparar dados para o gráfico
    barras = list(compensacoes_ordenadas.keys())
    valores = list(compensacoes_ordenadas.values())

    # Gerar gráfico de barras vertical
    trace = go.Bar(
        x=barras,
        y=valores,
        marker=dict(color='skyblue')
    )

    layout = go.Layout(
        title='Compensação por Barra',
        xaxis=dict(title='Barras', tickangle=-45),  # Rotaciona os nomes das barras para melhor visualização
        yaxis=dict(title='Compensação por barra (kWh)'),
        plot_bgcolor='white'
    )

    fig = go.Figure(data=[trace], layout=layout)

    # Salvar o gráfico como um arquivo HTML
    pyo.plot(fig, filename='compensacao_por_barra.html')

    # Imprimir o valor total de compensações no prompt
    print(f'Total de Compensação: {total_compensacoes:.2f} kWh')
#imprimir_compensacoes(compensacoes)


# Imprime a curva de potência Ativa e Reativa na barra alimentadora
def imprimir_power():
    horas = np.arange(1, 25)

    # Plotar gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(horas, -power[:, 0], label='P (kW)')
    #plt.plot(horas, power[:, 1], label='Q (kVAR)')
    plt.xlabel('Hora')
    plt.ylabel('Potência')
    plt.title('Potência Exigida pela Barra Alimentadora')
    plt.legend()
    plt.grid(True)
    plt.show()
#imprimir_power()

#print(power) #Potência que sai da barra é negativa no OpenDSS
def imprimir_power_stairs():
    # Adiciona a hora 0 ao início e a hora 24 ao final
    horas = np.arange(0, 25)

    # Adiciona o valor final ao início para fechar o loop corretamente
    power_p = np.append(-power[-1, 0], -power[:, 0])
    power_q = np.append(-power[-1, 1], -power[:, 1])


    # Criando os dados de escada
    horas_stairs = np.repeat(horas, 2)[1:-1]  # Duplicando e ajustando as horas para escada
    power_p_stairs = np.repeat(power_p, 2)[:-1]  # Duplicando e ajustando os valores de P
    power_q_stairs = np.repeat(power_q, 2)[:-1]  # Duplicando e ajustando os valores de Q

    print(power_p)
    print(power_q)
    print(sum(power_p)+power[-1, 0])
    print(sum(power_q)+power[-1, 1])

    trace1 = go.Scatter(
        x=horas_stairs,
        y=power_p_stairs,
        mode='lines',
        name='P (kW)',
        line_shape='hv'  # Forma horizontal-vertical para criar degraus
    )

    trace2 = go.Scatter(
        x=horas_stairs,
        y=power_q_stairs,
        mode='lines',
        name='Q (kvar)',
        line_shape='hv'  # Forma horizontal-vertical para criar degraus
    )

    layout = go.Layout(
        xaxis=dict(
            title='Hora do dia',
            titlefont=dict(size=24),  # Tamanho do título do eixo x
            tickfont=dict(size=18),   # Tamanho dos valores do eixo x
            showgrid=True,
            gridcolor='lightgray',
            tickvals=np.arange(0, 25, 1),  # Adiciona ticks em todas as horas
            ticktext=[str(i) for i in range(25)],  # Adiciona labels de hora
            dtick=1  # Define a frequência das linhas de grade
        ),
        yaxis=dict(
            title='Potência (kW/kvar)',
            titlefont=dict(size=24),  # Tamanho do título do eixo y
            tickfont=dict(size=20),   # Tamanho dos valores do eixo y
            showgrid=True,
            gridcolor='lightgray'
        ),
        legend=dict(
            font=dict(size=24)  # Tamanho do texto da legenda
        ),
        showlegend=True,
        plot_bgcolor='white',  # Definindo o fundo do gráfico como branco
        shapes=[
            # Linha horizontal em y=0
            dict(
                type='line',
                x0=0,
                y0=0,
                x1=24,
                y1=0,
                line=dict(
                    color='lightgray',
                    width=2
                )
            )
        ],
    )

    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # Mostrar o gráfico
    pyo.plot(fig, filename='potencia_exigida.html')
imprimir_power_stairs()

# Imprime a curva de perdas horárias
def imprime_perdas():
    # Preparar o eixo x
    horas = np.arange(1, 25)

    # Para garantir que o valor da hora 0 (x=0) seja igual ao valor da hora 24
    perdas_grafico = np.append(perdas_horarias, perdas_horarias[0])

    # Preparar o eixo x incluindo a hora 0
    horas = np.append([0], horas)

    # Plotar o gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(horas, perdas_grafico, marker='o')
    plt.xlabel('Hora do Dia')
    plt.ylabel('Perdas (kWh)')
    plt.title('Perdas Horárias ao Longo do Dia')
    plt.xticks(np.arange(0, 25, 1))
    plt.grid(True)
    plt.show()
#imprime_perdas()

# Imprime o estado dos capacitores
def imprimir_capstate():
    # Preparar os valores do eixo x
    horas = np.arange(1, 25)

    # Ajustar os status para incluir o valor em x=0 igual ao valor em x=24
    status_C9_ext = np.append([status_C9[-1]], status_C9)
    status_C21_ext = np.append([status_C21[-1]], status_C21)
    status_C16_ext = np.append([status_C16[-1]], status_C16)
    status_C8_ext = np.append([status_C8[-1]], status_C8)

    # Preparar o eixo x incluindo a hora 0
    horas_ext = np.append([0], horas)

    # Plotar o gráfico de degrau
    plt.figure(figsize=(12, 6))
    plt.step(horas_ext, status_C9_ext, where='post', marker='o', label='C9 (Fixo de 600 kVA)')
    plt.step(horas_ext, status_C21_ext, where='post', marker='o', label='C21 (Autom. de 600 kVA)')
    plt.step(horas_ext, status_C16_ext, where='post', marker='o', label='C16 (Fixo de 600 kVA)')
    plt.step(horas_ext, status_C8_ext, where='post', marker='o', label='C8 (Autom. de 1200 kVA)')

    plt.xlabel('Hora do Dia')
    plt.ylabel('Status dos Capacitores')
    plt.title('Status dos Capacitores ao Longo do Dia')
    plt.xticks(np.arange(0, 25, 1))
    plt.grid(True)
    plt.legend()
    plt.show()
#imprimir_capstate()

def imprime_todas_matrizes_z():
    # Exemplo de impressão dos valores
    print("Desvio total de tensão das barras com carga (24 hrs) = {}".format(z_total))
    #print(z_horario)
    #for i in range(102, 124):
        #print(f'Z médio da barra {i}: {z_total_dict[i]}')
        #print(f'Matriz Z horária da barra {i}:')
        #print(z_horario_[f"{i}"])
        #print("\n")
#imprime_todas_matrizes_z()

def imprimir_geracao_gd():
    app = dash.Dash(__name__)

    # Converta as listas de dados em DataFrames do pandas
    pvsystem_dfs = {key: pd.DataFrame(data_pvsystem, columns=["Hora", "Name", "kW", "kVar"]) for key, data_pvsystem in
                    pvsystem_data.items()}

    # Layout do aplicativo
    app.layout = html.Div([
        dcc.Dropdown(
            id='pvsystem-dropdown',
            options=[{'label': df['Name'].iloc[0], 'value': key} for key, df in pvsystem_dfs.items()],
            value='pvsystem_0'
        ),
        dcc.Graph(id='pvsystem-graph')
    ])

    # Callback para atualizar o gráfico com base no dropdown selecionado
    @app.callback(
        Output('pvsystem-graph', 'figure'),
        [Input('pvsystem-dropdown', 'value')]
    )
    def update_graph(selected_pvsystem):
        df = pvsystem_dfs[selected_pvsystem]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Hora'], y=df['kW'], mode='lines', name='kW'))
        fig.add_trace(go.Scatter(x=df['Hora'], y=df['kVar'], mode='lines', name='kVar'))

        fig.update_layout(
            title=f'Sistema PV: {df["Name"].iloc[0]}',
            xaxis_title='Hora',
            yaxis_title='Potência (kW/kVAr)',
            template='plotly_white'
        )

        return fig

    # Executa o aplicativo
    if __name__ == '__main__':
        app.run_server(debug=True)
#imprimir_geracao_gd()

def imprimir_geracao_total_gd():
    # Inicialize a aplicação Dash
    app = dash.Dash(__name__)

    # Criação do gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[hora for hora, _ in kw_sum], y=[valor for _, valor in kw_sum], mode='lines+markers',
                             name='Total kW', line=dict(shape='hv')))
    fig.add_trace(go.Scatter(x=[hora for hora, _ in kvar_sum], y=[valor for _, valor in kvar_sum], mode='lines+markers',
                             name='Total kVAr', line=dict(shape='hv')))

    fig.update_layout(
        title='Soma de Potência por Hora (Formato Escada)',
        xaxis_title='Hora',
        yaxis_title='Potência (kW/kVAr)',
        template='plotly_white'
    )

    # Layout do aplicativo
    app.layout = html.Div([
        dcc.Graph(id='pvsystem-graph', figure=fig)
    ])

    # Executa o aplicativo
    if __name__ == '__main__':
        app.run_server(debug=True)
#imprimir_geracao_total_gd()

def imprimir_todas_barras():
    barra = dss.circuit_all_bus_names()  # Obtenha os nomes das barras

    # Cria a aplicação Dash
    app = dash.Dash(__name__)

    # Layout da aplicação
    app.layout = html.Div([
        html.Div([
            dcc.Dropdown(
                id='barra-selection',
                options=[{'label': f'Barra {barra[i]}', 'value': barra[i]} for i in range(len(barra))],
                value=[],  # Nenhuma barra selecionada por padrão
                multi=True
            ),
            html.Button('Selecionar Todas', id='select-all-button', n_clicks=0),
            html.Button('Deselecionar Todas', id='deselect-all-button', n_clicks=0),
        ], style={'display': 'flex', 'flexDirection': 'column'}),
        dcc.Tabs([
            dcc.Tab(label='Curvas de Tensão', children=[
                dcc.Graph(id='tensao-graph')
            ]),
            dcc.Tab(label='Boxplot de Tensão', children=[
                dcc.Graph(id='boxplot-graph')
            ])
        ]),
    ])

    # Callback para selecionar todas as barras
    @app.callback(
        Output('barra-selection', 'value'),
        [Input('select-all-button', 'n_clicks'),
         Input('deselect-all-button', 'n_clicks')],
        [State('barra-selection', 'options')]
    )
    def select_deselect_all(select_all_clicks, deselect_all_clicks, options):
        ctx = dash.callback_context
        if not ctx.triggered:
            return []  # Nenhuma barra selecionada por padrão
        else:
            button_id = ctx.triggered[0]['prop_id'].split('.')[0]
            if button_id == 'select-all-button':
                return [option['value'] for option in options]
            elif button_id == 'deselect-all-button':
                return []

    # Callback para atualizar o gráfico de tensão
    @app.callback(
        Output('tensao-graph', 'figure'),
        Input('barra-selection', 'value')
    )
    def update_tensao_graph(selected_barras):
        fig = go.Figure()

        for i in range(tensao_todas_barras.shape[1]):
            if barra[i] in selected_barras:
                y_values = tensao_todas_barras[:, i].tolist()
                y_values.insert(0, y_values[-1])
                fig.add_trace(go.Scatter(
                    x=np.arange(25),  # de 0 a 24
                    y=y_values,
                    mode='lines',
                    line_shape='hv',  # Passo horizontal-vertical
                    name=f'Barra {barra[i]}'
                ))

        fig.update_layout(
            title='Curvas de Tensão ao Longo do Dia',
            xaxis_title='Hora do Dia',
            yaxis_title='Tensão (pu)',
            shapes=[
                {'type': 'line', 'y0': 0.8711, 'y1': 0.8711, 'x0': 0, 'x1': 1, 'xref': 'paper', 'line': {'color': 'red','dash': 'dash'}},
                {'type': 'line', 'y0': 0.9211, 'y1': 0.9211, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'green','dash': 'dash'}},
                {'type': 'line', 'y0': 1.05, 'y1': 1.05, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'green', 'dash': 'dash'}},
                {'type': 'line', 'y0': 1.0605, 'y1': 1.0605, 'x0': 0, 'x1': 1, 'xref': 'paper', 'line': {'color': 'red', 'dash': 'dash'}}
            ],
            plot_bgcolor='white'
        )
        return fig

    # Callback para atualizar o gráfico boxplot
    @app.callback(
        Output('boxplot-graph', 'figure'),
        Input('barra-selection', 'value')
    )
    def update_boxplot_graph(selected_barras):
        df = pd.DataFrame(tensao_todas_barras, columns=barra)

        # Filtrar as barras selecionadas
        df_selected = df[selected_barras]

        # Agrupar os dados por hora
        df_melted = df_selected.melt(var_name='Barra', value_name='Tensão', ignore_index=False)
        df_melted['Hora'] = df_melted.index

        fig = go.Figure()

        for hora in range(24):
            tensoes_hora = df_melted[df_melted['Hora'] == hora]['Tensão']
            fig.add_trace(go.Box(y=tensoes_hora, name=f'{hora}h'))

        fig.update_layout(
            title='Boxplot de Tensões por Hora do Dia',
            xaxis_title='Hora do Dia',
            yaxis_title='Tensão (pu)',
            plot_bgcolor='white',
            shapes = [
                {'type': 'line', 'y0': 0.8711, 'y1': 0.8711, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'red', 'dash': 'dash'}},
                {'type': 'line', 'y0': 0.9211, 'y1': 0.9211, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'green', 'dash': 'dash'}},
                {'type': 'line', 'y0': 1.05, 'y1': 1.05, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'green', 'dash': 'dash'}},
                {'type': 'line', 'y0': 1.0605, 'y1': 1.0605, 'x0': 0, 'x1': 1, 'xref': 'paper','line': {'color': 'red', 'dash': 'dash'}}
        ]
        )
        return fig

    # Executa a aplicação Dash
    if __name__ == '__main__':
        app.run_server(debug=True)
#imprimir_todas_barras()

cores_fixas = {}
def imprimir_tensoes_barras_carga():
    # Nomes das barras
    nome_barras = dss.circuit_all_bus_names()

    app = dash.Dash(__name__)

    app.layout = html.Div([
        html.Div([
            dcc.Dropdown(
                id='dropdown-barras',
                options=[{'label': k, 'value': k} for k in agrupamento_de_barras.keys()],
                value=['101'],
                multi=True
            ),
            dcc.Dropdown(
                id='dropdown-barras-individuais',
                options=[],
                value=[],
                multi=True
            ),
        ], style={'width': '50%', 'display': 'inline-block'}),

        dcc.Graph(id='graph-tensoes')
    ])

    @app.callback(
        Output('dropdown-barras-individuais', 'options'),
        [Input('dropdown-barras', 'value')]
    )
    def update_dropdown_barras_individuais(selected_groups):
        options = []
        for group in selected_groups:
            indices = [int(i) for i in agrupamento_de_barras[group]]
            options.extend([{'label': nome_barras[i], 'value': i} for i in indices])
        return options

    @app.callback(
        Output('graph-tensoes', 'figure'),
        [Input('dropdown-barras', 'value'),
         Input('dropdown-barras-individuais', 'value')]
    )
    def update_graph(selected_groups, selected_barras):
        fig = go.Figure()

        # Função para gerar cores aleatórias
        def random_color():
            r = lambda: random.randint(0, 255)
            return f'rgb({r()},{r()},{r()})'

        # Adicionar as linhas para os grupos selecionados
        for group in selected_groups:
            indices = [int(i) for i in agrupamento_de_barras[group]]
            df = pd.DataFrame(tensao_todas_barras[:, indices], columns=[nome_barras[i] for i in indices])

            for col in df.columns:
                if selected_barras is None or col in selected_barras:
                    # Atribuir uma cor fixa se ainda não tiver uma
                    if col not in cores_fixas:
                        cores_fixas[col] = random_color()
                    # Adicionando o valor da hora 24 no início para a hora 0
                    y_values = df[col].tolist()
                    y_values.insert(0, y_values[-1])
                    linha = go.Scatter(
                        x=np.arange(25),  # de 0 a 24
                        y=y_values,
                        mode='lines',
                        name=f'{group} - {col}',
                        line=dict(color=cores_fixas[col]),
                        line_shape='hv'  # Passo horizontal-vertical
                    )
                    fig.add_trace(linha)

        # Adicionar linhas para as barras individuais selecionadas
        if selected_barras:
            for barra in selected_barras:
                barra_label = nome_barras[int(barra)]
                # Atribuir uma cor fixa se ainda não tiver uma
                if barra_label not in cores_fixas:
                    cores_fixas[barra_label] = random_color()
                # Adicionando o valor da hora 24 no início para a hora 0
                y_values = tensao_todas_barras[:, int(barra)].tolist()
                y_values.insert(0, y_values[-1])
                linha_individual = go.Scatter(
                    x=np.arange(25),  # de 0 a 24
                    y=y_values,
                    mode='lines',
                    name=f'{barra_label}',
                    line=dict(color=cores_fixas[barra_label]),
                    line_shape='hv'  # Passo horizontal-vertical
                )
                fig.add_trace(linha_individual)

        fig.update_layout(
            title="Tensões por hora",
            xaxis_title="Hora",
            yaxis_title="Tensão (pu)",
            yaxis=dict(range=[0.9, 1.1], showgrid=False, zerolinecolor='grey'),  # Remover as linhas do grid do eixo y
            xaxis=dict(showgrid=False, zerolinecolor='grey'),  # Remover as linhas do grid do eixo x
            plot_bgcolor='white'
        )

        fig.add_shape(type="line", x0=0, y0=1.05, x1=24, y1=1.05,
                      line=dict(color="red", width=2, dash="dash"))
        fig.add_shape(type="line", x0=0, y0=0.93, x1=24, y1=0.93,
                      line=dict(color="red", width=2, dash="dash"))

        return fig

    if __name__ == '__main__':
        app.run_server(debug=True)
#imprimir_tensoes_barras_carga()

def imprimir_DRC_DRP():
    # Exemplo de uso dos valores somados
    for barra in barras_com_carga:
        #print(f"Barra: {barra}, DRC: {DRC[barra]}%, DRP: {DRP[barra]}%")
        print(f'Compensação {barra} = {compensacao[barra]}')
#imprimir_DRC_DRP()