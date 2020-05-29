segundos_str = input ("Por Favor, entre com o número de segundos que deseja converter:")
total_segs = int (segundos_str)

dias = total_segs // (24*3600)
segs_restantesfirst = total_segs % (24*3600)
horas = segs_restantesfirst // 3600
segs_restantessecond = segs_restantesfirst % 3600
minutos = segs_restantessecond // 60
segs_restantes_final = segs_restantessecond % 60

print (dias, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")