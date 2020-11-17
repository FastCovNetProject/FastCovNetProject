# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:11:01 2020

@author: belen
"""

#PASAR ARCHIVO .TXT A STRING IN PYTHON
enc ='iso-8859-15'
file = open('Extracted9.txt', 'r')
reader = str(file.read())

#NORMALIZAR
#import unicodedata
#normal = unicodedata.normalize('NFKD', reader).encode('ASCII', 'ignore')
#print(normal)

import unidecode
normal = unidecode.unidecode(reader)
#print(normal)

#SEPARAR POR INFORME Y CONVERTIR EN LISTA
todo = normal.replace('\n','')
puntos = todo.replace('--', '.')
valores_hemograma = puntos.replace('9/L [ =', '9/L [ .')
analiticas = puntos.split("Laboratori d'Urgencies")
list(analiticas)
#print(analiticas)



#LISTAS DE ITEMS DE ANALITICAS
nhc = []
fecha = []
sexo = []
edat = []
urea = []
creatinina = []
sodio = []
potasio = []
ala = []
tropo = []
ast = []
cloro = []
calcio = []
bilirrubina = []
ld = []
pcr = []
tp = []
ttpa = []
dd = []
albumina = []
leucocitos = []
neutrofilos = []
limfocitos = []
monocitos = []
eosinofilos = []
basofilos = []

eritrocitos = []
hb = []
hematocrito = []
plaquetas = []

error = []
e_con_nhc = 0
e_con_data = 0

u_text = 0

for pacient in analiticas: 
    if int(len(pacient)) == 0:
        pass
    if int(len(pacient)) > 0:

        start_nhc = pacient.find('NHC: ') + 5
        end_nhc = pacient.find('NHC: ') + 13
        e_con_nhc = pacient[start_nhc:end_nhc]
            
        start_fecha = pacient.find('Data recepcio mostra: ') + int(len('Data recepcio mostra: '))
        end_fecha = start_fecha + 10
        e_con_data = pacient[start_fecha:end_fecha]
       
        ##DISCRIMINADOR urea XX XY
                                    
        s_u = pacient.find(' ]Pla.Creatinini; c.subst.') - 1
        e_u = pacient.find(' ]Pla.Creatinini; c.subst.')
        u_text = pacient[s_u:e_u]
        try:
            int(u_text)
        

##COMUNES    
            nhc.append(pacient[start_nhc:end_nhc]) 
            
            fecha.append(pacient[start_fecha:end_fecha])
            
            start_sexo = pacient.find('Sexe: ') + int(len('Sexe: '))
            end_sexo = pacient.find(' Edat:')
            sexo.append(pacient[start_sexo:end_sexo])
            
            start_edat = pacient.find('Edat: ') + int(len('Edat: '))
            end_edat = pacient.find('Edat: ') + 8
            edat.append(pacient[start_edat:end_edat])
            
            start_sodio = pacient.find('Pla.Io sodi; c.subst.') + int(len('Pla.Io sodi; c.subst.'))
            end_sodio = pacient.find('mmol/L [ 135 - 147 ]')
            sodio.append(pacient[start_sodio:end_sodio])
            
            start_potasio = pacient.find('Pla.Io potassi; c.subst.') + int(len('Pla.Io potassi; c.subst.'))
            end_potasio = pacient.find('mmol/L [ 3.83 - 5.10 ]')
            potasio.append(pacient[start_potasio:end_potasio])
            
            start_tropo = pacient.find('Pla.Troponina T; c.massa ') + int(len('Pla.Troponina T; c.massa '))
            end_tropo = pacient.find('ng/L [ . 13 ]')
            tropop = pacient[start_tropo:end_tropo]
            if len(tropop) < len('Interferencia perhemolisi'):
                tropo.append(pacient[start_tropo:end_tropo])
            else: 
                tropo.append('notropo')
            
            start_cloro = pacient.find('Pla.Clorur; c.subst.')+ int(len('Pla.Clorur; c.subst.'))
            end_cloro = pacient.find('mmol/L [ 98 - 116 ]')    
            cloro.append(pacient[start_cloro:end_cloro])
            
            start_bilirrubina = pacient.find('Pla.Bilirubina; c.subst.') + int(len('Pla.Bilirubina; c.subst.'))
            end_bilirrubina = pacient.find('umol/L [ . 18 ]')
            bilirrubina.append(pacient[start_bilirrubina:end_bilirrubina]) 
            
            start_pcr = pacient.find('Pla.Proteina C reactiva; c.massa (CRM 470)') + int(len('Pla.Proteina C reactiva; c.massa (CRM 470)'))
            end_pcr = pacient.find('mg/L [ . 5.0 ]')
            pcr.append(pacient[start_pcr:end_pcr])
            
            start_tp = pacient.find('; IRP 67/40)') + int(len('; IRP 67/40)'))
            end_tp= pacient.find('; IRP 67/40)') + 19
            tp.append(pacient[start_tp:end_tp])
            
            start_ttpa = pacient.find('Pla.Coagulacio induida per una superficie; temps rel.(TTPA)') + int(len('Pla.Coagulacio induida per una superficie; temps rel.(TTPA)'))
            end_ttpa = pacient.find('Pla.Coagulacio induida per una superficie; temps rel.(TTPA)') + int(len('Pla.Coagulacio induida per una superficie; temps rel.(TTPA)')) + 5
            ttpa.append(pacient[start_ttpa:end_ttpa])
            
            start_dd = pacient.find('Pla.Dimer D de la fibrina; c.massa (immunoquim.) ') + int(len('Pla.Dimer D de la fibrina; c.massa (immunoquim.) '))
            end_dd = pacient.find('ug/L [ < 250 ]')
            dd.append(pacient[start_dd:end_dd])
            
            start_albumina = pacient.find('Pla.Albumina; c.massa') + int(len('Pla.Albumina; c.massa'))
            end_albumina = pacient.find('g/L [ 35 - 52 ]')
            albumina.append(pacient[start_albumina:end_albumina])
            
            start_leucos = pacient.find('San.Leucocits; c.nom.') + int(len('San.Leucocits; c.nom.'))
            end_leucos = pacient.find('x10E9/L [ 3.9 - 9.5 ]')
            leucosp = pacient[start_leucos:end_leucos]
            if len(leucosp) <= len('Interferencia perhemolisi'):
                leucocitos.append(pacient[start_leucos:end_leucos])
            else:
                leucocitos.append('no_hemograma')
            
            start_neutros = pacient.find('San.Neutrofils(segmentats); c.nom.') + int(len('San.Neutrofils(segmentats); c.nom.'))
            end_neutros = pacient.find('x10E9/L [ 1.50 - 5.70 ]')
            neutrosp = pacient[start_neutros:end_neutros]
            if len(neutrosp) <= len('Interferencia perhemolisi'):
                neutrofilos.append(pacient[start_neutros:end_neutros])
            else:
                neutrofilos.append(('no hemograma'))
            
            start_limfos = pacient.find('San.Limfocits;c.nom.') + int(len('San.Limfocits;c.nom.'))
            end_limfos = pacient.find('x10E9/L [ 1.30 - 3.40 ]')
            limfosp = pacient[start_limfos:end_limfos]
            if len(limfosp) <= len('Interferencia perhemolisi\n'):
                limfocitos.append(pacient[start_limfos:end_limfos])
            else:
                limfocitos.append('no_hemograma')
            
            start_mono = pacient.find('San.Monocits;c.nom.') + int(len('San.Monocits;c.nom.'))
            end_mono = pacient.find('x10E9/L [ . 0.92 ]')
            monop = pacient[start_mono:end_mono]
            if len(monop) <= len('Interferencia perhemolisi'):
                monocitos.append(pacient[start_mono:end_mono])
            else:
                monocitos.append('no_hemograma')
                
            start_eos = pacient.find('San.Eosinofils;c.nom.') + int(len('San.Eosinofils;c.nom.'))
            end_eos = pacient.find('x10E9/L [ . 0.39 ]')
            eosp = pacient[start_eos:end_eos]
            if len(eosp)  <= len('Interferencia perhemolisi'):
                eosinofilos.append(pacient[start_eos:end_eos])
            else:
                eosinofilos.append('no_hemograma')
                
            start_baso = pacient.find('San.Basofils;c.nom.') + int(len('San.Basofils;c.nom.'))
            end_baso = pacient.find('x10E9/L [ . 0.09 ]')
            basop = pacient[start_baso:end_baso]
            if len(basop)  <= len('Interferencia perhemolisi'): 
                basofilos.append(pacient[start_baso:end_baso])
            else:
                basofilos.append('no_hemograma')
            
                
            if int(u_text) == int(6):
                
                ##XY
                start_eritxy = pacient.find('San.Eritrocits; c.nom. ') + int(len('San.Eritrocits; c.nom. '))
                end_eritxy = pacient.find('x10E12/L [ 4.3 - 5.')
                eritrocitos.append(pacient[start_eritxy:end_eritxy])
                
                start_hbxy = pacient.find('San.Hemoglobina;c.massa') + int(len('San.Hemoglobina;c.massa'))
                end_hbxy = pacient.find('g/L [ 130 - 165 ]')
                hbp = pacient[start_hbxy:end_hbxy]
                if len(hbp) <= len('Interferencia perhemolisi'):
                    hb.append(pacient[start_hbxy:end_hbxy])
                else: 
                    hb.append('no_hemograma')
                
                start_hematocritxy = pacient.find('San.Eritrocits; fr.vol.(hematocrit)') + int(len('San.Eritrocits; fr.vol.(hematocrit)'))
                end_hematocritxy = pacient.find('% [ 40 - 50 ]')
                hematocritop = pacient[start_hematocritxy:end_hematocritxy]
                if len(hematocritop) <= len('Interferencia perhemolisi'):
                    hematocrito.append(pacient[start_hematocritxy:end_hematocritxy])
                else: 
                    hematocrito.append('no_hemograma') 
                
                start_plaquetasxy = pacient.find('San.Plaquetes;c.nom.') + int(len('San.Plaquetes;c.nom.'))
                end_plaquetasxy = pacient.find('x10E9/L [ 149 - 303 ]')
                plaquetasp = pacient[start_plaquetasxy:end_plaquetasxy]
                if len(plaquetasp) <= len('Interferencia perhemolisi'):
                    plaquetas.append(pacient[start_plaquetasxy:end_plaquetasxy])
                else:
                    plaquetas.append('no_hemograma')
                
                
                start_ureaxy = pacient.find('Pla.Urea; c.subst.') + int(len('Pla.Urea; c.subst.'))
                end_ureaxy = pacient.find('mmol/L [ 3.6 - 8.6 ]')
                urea.append(pacient[start_ureaxy:end_ureaxy])
                
                start_creatininaxy = pacient.find('Pla.Creatinini; c.subst.') + int(len('Pla.Creatinini; c.subst.'))
                end_creatininaxy = pacient.find('umol/L [ 59 - 104 ]')
                creatinina.append(pacient[start_creatininaxy:end_creatininaxy])
                
                start_alaxy = pacient.find('Pla.Alanina-aminotransferasa; c.cat.') + int(len('Pla.Alanina-aminotransferasa; c.cat.'))
                end_alaxy = pacient.find('U/L [ . 40 ]')
                alaxyj = pacient[start_alaxy:end_alaxy]
                if len(alaxyj) <= len('Interferencia perhemolisi'):
                    ala.append(pacient[start_alaxy:end_alaxy])
                else:
                    end_alaxyj = pacient.find(' U/L [ . 23 ]')
                    ala.append(pacient[start_alaxy:end_alaxyj])
                
                start_astxy = pacient.find('Pla.Aspartat-aminotransferasa; c.cat.') + int(len('Pla.Aspartat-aminotransferasa; c.cat.'))
                end_astxy = pacient.find('U/L [ . 39 ]')
                astj = pacient[start_astxy:end_astxy]
                if len(astj) <= len('Interferencia perhemolisi'):
                    ast.append(pacient[start_astxy:end_astxy]) 
                else:
                    end_astxyj = pacient.find(' U/L [ . 35 ]')
                    ast.append(pacient[start_astxy:end_astxyj])
                
                start_calcioxy = pacient.find('Pla.Calci(II); c.subst.') + int(len('Pla.Calci(II); c.subst.'))
                end_calcioxy = pacient.find('mmol/L [ 2.20 - 2.54 ]')
                calciop = pacient[start_calcioxy:end_calcioxy]
                if len(calciop) <= len('Interferencia perhemolisi'):
                    calcio.append(pacient[start_calcioxy:end_calcioxy])
                else: 
                    end_calcioxyj = pacient.find(' mmol/L [ 2.10 - 2.55 ]')
                    calcio.append(pacient[start_calcioxy:end_calcioxyj])
                
                start_ldxy = pacient.find('Lactat-deshidrogenasa; c.cat') + int(len('Lactat-deshidrogenasa; c.cat'))
                end_ldxy = pacient.find('U/L [ . 224 ]')
                ldp = pacient[start_ldxy:end_ldxy]
                if len(ldp) <= len('Interferencia perhemolisi'):
                    ld.append(pacient[start_ldxy:end_ldxy])
                else: 
                    end_ldxyj = pacient.find('U/L [ . 248 ]')
                    ld.append(pacient[start_ldxy:end_ldxyj])  
                
                
            if int(u_text) == int(0):
                ##XX
                start_eritxx = pacient.find('San.Eritrocits; c.nom. ') + int(len('San.Eritrocits; c.nom. '))
                end_eritxx = pacient.find('x10E12/L [ 3.9 - 5.1 ]')
                eritrocitos.append(pacient[start_eritxx:end_eritxx])
                
                start_hbxx = pacient.find('San.Hemoglobina;c.massa') + int(len('San.Hemoglobina;c.massa'))
                end_hbxx = pacient.find('g/L [ 120 - 147 ]')
                hbp = pacient[start_hbxx:end_hbxx]
                if len(hbp) <= len('Interferencia perhemolisi'):
                    hb.append(pacient[start_hbxx:end_hbxx])
                else: 
                    hb.append('no_hemograma') 
                    
                start_hematocritxx = pacient.find('San.Eritrocits; fr.vol.(hematocrit)') + int(len('San.Eritrocits; fr.vol.(hematocrit)'))
                end_hematocritxx = pacient.find('% [ 36 - 45 ]')                
                hematocritop = pacient[start_hematocritxx:end_hematocritxx]
                if len(hematocritop) <= len('Interferencia perhemolisi'):
                    hematocrito.append(pacient[start_hematocritxx:end_hematocritxx])
                else: 
                    hematocrito.append('no_hemograma')          
                    
                start_plaquetasxx = pacient.find('San.Plaquetes;c.nom.') + int(len('San.Plaquetes;c.nom.'))
                end_plaquetasxx = pacient.find('x10E9/L [ 153 - 368 ]')
                plaquetasp = pacient[start_plaquetasxx:end_plaquetasxx]
                if len(plaquetasp) <= len('Interferencia perhemolisi'):
                    plaquetas.append(pacient[start_plaquetasxx:end_plaquetasxx])
                else:
                    plaquetas.append('no_hemograma')
                
                start_ureaxx = pacient.find('Pla.Urea; c.subst.') + int(len('Pla.Urea; c.subst.'))
                end_ureaxx = pacient.find('mmol/L [ 3.3 - 8.0 ]')
                urea.append(pacient[start_ureaxx:end_ureaxx])
                
                start_creatininaxx = pacient.find('Pla.Creatinini; c.subst.') + int(len('Pla.Creatinini; c.subst.'))
                end_creatininaxx = pacient.find('umol/L [ 45 - 84 ]')
                creatinina.append(pacient[start_creatininaxx:end_creatininaxx])
                
                start_alaxx = pacient.find('Pla.Alanina-aminotransferasa; c.cat.') + int(len('Pla.Alanina-aminotransferasa; c.cat.'))
                end_alaxx = pacient.find('U/L [ . 32 ]')
                ala.append(pacient[start_alaxx:end_alaxx])
                
                start_astxx = pacient.find('Pla.Aspartat-aminotransferasa; c.cat.') + int(len('Pla.Aspartat-aminotransferasa; c.cat.'))
                end_astxx = pacient.find('U/L [ . 31 ]')
                ast.append(pacient[start_astxx:end_astxx]) 
                
                start_calcioxx = pacient.find('Pla.Calci(II); c.subst.') + int(len('Pla.Calci(II); c.subst.'))
                end_calcioxx = pacient.find('mmol/L [ 2.15 - 2.51 ]') 
                calcio.append(pacient[start_calcioxx:end_calcioxx])
                
                start_ldxx = pacient.find('L-Lactat-deshidrogenasa; c.cat') + int(len('L-Lactat-deshidrogenasa; c.cat'))
                end_ldxx = pacient.find('U/L [ . 213 ]')
                ld.append(pacient[start_ldxx:end_ldxx])
                
        except ValueError:
            error.append((e_con_nhc, e_con_data))
            pass
        except TypeError:
            error.append((e_con_nhc, e_con_data))
            pass
                
import csv
campos = [nhc, fecha, sexo, edat, urea, creatinina, sodio, potasio, ala, tropo, ast, cloro, calcio, 
          bilirrubina, ld, pcr, tp, ttpa, dd, albumina, eritrocitos, hb , hematocrito, plaquetas, leucocitos, 
          neutrofilos, limfocitos, monocitos, eosinofilos, basofilos]

with open('analiticas5.csv', 'w') as file:
    fieldnames = ['nhc', 'fecha', 'sexo', 'edad', 'urea', 'creatinina', 'sodio', 'potasio', 'ala', 'tropo', 'ast', 'cloro', 'calcio', 'bilirrubina', 'ld', 'pcr', 'tp', 'ttpa', 'dd', 'albumina', 'eritrocitos', 'hb', 'hematocrito', 'plaquetas', 'leucocitos', 'neutrofilos', 'limfocitos', 'monocitos', 'eosinofilos', 'basofilos']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    for i in range(len(nhc)):
        writer.writerow({'nhc': nhc[i], 'fecha': fecha[i], 'sexo': sexo[i], 'edad': edat[i], 
                          'urea': urea[i], 'creatinina': creatinina[i], 'sodio': sodio[i], 'potasio': potasio[i], 
                          'ala': ala[i], 'tropo': tropo[i], 'ast': ast[i], 'cloro': cloro[i], 'calcio': calcio[i], 
                          'bilirrubina': bilirrubina[i], 'ld': ld[i], 'pcr': pcr[i], 'tp': tp[i], 'ttpa': ttpa[i], 
                          'dd': dd[i], 'albumina': albumina[i], 'eritrocitos': eritrocitos[i], 'hb': hb[i], 
                          'hematocrito': hematocrito[i], 'plaquetas': plaquetas[i], 'leucocitos': leucocitos[i], 
                          'neutrofilos': neutrofilos[i], 'limfocitos': limfocitos[i], 'monocitos': monocitos[i], 
                          'eosinofilos': eosinofilos[i], 'basofilos': basofilos[i]})
    file.close()

with open('analiticas5.csv', 'r') as readfile:
    datos = readfile.read()
    print(datos)
    readfile.close()
